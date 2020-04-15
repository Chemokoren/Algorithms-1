import shutil
import tensorflow as tf

from . import losses
from . import metrics as Metrics
from .modes import TRAIN, EVAL, PREDICT
from .training import optimizer as create_optimizer
from .utils import call_fn, logger, dataset


def spec(mode=None, predictions=None, loss=None, optimizer=None, metrics=None, train_op=None, **keywords):
    if mode is None and predictions is not None:
        mode = PREDICT

    if mode == PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions, **keywords)

    if mode == tf.estimator.ModeKeys.TRAIN:
        if train_op is None:
            train_op = create_train_op(optimizer, loss)
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op, **keywords)

    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=metrics, **keywords)


class Estimator():

    def __init__(self, model, **keywords):
        self._hooks = self._get_hooks()
        self.estimator = self._create_estimator(model_fn=model, **keywords)

    def train(self, x, y=None, epochs=1, batch_size=128, shuffle=True, **keywords):
        input_fn = dataset(x=x,
                           y=y,
                           epochs=epochs,
                           batch_size=batch_size,
                           shuffle=shuffle)
        self._update_kwargs(TRAIN, keywords)
        self.estimator.train(input_fn=input_fn, **keywords)

    def evaluate(self, x, y=None, batch_size=128, **keywords):
        input_fn = dataset(x=x,
                           y=y,
                           batch_size=batch_size,
                           shuffle=False)
        self._update_kwargs(EVAL, keywords)
        return self.estimator.evaluate(input_fn=input_fn, **keywords)

    def predict(self, x, batch_size=128, **keywords):
        input_fn = dataset(x=x,
                           batch_size=batch_size,
                           shuffle=False)
        self._update_kwargs(PREDICT, keywords)
        return self.estimator.predict(input_fn=input_fn, **keywords)

    __call__ = predict

    def _create_estimator(self, model_fn, model_dir=None, params=None, **keywords):
        defaults = self._defaults()
        if model_dir is None:
            model_dir = defaults.get('model_dir')
            shutil.rmtree(model_dir, ignore_errors=True)
            logger.warn('Using temporary folder as model directory: {}'.format(model_dir))
        params = defaults.get('params', {}) if params is None else params
        model_fn = self._wrap_model_fn(model_fn)
        return tf.estimator.Estimator(model_fn=model_fn, model_dir=model_dir, params=params, **keywords)

    def _defaults(self):
        return {
            'model_dir': '/tmp/estimator_model_dir',
        }

    def _wrap_model_fn(self, model_fn):

        def fn(features, labels, mode, params, config):
            if list(features.keys()) == ['x']:
                features = features['x']
            ret = call_fn(model_fn, features, labels, mode=mode, params=params, config=config)
            if not isinstance(ret, tf.estimator.EstimatorSpec):
                if mode == PREDICT:
                    ret = spec(predictions=ret)
                else:
                    ret = spec(mode=mode, **ret)
            return ret

        return fn

    def _get_hooks(self):
        return {}

    def _update_kwargs(self, mode, keywords):
        hooks = self._hooks.get(mode, []) + keywords.get('hooks', [])
        if hooks:
            keywords['hooks'] = hooks


class Model(Estimator):

    def __init__(self, network, loss=None, optimizer=None, metrics=None, **keywords):
        model_fn = create_model_fn(network, loss, optimizer, metrics)
        super(Model, self).__init__(model_fn, **keywords)


def create_model_fn(network, loss_fn, optimizer, metrics):
    metrics = metrics or {}
    if isinstance(loss_fn, str):
        loss_fn = getattr(losses, loss_fn)
    if isinstance(metrics, list):
        metrics = [getattr(Metrics, metric) if isinstance(metric, str) else metric for metric in metrics]
        metrics = {metric.__name__: metric for metric in metrics}

    def model_fn(features, labels, mode, params, config):
        outputs = call_fn(network, features, mode=mode, params=params, config=config)
        if isinstance(outputs, tuple):
            outputs, predictions = outputs
        else:
            predictions = outputs
        if mode == PREDICT:
            return predictions

        loss = loss_fn(labels, outputs)
        eval_metric_ops = {name: metric(labels, outputs) for name, metric in metrics.items()}
        return dict(loss=loss,
                    optimizer=optimizer,
                    metrics=eval_metric_ops)

    return model_fn


def create_train_op(optimizer, loss):
    if isinstance(optimizer, tf.Operation):
        return optimizer
    global_step = tf.train.get_global_step()
    if isinstance(optimizer, tuple):
        optimizer = create_optimizer(*optimizer)
    if not isinstance(optimizer, tf.train.Optimizer) and callable(optimizer):
        return call_fn(optimizer, loss, global_step=global_step)
    return optimizer.minimize(loss=loss, global_step=global_step)
