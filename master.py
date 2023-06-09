# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'master.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from edit import *

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(685, 236)
        mainWindow.setMinimumSize(QtCore.QSize(685, 236))
        mainWindow.setMaximumSize(QtCore.QSize(685, 236))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        mainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/Microsoft-Word-02-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("QWidget{background:white}\n"
"QLineEdit{background:transparent;border:1px solid #B4B5B5;padding: 5px 0px 5px 5px}\n"
"QLineEdit:hover{border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 51, 119, 255), stop:1 rgba(0, 182, 238, 255))}\n"
"QPushButton{color:black;padding:5px;font-weight:bold;border:1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 51, 119, 255), stop:1 rgba(0, 182, 238, 255))}\n"
"QPushButton:hover{color:white;border:0;background:#003377}\n"
"QProgressBar::chunk{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 51, 119, 255), stop:1 rgba(0, 182, 238, 255));font-weight:bold}")
        mainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushBtn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_1.setGeometry(QtCore.QRect(590, 40, 70, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushBtn_1.setFont(font)
        self.pushBtn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushBtn_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushBtn_1.setAutoFillBackground(False)
        self.pushBtn_1.setStyleSheet("")
        self.pushBtn_1.setObjectName("pushBtn_1")
        # self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1 = MyLindEdit("", self)
        self.lineEdit_1.setGeometry(QtCore.QRect(210, 40, 360, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAcceptDrops(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        # self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2 = MyLindEdit("", self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 90, 360, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_2.setGeometry(QtCore.QRect(590, 90, 70, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushBtn_2.setFont(font)
        self.pushBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushBtn_2.setObjectName("pushBtn_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 171, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_3.setGeometry(QtCore.QRect(350, 140, 220, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushBtn_3.setFont(font)
        self.pushBtn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushBtn_3.setObjectName("pushBtn_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 101, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 140, 101, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(-10, 210, 711, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.pushBtn_1.clicked.connect(mainWindow.get_dir)
        self.pushBtn_2.clicked.connect(mainWindow.get_xlsx)
        self.pushBtn_3.clicked.connect(mainWindow.run)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "报告生成工具 V4.0"))
        self.pushBtn_1.setText(_translate("mainWindow", "浏览"))
        self.pushBtn_2.setText(_translate("mainWindow", "选择"))
        self.label.setText(_translate("mainWindow", "模板文件夹(.docx):"))
        self.label_2.setText(_translate("mainWindow", "车辆信息表(.xlsx):"))
        self.pushBtn_3.setText(_translate("mainWindow", "开      始"))
        self.label_3.setText(_translate("mainWindow", "样车数量："))
import apprcc_rc
