#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tensorflow as tf

# 创建一个变量，初始化为光标量：0
state = tf.Variable(0, name="counter")

# state = state + 1
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init_op)
    print sess.run(state)

    for _ in range(5):
        sess.run(update)
        print sess.run(state)