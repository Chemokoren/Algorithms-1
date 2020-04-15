import tensorflow as tf

exponential = tf.train.exponential_decay
inverse_time = tf.train.inverse_time_decay
natural_exp = tf.train.natural_exp_decay
polynomial = tf.train.polynomial_decay
cosine = tf.train.cosine_decay
linear_cosine = tf.train.linear_cosine_decay
noisy_linear_cosine = tf.train.noisy_linear_cosine_decay
