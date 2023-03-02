import os
import Homework as hw

def Csv():
    path_dir = 'data/2018-07-05-crawling'
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    path = os.path.join(path_dir, '{code}_{date_from}_{date_to}.csv'.format(code=code, date_from=str_datefrom, date_to=str_dateto))

    hw.df.to_csv(path, index=False)

    hw.df.rename(columns={'날짜':'Date'},inplace=True)
    hw.df.rename(columns={'종가':'End'},inplace=True)
    hw.df.rename(columns={'거래량':'volume'},inplace=True)

    hw.df.to_csv('주가.csv')