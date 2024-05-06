# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adder_1.1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 502)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.num = QtWidgets.QLineEdit(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(200, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num.setFont(font)
        self.num.setText("")
        self.num.setObjectName("num")
        self.num_labe = QtWidgets.QLabel(self.centralwidget)
        self.num_labe.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.num_labe.setFont(font)
        self.num_labe.setObjectName("num_labe")
        self.sum_labe = QtWidgets.QLabel(self.centralwidget)
        self.sum_labe.setGeometry(QtCore.QRect(10, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sum_labe.setFont(font)
        self.sum_labe.setObjectName("sum_labe")
        self.sum = QtWidgets.QLineEdit(self.centralwidget)
        self.sum.setGeometry(QtCore.QRect(130, 40, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sum.setFont(font)
        self.sum.setText("")
        self.sum.setObjectName("sum")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.before_labe = QtWidgets.QLabel(self.centralwidget)
        self.before_labe.setGeometry(QtCore.QRect(10, 70, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.before_labe.setFont(font)
        self.before_labe.setObjectName("before_labe")
        self.after_labe = QtWidgets.QLabel(self.centralwidget)
        self.after_labe.setGeometry(QtCore.QRect(190, 70, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.after_labe.setFont(font)
        self.after_labe.setObjectName("after_labe")
        self.before = QtWidgets.QLineEdit(self.centralwidget)
        self.before.setGeometry(QtCore.QRect(40, 70, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.before.setFont(font)
        self.before.setText("")
        self.before.setObjectName("before")
        self.after = QtWidgets.QLineEdit(self.centralwidget)
        self.after.setGeometry(QtCore.QRect(230, 70, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.after.setFont(font)
        self.after.setObjectName("after")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(240, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(10, 100, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.info.setFont(font)
        self.info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.labe_control = QtWidgets.QLabel(self.centralwidget)
        self.labe_control.setGeometry(QtCore.QRect(240, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labe_control.setFont(font)
        self.labe_control.setAlignment(QtCore.Qt.AlignCenter)
        self.labe_control.setObjectName("labe_control")
        self.c_avto = QtWidgets.QCheckBox(self.centralwidget)
        self.c_avto.setGeometry(QtCore.QRect(240, 140, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c_avto.setFont(font)
        self.c_avto.setObjectName("c_avto")
        self.c_hand = QtWidgets.QCheckBox(self.centralwidget)
        self.c_hand.setGeometry(QtCore.QRect(240, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c_hand.setFont(font)
        self.c_hand.setObjectName("c_hand")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 221, 311))
        self.textEdit.setObjectName("textEdit")
        self.rad_auto = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_auto.setGeometry(QtCore.QRect(240, 230, 82, 17))
        self.rad_auto.setChecked(True)
        self.rad_auto.setObjectName("rad_auto")
        self.rad_hend = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_hend.setGeometry(QtCore.QRect(240, 260, 82, 17))
        self.rad_hend.setObjectName("rad_hend")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.num_labe.setText(_translate("MainWindow", "Колличество"))
        self.sum_labe.setText(_translate("MainWindow", "Сумма"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.before_labe.setText(_translate("MainWindow", "От"))
        self.after_labe.setText(_translate("MainWindow", "До"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.info.setText(_translate("MainWindow", "Info"))
        self.labe_control.setText(_translate("MainWindow", "Control"))
        self.c_avto.setText(_translate("MainWindow", "Авто"))
        self.c_hand.setText(_translate("MainWindow", "Ручной"))
        self.rad_auto.setText(_translate("MainWindow", "Авто"))
        self.rad_hend.setText(_translate("MainWindow", "Ручной"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
