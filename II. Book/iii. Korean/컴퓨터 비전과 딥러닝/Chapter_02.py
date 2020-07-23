# Date : 2020-07-23-Thu
# Deep Learning for Computer Vision
# 컴퓨터 비전과 딥러닝
# 텐서플로와 케라스를 사용한 전문 가이드
# Chapter 2

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist_data = input_data.read_data_sets('MNIST_data', one_hot=True)

input_size = 784
no_classes = 10
batch_size = 100
total_batces = 200

x_input = tf.placeholder(tf.float32, shape=[None, input_size])
y_input = tf.placeholder(tf.float32, shape=[None, no_classes])

weights = tf.Variable(tf.random_normal([input_size, no_classes]))
bias = tf.Variable(tf.random_normal([no_classes]))

logits = tf.matmul(x_input, weights) + bias

softmax_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y_input, logits=logits)
loss_operation = tf.reduce_mean(softmax_cross_entropy)
optimiser = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(loss_operation)

session = tf.Session()
session.run(tf.global_variables_initializer())

for batch_no in range(total_batces):
    mnist_batch = mnist_data.train.next_batch(batch_size)
    _, loss_value = session.run([optimiser, loss_operation], feed_dict={x_input: mnist_batch[0], y_input: mnist_batch[1]})
    print(loss_value)

predictions = tf.argmax(logits, 1)
correct_predictions = tf.equal(predictions, tf.argmax(y_input, 1))
accuracy_operation = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
test_images, test_labels = mnist_data.test.images, mnist_data.test.labels
accuracy_value = session.run(accuracy_operation, feed_dict={x_input: test_images, y_input: test_labels})
print('Accuracy: ', accuracy_value)
session.close()
