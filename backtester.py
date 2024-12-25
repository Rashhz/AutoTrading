import pandas as pd
from account import *
from strategy import Strategy
from scanner import Scanner


class Backtester:
    def __init__(self, data,account):
        self.data = data  # 历史数据
        self.strategy = Strategy()
        self.symbol ='BTC/USDT'
        self.testAccount = account
    def run_turtle20(self):
        # 初始化账户
        # 开始模拟交易
        #产生交易信号
        self.data = self.strategy.turtle_breakout_strategy(self.data)
        for index, row in self.data.iterrows():
            if abs(self.data['Signal']) <= row['highPrice'] and abs(self.data['Signal'])>= row['lowPrice'] and self.data['Signal'] > 0:
                self.testAccount.buy(0.01, self.data['Signal'],self.symbol)  # 买入0.01个
                print(f'以{str(self.data['Signal'])}买入')
            elif abs(self.data['Signal']) <= row['highPrice'] and abs(self.data['Signal'])>= row['lowPrice'] and self.data['Signal'] < 0:
                self.testAccount.sell(0.01, abs(self.data['Signal']),self.symbol)  # 卖出0.01个
                print(f'以{str(self.data['Signal'])}卖出')
            elif self.data['Signal'] == 0:
                print('等待买入机会')
        if self.testAccount.
        self.testAccount
        return self.testAccount



if __name__ == '__main__':
    sc = Scanner()
    account = Account()
    bt = Backtester()