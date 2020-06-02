#binod suman deep learning playlist

#hello world

first=tf.constant('Hello')
second = tf.constant("Tensor")

fullword = first+second
print(fullword)

with tf.Session() as sess:
	result = sess.run(fullword)

result