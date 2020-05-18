import tensorflow as tf

from . import clips
from . import decays
from . import optimizers


def clip(fn_name, **kwargs):
    fn = getattr(clips, fn_name)
    if fn_name in ['global_norm']:
        wrapper = lambda values: fn(values, **kwargs)[0]
    else:
        wrapper = lambda values: [fn(v, **kwargs) for v in values]
    return wrapper


def decay(fn_name, **kwargs):
    fn = getattr(decays, fn_name)

    def wrapper(learning_rate, global_step):
        learning_rate = float(learning_rate)
        return fn(learning_rate=learning_rate, global_step=global_step, **kwargs)

    return wrapper


def optimizer(class_name, learning_rate, **kwargs):
    class_ = getattr(optimizers, class_name)
    decay = kwargs.pop('decay', None)
    clip = kwargs.pop('clip', None)

    def wrapper(loss, global_step):
        if decay is not None:
            lr = decay(learning_rate, global_step=global_step)
        else:
            lr = learning_rate

        if clip is not None:
            class Optimizer(class_):

                def apply_gradients(self, grads_and_vars, global_step=None, name=None):
                    grads, vars_ = zip(*grads_and_vars)
                    grads = clip(grads)
                    grads_and_vars = zip(grads, vars_)
                    return super(Optimizer, self).apply_gradients(grads_and_vars, global_step=global_step, name=name)
        else:
            Optimizer = class_

        # AdagradDA requies global_step as an argument
        if class_ in [optimizers.AdagradDA] and 'global_step' not in kwargs:
            kwargs['global_step'] = global_step

        return Optimizer(lr, **kwargs).minimize(loss=loss, global_step=global_step)

    return wrapper
