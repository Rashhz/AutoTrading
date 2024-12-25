# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(458, 338)
        self.tabWidget = QTabWidget(login)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, 9, 441, 321))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayoutWidget = QWidget(self.tab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 70, 321, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 190, 75, 23))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayoutWidget_3 = QWidget(self.tab_2)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(60, 60, 321, 61))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_6)

        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(170, 180, 75, 23))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(login)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.label.setText(QCoreApplication.translate("login", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("login", u"\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("login", u"\u767b\u5f55", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("login", u"\u767b\u5f55", None))
        self.label_5.setText(QCoreApplication.translate("login", u"\u7528\u6237\u540d", None))
        self.label_6.setText(QCoreApplication.translate("login", u"\u5bc6\u7801", None))
        self.pushButton_3.setText(QCoreApplication.translate("login", u"\u6ce8\u518c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("login", u"\u6ce8\u518c", None))
    # retranslateUi

