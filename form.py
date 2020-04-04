# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 600)
        MainWindow.setStyleSheet("background:#0E1621;\n"
"color:#FDFDFB;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 201, 25))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 191, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 520, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, -90, 31, 1631))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionfirst = QtWidgets.QAction(MainWindow)
        self.actionfirst.setObjectName("actionfirst")
        self.actionsecond = QtWidgets.QAction(MainWindow)
        self.actionsecond.setObjectName("actionsecond")
        self.action111 = QtWidgets.QAction(MainWindow)
        self.action111.setObjectName("action111")
        self.menuFile.addAction(self.actionfirst)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionsecond)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python tutorial"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Settings"))
        self.actionfirst.setText(_translate("MainWindow", "first"))
        self.actionsecond.setText(_translate("MainWindow", "second"))
        self.action111.setText(_translate("MainWindow", "111"))
