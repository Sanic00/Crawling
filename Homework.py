import logtest as log
import sys

args = sys.argv

print(args[0])
print(args[1])
print(args[2])

code = args[1]
date = args[2]

import requests
url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
res = requests.get(url, headers = {'User-Agent':'Mozilla/5.0'})
res.status_code

from bs4 import BeautifulSoup
soap = BeautifulSoup(res.text, 'lxml')

el_table_navi = soap.find("table", class_="Nnavi")
el_td_last = el_table_navi.find("td", class_="pgRR")
pg_last = el_td_last.a.get('href').rsplit('&')[1]
pg_last = pg_last.split('=')[1]
pg_last = int(pg_last)

import Panda1
import pandas as pd



import datetime
try:
    str_datefrom = datetime.datetime.strftime(datetime.datetime(year=int(date[0:4]), month=int(date[5:7]), day=int(date[8:10])), '%Y.%m.%d')
except Exception as e:
    log.logging.warning("!!!!!!!!!!!!!!문자를 잘못 입력하였습니다.!!!!!!!!!!!!!!")

str_dateto = datetime.datetime.strftime(datetime.datetime.today(), '%Y.%m.%d')
print(type(str_datefrom))
df = None
for page in range(1, pg_last+1):
    _df = Panda1.parse_page(code, page)
    _df_filtered = _df[_df['날짜'] > str_datefrom]
    if df is None:
        df = _df_filtered
    else:
        df = pd.concat([df, _df_filtered])
    if len(_df) > len(_df_filtered):
        break

df.tail()
print(df)

df.to_csv('주가1.csv')

import os
path_dir = 'data/2018-07-05-crawling'
if not os.path.exists(path_dir):
    os.makedirs(path_dir)
path = os.path.join(path_dir, '{code}_{date_from}_{date_to}.csv'.format(code=code, date_from=str_datefrom, date_to=str_dateto))

df.to_csv(path, index=False)

df.rename(columns={'날짜':'Date'},inplace=True)
df.rename(columns={'종가':'End'},inplace=True)
df.rename(columns={'거래량':'volume'},inplace=True)

df.to_csv('주가.csv')

import Graph as ga
ga.graph_painting()

import matplotlib.pyplot as plt


# plt.subplot(2, 1, 1)
# plt.plot(df.Date, df.volume,'#4DD0E1')
# plt.xlabel('date')
# plt.ylabel('volume')
# plt.title('SAMSUNG')
#
#
# plt.subplot(2, 1, 2)
# plt.plot(df.Date, df.End,'#4DD0E1')
# plt.xlabel('date')
# plt.ylabel('price')
# plt.title('SAMSUNG')
#
# plt.tight_layout()
# plt.show()



