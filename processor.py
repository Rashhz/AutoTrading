import pandas as pd
import sqlite3
from scanner import *


class DataProcessor:
    def __init__(self, raw_data, db_name):
        self.data = raw_data
        self.db_name = db_name

    def clean_data(self):
        # 清洗数据，处理缺失值、异常值、重复值等
        self.data = self.data.dropna()  # 删除缺失值
        self.data = self.data.drop_duplicates()  # 删除重复
        return self.data

    def caculateMA(self, period=20):  # 计算MA
        self.data['MA' + str(period)] = self.data['closePrice'].rolling(window=period).mean()
        return self.data

    def calculate_bollinger_bands(self, data, window=20, std_multiplier=2):
        # 计算中轨（简单移动平均线）
        self.data['MB'] = self.data['closePrice'].rolling(window=window).mean()
        # 计算标准差
        self.data['STD'] = self.data['closePrice'].rolling(window=window).std(ddof=1)
        # 计算上轨和下轨
        self.data['UP'] = self.data['MB'] + std_multiplier * self.data['STD']
        self.data['DN'] = self.data['MB'] - std_multiplier * self.data['STD']
        return self.data

    def store_data_to_database(self, processed_data, table_name):
        # 将处理后的数据存储到数据库中
        conn = sqlite3.connect(self.db_name)
        processed_data.to_sql(table_name, conn, if_exists='replace', index=True)
        conn.close()


sc = Scanner()
df = sc.get_data_from_binance()
dp = DataProcessor(df,'noname')
dp.clean_data()
pd.set_option('display.max_columns', None)
dp.caculateMA()
print(dp.data['MA20'])