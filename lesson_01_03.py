#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tensorflow as tf
# 交互式会话（Interactive Session）
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# 使用初始化器 initializer op 的 run() 初始化 'x'
x.initializer.run()

# 减法sub op
sub = tf.sub(x, a)
print sub.eval()