# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\-\I.Sushkov\PycharmProjects\ExcelWork\Design\mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupChoseWindow(self, choseWindow):
        choseWindow.setObjectName("choseWindow")
        choseWindow.resize(400, 300)
        # choseWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_3 = QtWidgets.QPushButton(choseWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 60, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(choseWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 130, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(choseWindow)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 361, 81))
        self.label_7.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateChoseWindow(choseWindow)
        QtCore.QMetaObject.connectSlotsByName(choseWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 90, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)

        self.check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box.setGeometry(QtCore.QRect(610, 180, 16, 16))
        self.check_box.setObjectName("check_box")
        self.label_with_check_box = QtWidgets.QLabel(self.centralwidget)
        self.label_with_check_box.setGeometry(QtCore.QRect(630, 180, 121, 16))
        self.label_with_check_box.setObjectName("label_with_check_box")
        self.choseNumber = QtWidgets.QSpinBox(self.centralwidget)
        self.choseNumber.setGeometry(QtCore.QRect(610, 210, 41, 41))
        self.choseNumber.setRange(1, 31)
        self.choseNumber.setObjectName("choseNumber")
        self.choseNumber.hide()
        # self.testbutton = QtWidgets.QPushButton(self.centralwidget)
        # self.testbutton.setGeometry(QtCore.QRect(610, 300, 41, 41))
        # self.testbutton.setObjectName("testbutton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 60, 161, 31))
        self.label.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 90, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 201, 31))
        self.label_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 315, 201, 31))
        self.label_4.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(700, 90, 41, 31))
        self.toolButton_2.setStyleSheet("background-color: rgb(50, 83, 122);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 170, 121, 41))
        self.pushButton.setStyleSheet("background-color: rgb(50, 83, 122);\n"
                                      "font: 12pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(260, 90, 41, 31))
        self.toolButton.setStyleSheet("background-color: rgb(50, 83, 122);")
        self.toolButton.setObjectName("toolButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(10, 20, 751, 311))
        self.label_6.setGeometry(QtCore.QRect(10, 280, 321, 51))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupDialog(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 192)
        Dialog.setStyleSheet("background-color: rgb(34, 167, 255);")
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(130, 100, 75, 23))
        self.pushButton_1.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 311, 71))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")

        self.retranslateDialogUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setupWindowWhileWork(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(376, 154)
        self.progressBar = QtWidgets.QProgressBar(Dialog1)
        self.progressBar.hide()
        self.pushButton_2 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 70, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog1)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateWindowWhileWorkUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateChoseWindow(self, choseWindow):
        _translate = QtCore.QCoreApplication.translate
        choseWindow.setWindowTitle(_translate("choseWindow", "Выберите действие"))
        self.pushButton_3.setText(_translate("choseWindow", "Создание нового файла с БЦ Аэродом"))
        self.pushButton_4.setText(_translate("choseWindow", "Выполнить совмещение двух файлов"))
        self.label_7.setPixmap(QtGui.QPixmap("img.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Best Prog Ever Seen"))
        self.label.setText(_translate("MainWindow", "Файл с БЦ Аэродом"))
        self.label_2.setText(_translate("MainWindow", " Файл с Ленинградки 44"))
        self.label_4.setText(_translate("MainWindow", "Created & Designed by I.Sushkov"))
        self.label_6.setPixmap(QtGui.QPixmap("img.png"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_with_check_box.setText(_translate("MainWindow", "Удалить время выхода"))
        # self.testbutton.setText(_translate("MainWindow", "TEST"))


    def retranslateDialogUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Выполнено"))
        self.pushButton_1.setText(_translate("Dialog", "OK"))
        self.label_3.setText(_translate("Dialog", "Программа выполнена успешно! \n Нажмите ОК для закрытия."))

    def retranslateWindowWhileWorkUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Ожидайте"))
        self.pushButton_2.setText(_translate("Dialog1", "OK"))
        self.label_5.setText(_translate("Dialog1", "Нажмите ОК и дождитесь окончания программы!"))
