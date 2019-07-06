from cctv.data_reader import DataReader


class CrimeModel:
    def __init__(self):
        self.dr = DataReader()

    def hook(self) -> object:
        self.create_crime_police()

    def create_crime_police(self):
        self.dr.context = './data/'
        self.dr.fname = 'crime_in_Seoul.csv'
        crime = self.dr.csv_to_dframe()
        # print(crime)
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울'+str(name[:-1])+'경찰서')
        station_addrs = []
        station_lats = [] # 위도
        station_lngs= [] # 경도
        gmaps = self.dr.create_gmaps()
        for name in station_names:
            tmp = gmaps.geocode(name, language='ko')
            station_addrs.append(tmp[0].get('formatted_address'))
            tmp_loc = tmp[0].get('geometry')
            station_lats.append(tmp_loc['location']['lat'])
            station_lngs.append(tmp_loc['location']['lng'])
            # print(name + '---> '+tmp[0].get('formatted_address'))
        gu_names = []
        for name in station_addrs:
            tmp = name.split()
            gu_name = [gu for gu in tmp if gu[-1] == '구'][0]
            gu_names.append(gu_name)

        crime['구별'] = gu_names

        # 만약에 구와 경찰서 위치가 다른 경우 수작업이 필요합니다.
        crime.loc[crime['관서명']=='혜화서',['구별']] == '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] == '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] == '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] == '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] == '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] == '강남구'

        # print(crime)

        crime.to_csv(self.dr.context+'saved/crime_police.csv')
