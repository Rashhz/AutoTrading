import datetime
import sqlite3
import time
from threading import Thread
import matplotlib
import pandas as pd
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QMessageBox
from time import sleep
from matplotlib import pyplot as plt
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from program_ui import Ui_MainWindow
from account import *
from login import Ui_login

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class MySignals(QObject):
    # 定义一种信号，参数类型
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    update_price = Signal(str)  # label5的更新信号
    # 还可以定义其他种类的信号
    update_graph = Signal(matplotlib.figure.Figure, matplotlib.axes._axes.Axes)


# 实例化
global_ms = MySignals()


class FigureCanvasKline(FigureCanvas):
    def __init__(self, fig, axes):
        FigureCanvas.__init__(self, fig)
        self.axes = axes
        self.draw()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_login()
        # 初始化界面
        self.ui.setupUi(self)
        self.con = sqlite3.connect('mydb.db')
        self.ui.pushButton.clicked.connect(self.handleloginButton)
        self.ui.pushButton_3.clicked.connect(self.handleRegButton)

    def handleloginButton(self):
        userid = self.ui.lineEdit.text()
        passwd = self.ui.lineEdit_2.text()
        cur = self.con.cursor()
        try:
            cur.execute("SELECT password FROM user WHERE id = ?", (userid,))
            result = cur.fetchone()
        except sqlite3.OperationalError:
            cur.execute("CREATE TABLE user(id TEXT PRIMARY KEY, password TEXT)")
            cur.execute("SELECT password FROM user WHERE id = ?", (userid,))
            result = cur.fetchone()
        if result and result[0] == passwd:
            self.close()
            self.mainwindow = MainWindow()
            self.mainwindow.show()
        else:
            QMessageBox.warning(self, '登录失败', '密码错误或用户不存在')

    def handleRegButton(self):
        userid = self.ui.lineEdit_5.text()
        passwd = self.ui.lineEdit_6.text()
        sql = f"INSERT INTO user VALUES('{userid}', '{passwd}')"
        cur = self.con.cursor()
        try:
            cur.execute(sql)
            self.con.commit()
            QMessageBox.information(self, '注册成功', f'已成功注册，用户名为：{userid}')
        except sqlite3.OperationalError:
            cur.execute("CREATE TABLE user(id TEXT PRIMARY KEY, password TEXT)")
            cur.execute(sql)
            self.con.commit()
            QMessageBox.information(self, '注册成功', f'已成功注册，用户名为：{userid}')
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, '注册失败', '该用户已注册')
        return cur.lastrowid


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        self.signal = MySignals()
        # 初始化界面
        self.ui.setupUi(self)
        # 初始化几个基本类
        self.sc = Scanner()
        self.bc = Backtester(pd.DataFrame())
        self.stra = Strategy()
        self.account = Account(type=1)
        self.con = sqlite3.connect('mydb.db')
        # global_ms.update_price.connect()
        self.ui.comboBox.currentTextChanged.connect(self.handleComboBox)
        th1 = Thread(target=lambda: self.handleLabel_5(self.sc.symbol))  # 更新行情
        th1.start()
        # th2 = Thread(target=lambda:self.updateGraphThread())
        # th2.start()
        # 绑定
        self.ui.pushButton.clicked.connect(self.handlepushButton)
        self.ui.pushButton_3.clicked.connect(self.handlepushButton2)
        self.ui.pushButton_5.clicked.connect(self.handlepushButton5)
        self.ui.pushButton_2.clicked.connect(self.handlepushButton2)
        self.ui.pushButton_4.clicked.connect(self.handlepushButton4)
        self.ui.pushButton_6.clicked.connect(self.handlepushButton6)
        self.ui.pushButton_7.clicked.connect(self.handlePushButton7)
        self.ui.pushButton_8.clicked.connect(self.handlePushButton8)
        self.ui.pushButton_9.clicked.connect(self.handlePushButton9)
        global_ms.update_price.connect(self.mainWindowdealWithhandleLabel_5)
        # global_ms.update_graph.connect(self.updateGraph)

    def handlepushButton(self):
        layout = self.ui.verticalLayout
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()
        try:
            fig, axes = self.sc.printGraph(start_date=self.ui.dateEdit.text(), end_date=self.ui.dateEdit_2.text())
            axes.set_title('历史数据')
            layout.addWidget(FigureCanvasKline(fig, axes))
        except TypeError:
            pass

    def handlepushButton5(self):
        select = self.ui.comboBox_3.currentText()
        print(select)
        now = datetime.datetime.now()
        begin = now - datetime.timedelta(days=180)
        df = self.sc.load_data(begin.date(), now.date())
        if select == 'turtle':
            df = self.stra.turtle_breakout_strategy(df)
        elif select == 'ma':
            df = self.stra.doubleMA(df)
        self.bc.data = df
        result = self.bc.run()
        balance = str(round(result.currentBalance, 2))
        totaLearn = result.currentBalance - result.initialBalance
        totaLearn = str(round(totaLearn, 2))
        profitRate = str(round((result.currentBalance - result.initialBalance) / result.initialBalance * 100, 2))
        dailyProfitRate = str(
            round((result.currentBalance - result.initialBalance) / (result.initialBalance * 180) * 100, 2))
        dailyProfitRateByYear = str(
            round((result.currentBalance - result.initialBalance) / (result.initialBalance * 180) * 100 * 365, 2))
        self.ui.label_18.setText('初期余额: ' + str(result.initialBalance))
        self.ui.label_19.setText('剩余余额: ' + balance)
        self.ui.label_21.setText('总收益: ' + totaLearn)
        self.ui.label_20.setText('盈利率: ' + profitRate + '%')
        self.ui.label_22.setText('回测周期长度: ' + str(180))
        self.ui.label_23.setText('日均盈利率: ' + dailyProfitRate + '%')
        self.ui.label_24.setText('日均年化盈利率: ' + dailyProfitRateByYear + '%')

    def handlepushButton2(self):
        symbol = self.ui.comboBox_2.currentText()
        price = self.ui.lineEdit_3.text()
        amount = self.ui.lineEdit_4.text()
        res = self.account.buy(amount, price, symbol)
        if res:
            orderid = res['id']
            symbol = res['symbol']
            timestamp = res['info']['ts']
            side = res['side']
            if res['type'] == 'limit':
                type = 'limit'
            else:
                type = 'market'
        try:
            cur = self.con.cursor()
            cur.execute(f"INSERT INTO orders VALUES('{orderid}','{symbol}','{timestamp}','{amount}','{type}','{price}','{side}')")
        except sqlite3.OperationalError:
            cur = self.con.cursor()
            cur.execute("CREATE TABLE orders(id PRIMARY KEY, symbol, timestamp, amount, type, price,side)")
            cur.execute(f"INSERT INTO orders VALUES('{orderid}','{symbol}','{timestamp}','{amount}','{type}','{price}','{side}')")
        self.ui.textEdit.append(str(res))

    def handlepushButton4(self):
        symbol = self.ui.comboBox_2.currentText()
        price = self.ui.lineEdit_5.text()
        amount = self.ui.lineEdit_6.text()
        res = self.account.sell(amount, price, symbol)
        if res:
            orderid = res['id']
            symbol = res['symbol']
            timestamp = res['info']['ts']
            side = res['side']
            if res['type'] == 'limit':
                type = 'limit'
            else:
                type = 'market'
        try:
            cur = self.con.cursor()
            cur.execute(f"INSERT INTO orders VALUES('{orderid}','{symbol}','{timestamp}','{amount}','{type}','{price}','{side}')")
        except sqlite3.OperationalError:
            cur = self.con.cursor()
            cur.execute("CREATE TABLE orders(id PRIMARY KEY, symbol , timestamp, amount, type, price, side)")
            cur.execute(f"INSERT INTO orders VALUES('{orderid}','{symbol}','{timestamp}','{amount}','{type}','{price}','{side}')")
        self.ui.textEdit.append(str(res))
        print(res)
        self.ui.textEdit.append(str(res))

    def handleComboBox(self):
        self.sc.symbol = self.ui.comboBox.currentText()

    def handleLabel_5(self, symbol):
        while (1):
            try:
                symbol = self.sc.symbol
                rp = self.sc.exchange.fetch_last_prices()
                global_ms.update_price.emit(f'当前{symbol}的价格为：' + str(rp[symbol]['price']))
                sleep(1)
            except ccxt.errors.NetworkError:
                global_ms.update_price.emit('行情获取失败，网络错误')

    def handlepushButton3(self):
        self.sc.http = self.ui.lineEdit.text()
        self.sc.https = self.ui.lineEdit_2.text()

    def handlepushButton6(self):
        self.ui.textEdit.clear()

    def handlePushButton7(self):
        self.account.apikey = self.ui.lineEdit_7.text()
        self.account.secretkey = self.ui.lineEdit_8.text()
        self.account.password = self.ui.lineEdit_9.text()

    def mainWindowdealWithhandleLabel_5(self, str1):
        self.ui.label_5.setText(str1)
    def handlePushButton8(self):
        res = self.account.okx_m.fetch_open_orders()
        for order in res:
            instID = order['symbol']
            price = order['price']
            dtime = order['datetime']
            side = order['side']
            self.ui.textEdit.append(f'交易对:{instID}, 价格：{price}, 下单时间：{dtime}, 方向：{side}')

    def handlePushButton9(self):
        open_orders = self.account.okx_m.fetch_open_orders()
        for order in open_orders:
            try:
                self.ui.textEdit.append(f"取消订单: {order['id']}")
                self.account.okx_m.cancel_order(order['id'], order['symbol'])
                time.sleep(0.2)  # 避免超出速率限制
            except Exception as e:
                self.ui.textEdit.append(f"无法取消订单 {order['id']}: {str(e)}")
    # def updateGraph(self,fig,axes):
    #     while(1):
    #         layout = self.ui.verticalLayout_2
    #         for i in range(layout.count()):
    #             layout.itemAt(i).widget().deleteLater()
    #         fig = fig
    #         axes = axes
    #         layout.addWidget(FigureCanvasKline(fig, axes))
    def updateGraphThread(self):
        while (1):
            try:
                fig, axes = self.sc.printGraph2()
                if fig != 0 and axes != 0:
                    axes.set_title('历史数据')
                    global_ms.update_graph.emit(fig, axes)
            except ccxt.errors.NetworkError:
                pass

    # def handlepushiButton9(self):
    #     name = self.ui.lineEdit_11.text()
    #     type = self.ui.checkBox.isChecked()
    #     self.ui.comboBox_4.addItem(name)
    #     if type == 0:
    #         balance = 10000
    #         currency = 0
    #     elif type == 1:
    #         balance = 0
    #         currency = 0
    #     cur = self.con.cursor()
    #     try:
    #         cur.execute(f"INSERT INTO Taccount VALUES('{name}','{balance}','{currency}','{type}')")
    #     except sqlite3.OperationalError:
    #         cur.execute(
    #             "CREATE TABLE orders(name PRIMARY KEY, balance, currency , type , apikey , secretkey , password)")
    #         cur.execute(f"INSERT INTO Taccount VALUES('{name}','{balance}','{currency}','{type}')")




if __name__ == '__main__':
    date_str1 = '2023-10-19'
    date_str2 = '2024-2-12'
    datetime_obj1 = pd.to_datetime(date_str1)
    datetime_obj2 = pd.to_datetime(date_str2)
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()
