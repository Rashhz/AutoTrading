import sqlite3
import ccxt
import pandas as pd
import pandas.errors
from matplotlib import dates as mdates, pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime


class Scanner:
    def __init__(self):
        self.symbol = 'BTC/USDT'
        self.con = sqlite3.connect('mydb.db')
        self.cycle = '1d'
        self.http = 'http://127.0.0.1:7897'
        self.https = 'http://127.0.0.1:7897'
        self.dict = {
            'proxies': {
                'http': '',
                'https': ''
            }}
        self.dict['proxies']['http'] = self.http
        self.dict['proxies']['https'] = self.https
        self.exchange = ccxt.binance(self.dict)

    def get_data_from_binance(self, cycle, symbol):
        data = self.exchange.fetch_ohlcv(symbol, cycle, limit=1000)  # 默认获取BTC/USDT的日K线数据
        df = pd.DataFrame(data)
        df = df.rename(
            columns={0: 'dateTime', 1: 'openPrice', 2: 'highPrice', 3: 'lowPrice', 4: 'closePrice', 5: 'Volume'})
        df['dateTime'] = pd.to_datetime(df['dateTime'], unit='ms')
        symboldrop = self.symbol.replace("/", "")
        df.to_sql(f'{symboldrop}_{cycle}_data', con=self.con, if_exists='replace')
        return df

    def load_data(self, start_date, end_date):
        symboldrop = self.symbol.replace("/", "")
        now_date = datetime.now().date()
        if pd.to_datetime(start_date) >= pd.to_datetime('2021-07-01') and pd.to_datetime(end_date) <= pd.to_datetime(
                now_date):  # 只允许查询2021年以后的，api限制
            try:
                sqltest1 = f"SELECT * from {symboldrop}_{self.cycle}_data WHERE DATE(dateTime)='{end_date}'"
                dft1 = pd.read_sql(sqltest1, con=self.con)
                sqltest2 = f"SELECT * from {symboldrop}_{self.cycle}_data WHERE DATE(dateTime)='{start_date}'"
                dft2 = pd.read_sql(sqltest2, con=self.con)
                if dft1.empty == False and dft2.empty == False:
                    sqlword = f"SELECT * from {symboldrop}_{self.cycle}_data WHERE dateTime BETWEEN '{start_date}' AND '{end_date}'"
                    df = pd.read_sql(sqlword, con=self.con)
                    return df
                else:
                    df = self.get_data_from_binance(self.cycle, self.symbol)
                    return df
            except pandas.errors.DatabaseError:
                df = self.get_data_from_binance(self.cycle, self.symbol)
                return df
        else:
            return pd.DataFrame()

    def printGraph(self, start_date, end_date):
        data = self.load_data(start_date, end_date)
        if data.empty == False:
            data['dateTime'] = pd.to_datetime(data['dateTime'])
            data = data.loc[(data['dateTime'] >= start_date) & (data['dateTime'] <= end_date)]
            # data = data.drop('Volume', axis=1)
            # 将 datetime 对象转换为 matplotlib 的日期格式
            data['dateTime'] = mdates.date2num(data['dateTime'])
            # 将数据转换为二维数组
            ohlc = data[['dateTime', 'openPrice', 'highPrice', 'lowPrice', 'closePrice']].values
            # 创建图表和坐标轴
            fig, axes = plt.subplots()
            # 绘制 K 线图
            candlestick_ohlc(axes, ohlc, width=0.6, colorup='g', colordown='r')
            # 将横坐标转换为 datetime
            axes.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            plt.xticks(rotation=15)
            plt.title = 'Kline'
            plt.xlabel('Date')
            plt.ylabel('Price/USD')
            plt.grid(True)
            return fig, axes
        else:
            return 0, 0

    def printGraph2(self):
        try:
            data = pd.DataFrame(self.exchange.fetch_ohlcv(self.symbol, '1m', limit=50))
        except ccxt.errors.NetworkError:
            return 0, 0
        if data.empty == False:
            data = data.rename(
                columns={0: 'dateTime', 1: 'openPrice', 2: 'highPrice', 3: 'lowPrice', 4: 'closePrice', 5: 'Volume'})
            data['dateTime'] = pd.to_datetime(data['dateTime'])
            data = data.tail(40)
            data = data.drop('Volume', axis=1)
            # 将 datetime 对象转换为 matplotlib 的日期格式
            data['dateTime'] = mdates.date2num(data['dateTime'])
            # 将数据转换为二维数组
            ohlc = data[['dateTime', 'openPrice', 'highPrice', 'lowPrice', 'closePrice']].values
            # 创建图表和坐标轴
            fig, axes = plt.subplots()
            # 绘制 K 线图
            candlestick_ohlc(axes, ohlc, width=0.6, colorup='g', colordown='r')
            # 将横坐标转换为 datetime
            axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            plt.xticks(rotation=15)
            plt.title = 'Kline'
            plt.xlabel('Date')
            plt.ylabel('Price/USD')
            plt.grid(True)
            return fig, axes
        else:
            return 0, 0


if __name__ == '__main__':
    sc = Scanner()
    data = sc.load_data('2023-06-01', '2024-01-02')
    print(data)
