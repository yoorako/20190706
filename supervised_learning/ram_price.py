import mglearn

import pandas as pd

import os

import matplotlib.pyplot as plt

import numpy as np

from sklearn.tree import DecisionTreeRegressor

from sklearn.linear_model import LinearRegression



class RamPrice:

    def __init__(self):

        pass



    def hook(self):

        self.execute()



    def execute(self):

        ram_price = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH,'ram_price.csv'))

        plt.semilogy(ram_price.date, ram_price.price)

        plt.xlabel('년')

        plt.ylabel('가격')



        plt.show()



        data_train = ram_price[ram_price['date'] < 2000]

        data_test = ram_price[ram_price['date'] >= 2000]



        x_train = data_train['date'][:,np.newaxis] # train data 를 1열로 만들다

        y_train = np.log(data_train['price'])

        tree = DecisionTreeRegressor().fit(x_train,y_train)

        lr = LinearRegression().fit(x_train,y_train)



        x_all = ram_price['date'].values.reshape(-1, 1) # x_all 을 1열로 만듦

        pred_tree = tree.predict(x_all)

        price_tree = np.exp(pred_tree) # log 값 되돌리기

        pred_lr = lr.predict(x_all)

        price_lr = np.exp(pred_lr) # log 값 되돌리기

        plt.semilogy(ram_price['date'], pred_tree, label='tree predict', ls='-', dashes=(2,1))

        plt.semilogy(data_train['date'], data_train['price'], label='train data', alpha = 0.4)

        plt.semilogy(data_test['date'], data_test['price'], label='test data')

        plt.legend(loc = 1)

        plt.xlabel('year', size = 15)

        plt.ylabel('price', size = 15)

        plt.show()