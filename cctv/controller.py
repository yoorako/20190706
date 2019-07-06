from cctv.cctv_pop import CCTVModel
from cctv.crime_police import CrimeModel
from cctv.police_norm import PoliceNormModel
from cctv.police_chart import PoliceChart
from cctv.folium_test import FoliumTest
from cctv.crime_map import CrimeMap

class CCTVController:
    def __init__(self):
        # self._m = CCTVModel()
        # self._m = CrimeModel()
        # self._m = PoliceNormModel()
        # self._m = PoliceChart()
        # self._m = FoliumTest()
        self._m = CrimeMap()

    def test(self):
        m = self._m
        m.hook()





    def test(self):

        m = self._m

        m.hook()