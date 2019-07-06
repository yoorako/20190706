import tensorflow as tf
import numpy as np

class CabbageController:
    def __init__(self,avg_temp,min_temp,max_temp,rain_fall):
        self.avg = avg_temp
        self.min = min_temp
        self.max = max_temp
        self.rain = rain_fall

    def service(self):
        X = tf.placeholder(tf.float32, shape=[None, 4])
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        saver = tf.train.Saver()

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            save_path = 'cabbage/data/saved.ckpt'
            saver.restore(sess, save_path)
            data = [[self.avg,self.min, self.max, self.rain],]
            arr = np.array(data, dtype=np.float32)
            dict = sess.run(tf.matmul(X, W) + b, {X: arr[0:4]})
            print(dict[0])
        return int(dict[0])

