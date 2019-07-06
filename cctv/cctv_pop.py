import pandas as pd
import numpy as np
from cctv.data_reader import DataReader

class CCTVModel:
    def __init__(self):
        self.dr = DataReader()

    def hook(self) -> object:
        self.create_cctv_pop()

    def create_cctv_pop(self)->object:
        self.dr.context = './data/'
        self.dr.fname = 'CCTV_in_Seoul.csv'
        cctv = self.dr.csv_to_dframe()
        # print(cctv)
        cctv_idx = cctv.columns
        # print(cctv_idx)
        # print('::::::::::::::::::::::::::::')
        self.dr.fname = 'population_in_Seoul.xls'
        pop = self.dr.xls_to_dframe(2, 'B,D,G,J,N')
        # print(pop)
        pop_idx = pop.columns
        # print(pop_idx)

        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)
        pop.rename(columns={pop.columns[0]: '구별',
                            pop.columns[1]: '인구수',
                            pop.columns[2]: '한국인',
                            pop.columns[3]: '외국인',
                            pop.columns[4]: '고령자'
                            }, inplace=True)

        # cctv.sort_values(by='소계', ascending=True)
        pop.drop([0], inplace=True)
        # print(pop['구별'].unique())
        # print(pop['구별'].isnull()) # 26행이 null
        pop.drop([26], inplace=True)

        pop['외국인비율'] = pop['외국인'] / pop['인구수'] * 100
        pop['고령자비율'] = pop['고령자'] / pop['인구수'] * 100

        cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'], 1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on='구별')
        cctv_pop.set_index('구별', inplace=True)

        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])

        print('고령자비율 과 CCTV 상관계수 {} \n 외국인비율 과 CCTV 상관계수 {}'.format(cor1, cor2))

        """
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계

        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]] 
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]
        """

        cctv_pop.to_csv(self.dr.context + 'saved/cctv_pop.csv')
