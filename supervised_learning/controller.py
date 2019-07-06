
from supervised_learning.ram_price import RamPrice



class SupervisedLearningController:



    def __init__(self):

        self._m = RamPrice()



    def test(self):

        m = self._m

        m.hook()