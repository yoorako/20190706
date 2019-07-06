from cctv.controller import CCTVController
from cctv.data_reader import DataReader
if __name__ == '__main__':
    ctrl = CCTVController()
    ctrl.test()
    # dr = DataReader()
    # print(dr.create_gmaps())