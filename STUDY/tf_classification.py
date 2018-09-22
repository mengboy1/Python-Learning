#用tensorflow解决classification(分类)问题

#MNIST是手写数字库，数据中包含55000张训练图片，每张图片的分辨率是28*28
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

def add_layer(inputs,in_size,out_size,activation_function=None):
	Weights = tf.Variable(tf.random_normal([in_size,out_size]))
	biases = tf.Variable(tf.zeros([1,out_size])+0.1)
	Wx_plus_b = tf.matmul(inputs,Weights) + biases
	if activation_function is None:
		outputs = Wx_plus_b
	else:
		outputs = activation_function(Wx_plus_b)
	return outputs

def compute_accuracy(v_xs, v_ys):
	global prection
	y_pre = sess.run(prection, feed_dict={xs: v_xs})
	correct_prection = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
	accuracy = tf.reduce_mean(tf.cast(correct_prection, tf.float32))
	result  =sess.run(accuracy,feed_dict={xs: v_xs, ys: v_ys})
	return result

xs = tf.placeholder(tf.float32, [None,784]) #28*28
ys = tf.placeholder(tf.float32, [None,10])
prection = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prection),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
	if i % 50 == 0:
		print(compute_accuracy(mnist.test.images,mnist.test.labels))