from cctv.data_reader import DataReader
import pandas as pd
import numpy as np
from sklean import preprocessing#전처리하는 라이브러리

class CrimeRateModel:

    def __init__(self):

        self.dr = DataReader()



    def hook(self):

        self.create_crime_rate()



    def create_crime_rate(self):

        self.dr.context = './data/'

        self.dr.fname = 'saved/crime_police.csv'

        police_crime = self.dr.csv_to_dframe()



        print('---------- pivotal 전 ------------------')

        print(police_crime.columns)

        """

        Index(['Unnamed: 0', '관서명', '살인 발생', '살인 검거',

         '강도 발생', '강도 검거', '강간 발생',

       '강간 검거', '절도 발생', '절도 검거', '폭력 발생',

        '폭력 검거', '구별'],

      dtype='object')

        """

        police = pd.pivot_table(police_crime, index='구별', aggfunc=np.sum)

        print('---------- pivotal 후 ------------------')

        print(police.columns)

        print(police)

        """

        Index(['Unnamed: 0', '강간 검거', '강간 발생', '강도 검거',

         '강도 발생', '살인 검거', '살인 발생'], dtype='object')

        """

        arrest_crime_1 = pd.to_numeric(police['살인 검거'])

        occurr_crime_1 = pd.to_numeric(police['살인 발생'])



        print('살인 검거 출력: %s'% (arrest_crime_1))

        print('살인 발생 출력: %s'% (occurr_crime_1))

        police['살인검거율'] = (arrest_crime_1 / occurr_crime_1) * 100

        print('살인검거율 출력: %s'% (police['살인검거율']))

        arrest_crime_2 = pd.to_numeric(police['강도 검거'])

        occurr_crime_2 = pd.to_numeric(police['강도 발생'])

        police['강도검거율'] = (arrest_crime_2 / occurr_crime_2) * 100

        arrest_crime_3 = pd.to_numeric(police['강간 검거'])

        occurr_crime_3 = pd.to_numeric(police['강간 발생'])

        police['강간검거율'] = (arrest_crime_3 / occurr_crime_3) * 100

        print('강간검거율 출력: %s' % (police['강간검거율']))

        """

        print('--------->> 이슈 발생')

        print(police['절도 검거'])

        arrest_crime_4 = pd.to_numeric(police['절도 검거'])

        print(arrest_crime_4)

        occurr_crime_4 = pd.to_numeric(police['절도 발생'])

        print('절도 검거 출력: %s' % (arrest_crime_4))

        print('절도 발생 출력: %s' % (occurr_crime_4))

        police['절도검거율'] = (arrest_crime_4 / occurr_crime_4) * 100

        print('절도검거율 출력: %s' % (police['절도검거율']))

        arrest_crime_5 = pd.to_numeric(police['폭력 검거'])

        occurr_crime_5 = pd.to_numeric(police['폭력 발생'])

        police['폭력검거율'] = (arrest_crime_5 / occurr_crime_5) * 100

        """

        police.drop(columns={'살인 검거','강도 검거','강간 검거'}, axis=1)



        print(police)
        #검거율이 100%가 넘는 것은 오류를 발생시키므로 정리함
        police_columns = ["살인검거율","강도검거율","강간검거율","절도검거율","폭력검거율"]
        x = police[police_columns].values
        main_max_scalar = preprocessing.MinMaxScaler()
        """
        평균 = 0, 분산 = 1
        """
        x_scalar = min_max_scalar.fit_transform(x.astype(float))
        police_norm = pd.DataFrame(x_scalar, columns=police_columns, index=police.index)
        police_norm =[police_columns] = police[police_columns]
        #self.dr.context('./data/')
        #self.dr.fname('saved/cctv_pop.csv')
        #newfile = self.dr.new_file()
        cctv_pop = pd.read_csv('./data/saved/cctv_pop.csv',
                               encoding='UTF-8',
                               sep=',',
                               index_col='구별')

        police_norm[['인구수','CCTV']] = cctv_pop[['인구수','소계']] #소계는 CCTV 갯수
        police_norm['범죄'] = np.sum
        print(cctv_pop)
