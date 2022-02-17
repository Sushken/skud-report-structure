# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\-\I.Sushkov\PycharmProjects\ExcelWork\Design\mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.styleForPushButtons = '''
               QPushButton{
                   border-style: outset;
                   border-width: 1.5px;
                   border-color: black;
               }
               QPushButton::hover {
                   background-color: lightgrey;
               }
        '''
        self.styleForWindows = '''
                background-color: white;                   
        '''
        self.styleForLineEdit = '''
                border: 1px solid black;
            '''


    def setupTestMenu(self, layOut):

        self.button_1 = QtWidgets.QPushButton("Первая кнопка")
        self.button_1.setStyleSheet(self.styleForPushButtons)
        self.button_1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.button_2 = QtWidgets.QPushButton("Вторая кнопка")
        self.button_2.setStyleSheet(self.styleForPushButtons)
        self.button_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        layOut.addWidget(self.button_1)
        layOut.addWidget(self.button_2)

    def setupStartMenu(self, startMenu):
        startMenu.setObjectName("startMenu")
        startMenu.resize(400, 400)
        startMenu.setStyleSheet(self.styleForWindows)

        layOut = QtWidgets.QGridLayout()
        widget = QtWidgets.QWidget()

        self.moodleButton = QtWidgets.QPushButton(startMenu)
        self.moodleButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.moodleButton.setStyleSheet(self.styleForPushButtons)

        self.skudButton = QtWidgets.QPushButton(startMenu)
        self.skudButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.skudButton.setStyleSheet(self.styleForPushButtons)

        layOut.addWidget(self.moodleButton)
        layOut.addWidget(self.skudButton)
        widget.setLayout(layOut)
        startMenu.setCentralWidget(widget)
        self.retranslateStartMenu(startMenu)

    def setupMoodleReport(self, moodleReport):
        moodleReport.setObjectName("moodleReport")
        moodleReport.resize(400, 550)
        moodleReport.setStyleSheet(self.styleForWindows)

        self.HcButton = QtWidgets.QPushButton(moodleReport)
        self.HcButton.setGeometry(QtCore.QRect(20, 60, 361, 51))
        self.HcButton.setStyleSheet(self.styleForPushButtons)

        self.KvrzButton = QtWidgets.QPushButton(moodleReport)
        self.KvrzButton.setGeometry(QtCore.QRect(20, 130, 361, 51))
        self.KvrzButton.setStyleSheet(self.styleForPushButtons)

        self.KvrpButton = QtWidgets.QPushButton(moodleReport)
        self.KvrpButton.setGeometry(QtCore.QRect(20, 200, 361, 51))
        self.KvrpButton.setStyleSheet(self.styleForPushButtons)

        self.VrpButton = QtWidgets.QPushButton(moodleReport)
        self.VrpButton.setGeometry(QtCore.QRect(20, 270, 361, 51))
        self.VrpButton.setStyleSheet(self.styleForPushButtons)

        self.BvrpButton = QtWidgets.QPushButton(moodleReport)
        self.BvrpButton.setGeometry(QtCore.QRect(20, 340, 361, 51))
        self.BvrpButton.setStyleSheet(self.styleForPushButtons)

        self.labelReportPath = QtWidgets.QLabel(moodleReport)
        self.labelReportPath.setGeometry(QtCore.QRect(20, 410, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.labelReportPath.setFont(font)
        self.labelReportPath.setAlignment(QtCore.Qt.AlignCenter)
        self.labelReportPath.setObjectName("labelReportPath")

        self.label_nv = QtWidgets.QLabel(moodleReport)
        self.label_nv.setGeometry(QtCore.QRect(20, 470, 361, 81))
        self.label_nv.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.label_nv.setObjectName("label_nv")

        self.retranslateMoodleReport(moodleReport)

    def setupFileSharingWindow(self, sharingWindow):
        sharingWindow.setObjectName("sharingWindow")
        sharingWindow.resize(400, 400)
        sharingWindow.setStyleSheet(self.styleForWindows)

        # First point
        self.labelForFirst = QtWidgets.QLabel(sharingWindow)
        self.labelForFirst.setGeometry(QtCore.QRect(30, 20, 161, 31))
        self.labelForFirst.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.labelForFirst.setObjectName("labelForFirst")
        self.lineForFirst = QtWidgets.QLineEdit(sharingWindow)
        self.lineForFirst.setGeometry(QtCore.QRect(50, 50, 240, 31))
        self.lineForFirst.setObjectName("lineForFirst")
        self.lineForFirst.setStyleSheet(self.styleForLineEdit)
        self.lineForFirst.setReadOnly(True)
        self.toolButtonForFirst = QtWidgets.QToolButton(sharingWindow)
        self.toolButtonForFirst.setGeometry(QtCore.QRect(300, 50, 41, 31))
        self.toolButtonForFirst.setStyleSheet("background-color: rgb(50, 83, 122);")
        self.toolButtonForFirst.setObjectName("toolButtonForFirst")

        # Second point
        self.labelForSecond = QtWidgets.QLabel(sharingWindow)
        self.labelForSecond.setGeometry(QtCore.QRect(30, 100, 200, 31))
        self.labelForSecond.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.labelForSecond.setObjectName("labelForSecond")
        self.comboForSecond = QtWidgets.QComboBox(sharingWindow)
        self.comboForSecond.setGeometry(QtCore.QRect(50, 130, 201, 31))
        self.comboForSecond.addItems(["ГК Новотранс", "Новотранс Актив", "РК Новотранс", "ХК Новотранс", "Арго", "УК Новотранс", "ПИИР",
                                      "Питер (НВТА)", "Питер (БТП)", "Питер (КУЛ)", "Питер (СК)", "Питер (БВРЗ)", "Питер (УК)", "Питер (Строй)", "Питер (ПУЛ)", "Питер (ПИИР)"])
        self.comboForSecond.setStyleSheet("border: 1px solid black;")

        # Third point
        self.labelForThird = QtWidgets.QLabel(sharingWindow)
        self.labelForThird.setGeometry(QtCore.QRect(30, 180, 300, 31))
        self.labelForThird.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.labelForThird.setObjectName("labelForThird")
        self.lineForThird = QtWidgets.QLineEdit(sharingWindow)
        self.lineForThird.setGeometry(QtCore.QRect(50, 210, 300, 31))
        self.lineForThird.setObjectName("lineForThird")
        self.lineForThird.setStyleSheet(self.styleForLineEdit)
        self.lineForThird.setReadOnly(False)

        # Start point
        self.pushStartButton = QtWidgets.QPushButton(sharingWindow)
        self.pushStartButton.setGeometry(QtCore.QRect(160, 260, 80, 50))
        self.pushStartButton.setStyleSheet(self.styleForPushButtons)

        self.retranslateSharingWindow(sharingWindow)
        QtCore.QMetaObject.connectSlotsByName(sharingWindow)

    def setup_SPB_ChoseWindow(self, SPBChoseWindow):
        SPBChoseWindow.setObjectName("SPBChoseWindow")
        SPBChoseWindow.resize(400, 400)
        SPBChoseWindow.setStyleSheet(self.styleForWindows)
        font = QtGui.QFont()
        font.setPointSize(10)
        # Make new file like APPACS
        self.buttonMakeFile = QtWidgets.QPushButton(SPBChoseWindow)
        self.buttonMakeFile.setGeometry(QtCore.QRect(20, 60, 361, 41))
        self.buttonMakeFile.setFont(font)
        self.buttonMakeFile.setStyleSheet(self.styleForPushButtons)
        self.buttonMakeFile.setObjectName("buttonMakeFile")

        # Chose number of days
        self.labelDays = QtWidgets.QLabel(SPBChoseWindow)
        self.labelDays.setGeometry(QtCore.QRect(20, 130, 150, 41))
        self.labelDays.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.labelDays.setObjectName("labelDays")
        self.numberOdDays = QtWidgets.QSpinBox(SPBChoseWindow)
        self.numberOdDays.setGeometry(QtCore.QRect(170, 130, 41, 41))
        self.numberOdDays.setRange(1, 31)
        self.numberOdDays.setObjectName("numberOdDays")


        # Button for doing migrations
        self.buttonMigrations = QtWidgets.QPushButton(SPBChoseWindow)
        self.buttonMigrations.setGeometry(QtCore.QRect(20, 200, 361, 41))
        self.buttonMigrations.setFont(font)
        self.buttonMigrations.setStyleSheet(self.styleForPushButtons)
        self.buttonMigrations.setObjectName("buttonMigrations")

        self.retranslateSPBChoseWindos(SPBChoseWindow)
        QtCore.QMetaObject.connectSlotsByName(SPBChoseWindow)

    def setupChoseWindow(self, choseWindow):
        choseWindow.setObjectName("choseWindow")
        choseWindow.resize(400, 450)
        choseWindow.setStyleSheet(self.styleForWindows)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3 = QtWidgets.QPushButton(choseWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 60, 361, 41))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(self.styleForPushButtons)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(choseWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 130, 361, 41))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(self.styleForPushButtons)
        self.pushButton_5 = QtWidgets.QPushButton(choseWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 270, 361, 41))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(self.styleForPushButtons)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(choseWindow)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 200, 361, 41))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(self.styleForPushButtons)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_7 = QtWidgets.QLabel(choseWindow)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 361, 81))
        self.label_7.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateChoseWindow(choseWindow)
        QtCore.QMetaObject.connectSlotsByName(choseWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 381)
        MainWindow.setStyleSheet(self.styleForWindows)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 90, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(self.styleForLineEdit)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 60, 161, 31))
        self.label.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 90, 201, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet(self.styleForLineEdit)
        self.lineEdit_2.setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 201, 30))
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
        Dialog1.setStyleSheet(self.styleForWindows)
        self.progressBar = QtWidgets.QProgressBar(Dialog1)
        self.progressBar.hide()
        self.pushButton_2 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 70, 141, 41))
        self.pushButton_2.setStyleSheet(self.styleForPushButtons)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_10 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 70, 141, 41))
        self.pushButton_10.setStyleSheet(self.styleForPushButtons)
        self.pushButton_10.setObjectName("pushButton_10")

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

    def retranslateSharingWindow(self, sharingWindow):
        _translate = QtCore.QCoreApplication.translate
        sharingWindow.setWindowTitle(_translate("sharingWindow", "Раскладывание по папкам"))
        self.labelForFirst.setText(_translate("sharingWindow", "1. Выберите файл"))
        self.toolButtonForFirst.setText(_translate("sharingWindow", "..."))
        self.labelForSecond.setText(_translate("sharingWindow", "2. Выберите компанию"))
        self.labelForThird.setText(_translate("sharingWindow", "3. Задайте имя создаваемых файлов"))
        self.pushStartButton.setText(_translate("sharingWindow", "START"))

    def retranslateSPBChoseWindos(self, SPBChoseWindow):
        _translate = QtCore.QCoreApplication.translate
        SPBChoseWindow.setWindowTitle(_translate("SPBChoseWindow", "Выберите действие"))
        self.buttonMakeFile.setText(_translate("SPBChoseWindow", "Создание файла-шаблона APPACS"))
        self.buttonMigrations.setText(_translate("SPBChoseWindow", "Совмещение двух файлов"))
        self.labelDays.setText(_translate("SPBChoseWindow", "Количество дней: "))

    def retranslateChoseWindow(self, choseWindow):
        _translate = QtCore.QCoreApplication.translate
        choseWindow.setWindowTitle(_translate("choseWindow", "Выберите действие"))
        self.pushButton_3.setText(_translate("choseWindow", "Создание нового файла с БЦ Аэродом"))
        self.pushButton_4.setText(_translate("choseWindow", "Выполнить совмещение двух файлов"))
        self.pushButton_5.setText(_translate("choseWindow", "Разложить файл по папкам на шаре"))
        self.pushButton_6.setText(_translate("choseWindow", "Питерский отчет"))
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

    def retranslateDialogUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Выполнено"))
        self.pushButton_1.setText(_translate("Dialog", "OK"))
        self.label_3.setText(_translate("Dialog", "Программа выполнена успешно! \n Нажмите ОК для закрытия."))

    def retranslateWindowWhileWorkUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Ожидайте"))
        self.pushButton_2.setText(_translate("Dialog1", "OK"))
        self.pushButton_10.setText(_translate("Dialog1", "ЗАКРЫТЬ"))
        self.label_5.setText(_translate("Dialog1", "Нажмите ОК и дождитесь окончания программы!"))

    def retranslateStartMenu(self,starMenu):
        _translate = QtCore.QCoreApplication.translate
        starMenu.setWindowTitle(_translate("startMenu", "Добро пожаловать!"))
        self.moodleButton.setText(_translate("startMenu", "Отчет Moodle"))
        self.skudButton.setText(_translate("startMenu", "Отчет СКУД"))

    def retranslateMoodleReport(self, moodleReport):
        _translate = QtCore.QCoreApplication.translate
        moodleReport.setWindowTitle(_translate("moodleReport", "Добро пожаловать!"))
        self.HcButton.setText(_translate("moodleReport", "Отчет ЦА"))
        self.KvrzButton.setText(_translate("moodleReport", "Отчет КВРЗ"))
        self.KvrpButton.setText(_translate("moodleReport", "Отчет КВРП"))
        self.VrpButton.setText(_translate("moodleReport", "Отчет ВРП"))
        self.BvrpButton.setText(_translate("moodleReport", "Отчет БВРП"))
        self.labelReportPath.setText(_translate("moodleReport", "N:\УК\УКБ\Курсы Moodle\Отчеты\ \n Временная папка для программы\\"))
        self.label_nv.setPixmap(QtGui.QPixmap("img.png"))