import tensorflow as tf 
import numpy as np 

with tf.Session() as sess:
    data = np.reshape(np.arange(18),[3,6])

x = tf.constant(data)
result = tf.gather_nd(x,[1,3])
print(result.eval(session=sess))


x=[2.,3.,5.]
y=[0.,3.,5.]
eq = tf.equal(x,y)
cast_Val = tf.cast(eq,tf.float32)