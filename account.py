import ccxt
from strategy import Strategy
from scanner import Scanner


class Account:
    def __init__(self, type=0, initial_balance=10000):
        # 0为模拟账户，1为实盘账户
        self.type = type
        self.http = 'http://127.0.0.1:7897'
        self.https = 'http://127.0.0.1:7897'
        self.apikey = 'api'
        self.secretkey = 'sk'
        self.password = 'Abc123456!'
        self.dict = {
            'proxies': {
                'http': self.http,
                'https': self.https
            },
            'apiKey': self.apikey,
            'secret': self.secretkey,
            'password': self.password
        }
        self.okx_m = ccxt.okx(self.dict)
        self.okx_m.set_sandbox_mode(True)
        self.initialBalance = initial_balance
        self.currentBalance = initial_balance
        self.targetBalance = 0

    def buy(self, amount, makerPrice, symbol):  # 金额
        if self.type == 0:
            self.targetBalance += amount
            self.currentBalance -= amount * makerPrice
        if self.type == 1:
            try:
                res = self.okx_m.create_order(symbol=symbol, type='limit', side='buy', amount=amount,
                                              price=makerPrice)
                symbol = symbol.replace('/USDT', '')
                self.targetBalance = self.okx_m.fetch_balance()[symbol]
                self.currentBalance = self.okx_m.fetch_balance()['USDT']
                return res
            except ccxt.errors.NetworkError:
                return 'NetworkError'

    def sell(self, amount, makerPrice, symbol):
        if self.type == 0:
            self.targetBalance -= amount
            self.currentBalance += amount * makerPrice
        if self.type == 1:
            try:
                res = self.okx_m.create_order(symbol=symbol, type='limit', side='sell', amount=amount,
                                              price=makerPrice)
                symbol = symbol.replace('/USDT', '')
                self.targetBalance = self.okx_m.fetch_balance()[symbol]
                self.currentBalance = self.okx_m.fetch_balance()['USDT']
                return res
            except ccxt.errors.NetworkError:
                return 'NetworkError'

    def reset(self, initial_balance=10000):
        self.balance = initial_balance
        self.targetBalance = 0


class Backtester:
    def __init__(self, data):
        self.data = data  # 历史数据
        self.symbol = 'BTC/USDT'
        self.testAccount = Account(type=0)

    def run(self):
        # 初始化账户
        # 开始模拟交易
        # 产生交易信号
        # row = self.strategy.turtle_breakout_strategy(row)
        for index, row in self.data.tail(180).iterrows():
            if abs(row['Signal']) <= row['highPrice'] and abs(row['Signal']) >= row['lowPrice'] and row['Signal'] > 0:
                if self.testAccount.currentBalance >= 0.01 * abs(row['Signal']):
                    self.testAccount.buy(0.01, abs(row['Signal']), self.symbol)  # 买入0.01个
                    print(f'以{str(row['Signal'])}买入')
                else:
                    print("余额不足")

            elif abs(row['Signal']) <= row['highPrice'] and abs(row['Signal']) >= row['lowPrice'] and row['Signal'] < 0:
                if self.testAccount.targetBalance >= 0.01:
                    self.testAccount.sell(0.01, abs(row['Signal']), self.symbol)  # 卖出0.01个
                    print(f'以{str(row['Signal'])}卖出')
                else:
                    print('仓位不足')
            elif row['Signal'] == 0:
                print('等待买入机会')
        if self.testAccount.targetBalance != 0:
            self.testAccount.sell(self.testAccount.targetBalance, self.data.iloc[-1]['closePrice'], self.symbol)
            print('卖出所有仓位')
        return self.testAccount


if __name__ == '__main__':
    account = Account(type=1)
    res = account.buy(0.01, 60000, 'BTC/USDT')
    print(res)
