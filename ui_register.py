# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerMehjGQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(586, 384)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.email_entry = QLineEdit(self.centralwidget)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setGeometry(QRect(180, 150, 231, 21))
        self.email_entry.setStyleSheet(u"border-radius: 7px;\n"
"border: 0.5px solid black;\n"
"padding-left: 5px;")
        self.register_btn = QPushButton(self.centralwidget)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(260, 260, 75, 23))
        self.register_btn.setStyleSheet(u"border-radius: 7px;\n"
"border: 0.5px solid black;\n"
"padding-left: 5px;")
        self.login_lbl = QLabel(self.centralwidget)
        self.login_lbl.setObjectName(u"login_lbl")
        self.login_lbl.setGeometry(QRect(240, 30, 121, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(48)
        self.login_lbl.setFont(font)
        self.pass_entry = QLineEdit(self.centralwidget)
        self.pass_entry.setObjectName(u"pass_entry")
        self.pass_entry.setGeometry(QRect(180, 180, 231, 21))
        self.pass_entry.setStyleSheet(u"border-radius: 7px;\n"
"border: 0.5px solid black;\n"
"padding-left: 5px;")
        self.pass_entry.setEchoMode(QLineEdit.Password)
        self.name_entry = QLineEdit(self.centralwidget)
        self.name_entry.setObjectName(u"name_entry")
        self.name_entry.setGeometry(QRect(180, 120, 231, 21))
        self.name_entry.setStyleSheet(u"border-radius: 7px;\n"
"border: 0.5px solid black;\n"
"padding-left: 5px;")
        self.username_entry = QLineEdit(self.centralwidget)
        self.username_entry.setObjectName(u"username_entry")
        self.username_entry.setGeometry(QRect(180, 90, 231, 21))
        self.username_entry.setStyleSheet(u"border-radius: 7px;\n"
"border: 0.5px solid black;\n"
"padding-left: 5px;")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(200, 230, 181, 17))
        self.checkBox.setStyleSheet(u"")
        self.loginTransfer = QPushButton(self.centralwidget)
        self.loginTransfer.setObjectName(u"loginTransfer")
        self.loginTransfer.setGeometry(QRect(220, 300, 171, 23))
        self.loginTransfer.setStyleSheet(u"background-color: #f0f0f0;\n"
"border: 0px transparent white;\n"
"color: rgb(3, 83, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 586, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.email_entry.setText("")
        self.email_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.login_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">REGISTER</span></p><p><br/></p></body></html>", None))
        self.pass_entry.setText("")
        self.pass_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.name_entry.setText("")
        self.name_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.username_entry.setText("")
        self.username_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"I accept the terms and conditions", None))
        self.loginTransfer.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
    # retranslateUi

