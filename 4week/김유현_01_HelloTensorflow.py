import tensorflow as tf
__author__ = "youhyeoneee(김유현)"
#출처 : https://www.youtube.com/watch?v=-57Ne86Ia8w&feature=youtu.be
#Create a constant op
#this op is added as a node to the default graph
hello = tf.constant('Hello, TendorFlow!')

#sess = tf.Session()
sess = tf.Session()

#run the op and get result
print(sess.run(hello))

