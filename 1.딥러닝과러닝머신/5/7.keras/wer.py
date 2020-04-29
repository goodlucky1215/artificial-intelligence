import tensorflow as tf
import keras
from keras.backend.tensorflow_backend import set_session
sess = tf.compat.v1.Session()
hello = tf.constant('Hello')
sess.run(hello)
b'Hello'

