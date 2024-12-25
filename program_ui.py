# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 773)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabScanner = QWidget()
        self.tabScanner.setObjectName(u"tabScanner")
        self.line = QFrame(self.tabScanner)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 190, 901, 41))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.tabScanner)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 210, 53, 15))
        self.horizontalLayoutWidget = QWidget(self.tabScanner)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 240, 831, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMidLineWidth(0)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.dateEdit = QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumDateTime(QDateTime(QDate(2021, 9, 5), QTime(16, 0, 0)))

        self.horizontalLayout_3.addWidget(self.dateEdit)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)

        self.dateEdit_2 = QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setDateTime(QDateTime(QDate(2024, 1, 5), QTime(16, 0, 0)))
        self.dateEdit_2.setMinimumDateTime(QDateTime(QDate(2021, 9, 5), QTime(16, 0, 0)))

        self.horizontalLayout_3.addWidget(self.dateEdit_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.layoutWidget = QWidget(self.tabScanner)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 70, 731, 141))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9, 0, Qt.AlignRight)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.verticalLayoutWidget = QWidget(self.tabScanner)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 310, 831, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.tabScanner)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 20, 121, 31))
        self.tabWidget.addTab(self.tabScanner, "")
        self.tabStragegy = QWidget()
        self.tabStragegy.setObjectName(u"tabStragegy")
        self.line_2 = QFrame(self.tabStragegy)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 180, 911, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_14 = QLabel(self.tabStragegy)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(390, 30, 53, 15))
        self.comboBox_3 = QComboBox(self.tabStragegy)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(190, 100, 171, 22))
        self.pushButton_5 = QPushButton(self.tabStragegy)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(500, 100, 75, 23))
        self.label_15 = QLabel(self.tabStragegy)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(380, 220, 91, 16))
        self.layoutWidget1 = QWidget(self.tabStragegy)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(130, 280, 281, 281))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_2.addWidget(self.label_18)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_2.addWidget(self.label_19)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_21 = QLabel(self.layoutWidget1)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_2.addWidget(self.label_21)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_2.addWidget(self.label_20)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_2.addWidget(self.label_22)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_2.addWidget(self.label_23)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_2.addWidget(self.label_24)

        self.tabWidget.addTab(self.tabStragegy, "")
        self.tagTrade = QWidget()
        self.tagTrade.setObjectName(u"tagTrade")
        self.label_10 = QLabel(self.tagTrade)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(370, 80, 91, 16))
        self.comboBox_2 = QComboBox(self.tagTrade)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(80, 70, 101, 22))
        self.label_6 = QLabel(self.tagTrade)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 46, 81, 20))
        self.formLayoutWidget = QWidget(self.tagTrade)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(490, 170, 211, 51))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.formLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_6)

        self.pushButton_2 = QPushButton(self.tagTrade)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 280, 75, 23))
        self.pushButton_4 = QPushButton(self.tagTrade)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(560, 280, 75, 23))
        self.textEdit = QTextEdit(self.tagTrade)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(160, 320, 531, 321))
        self.layoutWidget2 = QWidget(self.tagTrade)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(160, 170, 191, 54))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.lineEdit_3 = QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.lineEdit_4 = QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.pushButton_6 = QPushButton(self.tagTrade)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(380, 660, 75, 23))
        self.widget = QWidget(self.tagTrade)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(740, 450, 82, 54))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_5.addWidget(self.pushButton_9)

        self.tabWidget.addTab(self.tagTrade, "")
        self.tabOther = QWidget()
        self.tabOther.setObjectName(u"tabOther")
        self.label_7 = QLabel(self.tabOther)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 20, 71, 31))
        self.lineEdit = QLineEdit(self.tabOther)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 100, 161, 21))
        self.lineEdit_2 = QLineEdit(self.tabOther)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 160, 161, 21))
        self.label_11 = QLabel(self.tabOther)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 100, 53, 15))
        self.label_13 = QLabel(self.tabOther)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 160, 53, 15))
        self.pushButton_3 = QPushButton(self.tabOther)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(340, 120, 75, 23))
        self.line_3 = QFrame(self.tabOther)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 200, 861, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_25 = QLabel(self.tabOther)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(60, 260, 141, 16))
        self.lineEdit_7 = QLineEdit(self.tabOther)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(140, 310, 113, 21))
        self.lineEdit_8 = QLineEdit(self.tabOther)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(140, 370, 113, 21))
        self.lineEdit_9 = QLineEdit(self.tabOther)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(140, 430, 113, 21))
        self.pushButton_7 = QPushButton(self.tabOther)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(330, 360, 75, 23))
        self.label_26 = QLabel(self.tabOther)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(50, 310, 53, 15))
        self.label_27 = QLabel(self.tabOther)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 370, 71, 16))
        self.label_28 = QLabel(self.tabOther)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(40, 430, 61, 16))
        self.line_4 = QFrame(self.tabOther)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 540, 861, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.tabOther)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(422, 210, 21, 331))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.tabWidget.addTab(self.tabOther, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u884c\u60c5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u59cb\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u622a\u6b62\u65e5\u671f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u884c\u60c5", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5e01\u79cd", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"BTC/USDT", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ETH/USDT", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u884c\u60c5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScanner), QCoreApplication.translate("MainWindow", u"\u884c\u60c5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u9009\u62e9", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"turtle", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"ma", None))

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u56de\u6d4b", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u56de\u6d4b\u7ed3\u679c", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u521d\u671f\u4f59\u989d", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5269\u4f59\u4f59\u989d", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u603b\u6536\u76ca", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u76c8\u5229\u7387", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u56de\u6d4b\u5468\u671f\u957f\u5ea6", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5747\u76c8\u5229\u7387", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5747\u5e74\u5316\u76c8\u5229\u7387", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStragegy), QCoreApplication.translate("MainWindow", u"\u7b56\u7565", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u76d8\u4ea4\u6613", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"BTC/USDT", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"ETH/USDT", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4ea4\u6613\u5bf9", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5356\u51fa\u4ef7\u683c", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5356\u51fa\u91d1\u989d", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e70\u5165", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5356\u51fa", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4e70\u5165\u4ef7\u683c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u4e70\u5165\u91d1\u989d", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u5f53\u524d\u8ba2\u5355", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500\u6240\u6709\u8ba2\u5355", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tagTrade), QCoreApplication.translate("MainWindow", u"\u4ea4\u6613", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"http://127.0.0.1:7897", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://127.0.0.1:7897", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"http\u4ee3\u7406", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"https\u4ee3\u7406", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"okx\u4ea4\u6613\u6240api\u8bbe\u7f6e", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"apiKey", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"secretKey", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOther), QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
    # retranslateUi

