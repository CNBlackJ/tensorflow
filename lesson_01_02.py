#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tensorflow as tf

# 创建constant op
matrix1 = tf.constant([[1., 1.], [3., 4.], [5., 6.]]) # 3x2矩阵
matrix2 = tf.constant([[2., 3.],[2., 4.]]) # 2x2矩阵

# 创建矩阵乘法matmul op
product = tf.matmul(matrix1, matrix2)

sess = tf.Session()
result = sess.run(product)

print result

sess.close()