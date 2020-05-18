import argparse
import inspect
import logging
import numpy as np
import tensorflow as tf

try:
    import pandas
except (IOError, ImportError):
    pandas = None

logger = logging.getLogger('estimator')
logger.setLevel(logging.INFO)

to_categorical = tf.keras.utils.to_categorical


def dataset(x, y=None, epochs=1, **keywords):
    if isinstance(x, np.ndarray):
        fn = tf.estimator.inputs.numpy_input_fn
    elif pandas is not None and isinstance(x, pandas.DataFrame):
        fn = tf.estimator.inputs.pandas_input_fn
    else:
        fn = None

    if fn is not None:
        if not isinstance(x, dict):
            x = {'x': x}
        return fn(x=x, y=y, num_epochs=epochs, **keywords)

    return x


def to_dense(x):
    return tf.argmax(x, axis=1) if len(x.shape) > 1 and x.shape[1] > 1 else x


def call_fn(fn, *args, **keywords):
    sig = inspect.signature(fn)
    kwargs = {}
    for keyword, value in keywords.items():
        if keyword in sig.parameters:
            kwargs[keyword] = value
    return fn(*args, **kwargs)


def cli(**keywords):
    parser = argparse.ArgumentParser()
    for name, value in keywords.items():
        type_ = None if value is None else type(value)
        parser.add_argument('--' + name, default=value, type=type_)
    return parser.parse_args()
