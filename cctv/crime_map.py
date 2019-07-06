from cctv.data_reader import DataReader
import folium
import numpy as np
class CrimeMap:
    def __init__(self):
        self.dr = DataReader()

    def hook(self):
        # self.seoul_crime_map()
        self.create_map()

    def create_seoul_crime_map(self):
        print('---------1 ---------')
        self.dr.context = './data/'
        self.dr.fname = 'saved/police_norm.csv'
        pn = self.dr.csv_to_dframe()
        print(pn)
        self.dr.fname = 'geo_simple.json'
        geo_str = self.dr.json_load()
        map = folium.Map(location=[37.5502, 126.982],
                         zoom_start=12,
                         tiles='Stamen Toner')
        map.choropleth(
            geo_data=geo_str,
            name='choropleth',
            data=tuple(zip(pn['구별'], pn['범죄'])),
            key_on='feature.id',
            fill_color='PuRd'
        )
        map.save(self.dr.context+'saved/seoul_crime_map.html')

    def create_map(self):
        print('-----------')
        self.dr.context = './data/'
        self.dr.fname = 'saved/police_norm.csv'
        pn = self.dr.csv_to_dframe()
        self.dr.fname = 'crime_in_Seoul.csv'
        crime = self.dr.csv_to_dframe()
        # print(crime)
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울' + str(name[:-1]) + '경찰서')
        station_addrs = []
        station_lats = []  # 위도
        station_lngs = []  # 경도
        gmaps = self.dr.create_gmaps()
        for name in station_names:
            tmp = gmaps.geocode(name, language='ko')
            station_addrs.append(tmp[0].get('formatted_address'))
            tmp_loc = tmp[0].get('geometry')
            station_lats.append(tmp_loc['location']['lat'])
            station_lngs.append(tmp_loc['location']['lng'])
            print(name + '---> '+tmp[0].get('formatted_address'))
        self.dr.fname = 'police_position.csv'
        police_pos = self.dr.csv_to_dframe()
        police_pos['lat'] = station_lats
        police_pos['lng'] = station_lngs
        print(police_pos.columns)
        col = ["살인 검거", "강도 검거", "강간 검거", "절도 검거", "폭력 검거"]
        tmp = police_pos[col] / police_pos[col].max()
        police_pos['검거'] = np.sum(tmp, axis=1)
        self.dr.fname = 'geo_simple.json'
        geo_str = self.dr.json_load()
        map = folium.Map(location=[37.5502, 126.982],
                         zoom_start=12,
                         tiles='Stamen Toner')
        map.choropleth(
            geo_data=geo_str,
            name='choropleth',
            data=tuple(zip(pn['구별'], pn['범죄'])),
            key_on='feature.id',
            fill_color='PuRd'
        )
        for i in police_pos.index:
            folium.CircleMarker([police_pos['lat'][i], police_pos['lng'][i]],
                                radius=police_pos['검거'][i] * 10,
                                color = '#0a0a32',
                                fill_color = '#0a0a32').add_to(map)
        map.save(self.dr.context+'saved/seoul_police_map.html')