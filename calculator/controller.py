import tensorflow as tf

class CalculatorController:
    def __init__(self, num1, num2, opcode):
        self._num1 = num1
        self._num2 = num2
        self._opcode = opcode

    def calc(self):
        n1 = self._num1
        n2 = self._num2
        opcode = self._opcode

        print('컨트롤러에 넘어온 값 n1 = {}, n2 = {}, op = {}'.format(n1,n2,opcode ))

        tf.reset_default_graph()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver = tf.train.import_meta_graph('calculator/saved_'+opcode+'_model/model-1000.meta')
            saver.restore(sess, tf.train.latest_checkpoint('calculator/saved_'+opcode+'_model'))

            graph = tf.get_default_graph()
            w1 = graph.get_tensor_by_name('w1:0')
            w2 = graph.get_tensor_by_name('w2:0')
            print('num1 is {}\n'.format(float(n1)))
            print('num2 is {}'.format(float(n2)))
            feed_dict = {w1: float(n1), w2: float(n2)}

            op_to_restore = graph.get_tensor_by_name("op_"+opcode+":0")
            result = sess.run(op_to_restore, feed_dict)
            print('최종결과 : {}'.format(result))
        return result