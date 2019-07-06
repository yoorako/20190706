from cctv.data_reader import DataReader
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

class PoliceChart:
    def __init__(self):
        self.dr = DataReader()

    def hook(self):
        police_norm = self.create_police_norm()
        # self.show_sns(police_norm)
        self.show_heatmap(police_norm)

    def create_police_norm(self):
        self.dr.context = './data/'
        self.dr.fname = 'saved/police_norm.csv'
        police_norm = self.dr.csv_to_dframe()
        # print(police_norm)
        return police_norm

    def show_sns(self, pn):
        font = 'C:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=font).get_name()
        print('폰트명 %s :' % (font_name))
        rc('font', family=font_name)
        sns.pairplot(pn, vars=['강도','살인','폭력'],kind='reg', height=3)
        sns.pairplot(pn, x_vars=['인구수','CCTV'], y_vars=['살인','강도'], kind='reg', height=3)
        tmp_max = pn['검거'].max()
        pn['검거'] = pn['검거'] / tmp_max * 100
        plt.figure(figsize=(10,10))
        plt.show()

    def show_heatmap(self, pn):
        font = 'C:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=font).get_name()
        rc('font', family=font_name)
        pn_sort = pn.sort_values(by='검거', ascending=False)
        crime_rate_columns = ["살인검거율", "강도검거율", "강간검거율", "절도검거율", "폭력검거율"]
        sns.heatmap(pn_sort[crime_rate_columns], annot=True, fmt='f', linewidths=5)
        plt.title('범죄 검거 비율')
        # plt.show()

        crime_columns = ["살인", "강도", "강간", "절도", "폭력"]
        pn['범죄'] = pn['범죄'] / 5
        pn_sort = pn.sort_values(by='범죄', ascending=False)
        plt.figure(figsize=(10,10))
        sns.heatmap(pn_sort[crime_columns], annot=True, fmt='f', linewidths=5)
        plt.title('범죄 비율')
        plt.show()

