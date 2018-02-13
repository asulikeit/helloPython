'''
Created on 2018. 1. 16.

@author: SDS
'''

import tensorflow as tf

sess = tf.Session()
a = tf.constant(10)
b = tf.constant(20)
print(sess.run(a + b))