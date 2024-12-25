
import numpy as np
class Strategy:

    def turtle_breakout_strategy(self,df, n=20):
        """
        海龟突破策略
        :param df: 包含K线数据的DataFrame，至少包含'High'和'Low'列
        :param n: 突破周期
        :return: 交易信号，1表示买入，-1表示卖出
        """
        df['ATR'] = df['highPrice'] - df['lowPrice']
        df['ATR_MA'] = df['ATR'].rolling(window=n).mean()

        # 计算突破信号
        df['Long_Entry'] = df['closePrice'] > df['highPrice'].shift(1) + 1.5 * df['ATR_MA']
        df['Short_Entry'] = df['closePrice'] < df['lowPrice'].shift(1) - 1.5 * df['ATR_MA']

        # 生成交易信号
        df['Signal'] = 0
        df.loc[df['Long_Entry'], 'Signal'] = 1
        df.loc[df['Short_Entry'], 'Signal'] = -1
        df['Signal'] = df['Signal'] * df['closePrice']
        return df

    # signals = turtle_breakout_strategy(your_dataframe)
    def doubleMA(self,df):
        # 计算短期均线（如5日均线）和长期均线（如20日均线）
        short_window = 5
        long_window = 20
        df['Short_MA'] = df['closePrice'].rolling(window=short_window).mean()
        df['Long_MA'] = df['closePrice'].rolling(window=long_window).mean()
        # 生成交易信号
        df['Signal'] = 0
        df['Signal'] = np.where(df['Short_MA'] > df['Long_MA'], 1, -1)
        df['Signal'] = df['Signal'] * df['closePrice']
        return df


# if __name__ == '__main__':
#     sc = Scanner()
#     df = sc.load_data('2023-06-01','2024-01-02')
#     celue1 = Strategy()
#     df = celue1.turtle_breakout_strategy(df)
#     print(df)
#     print(df.loc[df['Signal'] != 0])
