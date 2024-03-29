import sys
import os
import time
import AddFullNameOnPostions
import AddSumOfTime
import AddTimeOfWork
import AddTimeOfWorkUnchecked
import Main
import MyDesign  # импорт нашего сгенерированного файла
import ResolveAerodom
import ResolveSeconds
import SharingFIles
import CreateSpbLikeAppacs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
import SQLConnector


class startUpMenu(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupStartMenu(self)
        self.moodleButton.clicked.connect(self.goToMoodle)
        self.skudButton.clicked.connect(self.goToSkud)

    def goToMoodle(self):
        self.moodleReport_ = moodleReport()
        self.moodleReport_.show()

    def goToSkud(self):
        self.choseWindow_ = choseWindow()
        self.choseWindow_.show()


class moodleReport(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupMoodleReport(self)
        self.HcButton.clicked.connect(self.getHCReport)
        self.KvrzButton.clicked.connect(self.getKvrzReport)
        self.KvrpButton.clicked.connect(self.getKvrpReport)
        self.VrpButton.clicked.connect(self.getVrpReport)
        self.BvrpButton.clicked.connect(self.getBvrpReport)


    def getHCReport(self):
        SQLConnector.get_report('hc')
        self.test = closeWindow()
        self.test.show()


    def getKvrzReport(self):
        SQLConnector.get_report('kvrz')
        self.test = closeWindow()
        self.test.show()

    def getKvrpReport(self):
        SQLConnector.get_report('kvrp')
        self.test = closeWindow()
        self.test.show()

    def getVrpReport(self):
        SQLConnector.get_report('vrp')
        self.test = closeWindow()
        self.test.show()


    def getBvrpReport(self):
        SQLConnector.get_report('bvrp')
        self.test = closeWindow()
        self.test.show()
        self.hide()


class choseWindow(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupChoseWindow(self)
        self.pushButton_3.clicked.connect(self.createAerodom)
        self.pushButton_4.clicked.connect(self.mainProg)
        self.pushButton_5.clicked.connect(self.fileDelivery)
        self.pushButton_6.clicked.connect(self.SPB)

    def createAerodom(self):
        filename = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Excel Files *.xlsx")
        self.path = filename[0]
        if self.path:
            self.WWC = windowWhileCreate(self.path)
            self.WWC.show()

    def mainProg(self):
        self.mainWindow = mywindow()
        self.mainWindow.show()

    def fileDelivery(self):
        self.share = fileSharing()
        self.share.show()

    def SPB(self):
        self.spb = SPBChoseWindow()
        self.spb.show()


class SPBChoseWindow(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setup_SPB_ChoseWindow(self)
        self.buttonMakeFile.clicked.connect(self.makeNewFile)
        self.buttonMigrations.clicked.connect(self.makeMigrations)


    def makeNewFile(self):
        filename = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Excel Files *.xlsx")
        self.path = filename[0]
        if self.path:
            self.createFile = SPBCreateFile(self.path, self.numberOdDays.value())
            self.createFile.show()

    def makeMigrations(self):
        self.migrate = mywindow()
        self.migrate.label_2.setText("Шаблон Питер")
        self.migrate.label.setText("Болид Питер")
        self.migrate.label_with_check_box.hide()
        self.migrate.check_box.hide()
        self.migrate.show()
        # self.migrate = SPBMigration()
        # self.migrate.show()


class SPBCreateFile(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self, path, days):
        super().__init__()
        self.setupWindowWhileWork(self)
        self.path = path
        self.numberOfDays = days
        self.pushButton_10.hide()
        self.pushButton_2.clicked.connect(self.getCreate)

    def getCreate(self):
        self.pushButton_2.close()
        self.progressBar.show()
        self.progressBar.setGeometry(QtCore.QRect(130, 70, 141, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.thread_of_CreateSPBLikeAppacs = CreateSpbLikeAppacs.WorkWithNewFile(self.path, self.numberOfDays)
        self.thread_of_CreateSPBLikeAppacs.percentageChanged.connect(self.progressBar.setValue)
        self.thread_of_CreateSPBLikeAppacs.indicator_of_end_work.connect(self.close)
        self.thread_of_CreateSPBLikeAppacs.start()

    def close(self):
        time.sleep(1.5)
        self.progressBar.hide()
        self.pushButton_10.show()
        self.pushButton_10.clicked.connect(self.hide_window)

    def hide_window(self):
        self.hide()


class fileSharing(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupFileSharingWindow(self)
        self.toolButtonForFirst.clicked.connect(self.openDialogBox)
        self.pushStartButton.clicked.connect(self.goSharing)

    def openDialogBox(self):
        filename = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Excel Files *.xlsx")
        self.path = filename[0]
        if self.path != '':
            count = 0
            for i in range(len(self.path)):
                if self.path[i] == '.' and self.path[i + 1] == 'x':
                    j = i
                    countOfName = 0
                    while self.path[j] != '/':
                        j -= 1
                        countOfName += 1
                    self.pathOfName = self.path[count - countOfName + 1:]
                    i = len(self.path)
                else:
                    count += 1
            self.lineForFirst.setText(self.pathOfName)
            self.lineForFirst.setStyleSheet("font: 12pt \"Times New Roman\";")
            self.lineForFirst.setReadOnly(True)
            return self.path

    def goSharing(self):
        treadSharing = SharingFIles.WorkWithFile(self.path, self.comboForSecond.currentText(), self.lineForThird.text())
        treadSharing.indicator_of_end_work.connect(self.closeOne)
        treadSharing.run()

    def closeOne(self):
        time.sleep(1)
        self.hide()
        self.w2 = closeWindow()
        self.w2.show()


class windowWhileCreate(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):


    def __init__(self, path):
        super().__init__()

        self.path = path
        self.count = 0
        self.setupWindowWhileWork(self)
        self.pushButton_10.hide()
        self.pushButton_2.clicked.connect(self.getResolveAerodom)

    def getResolveAerodom(self):
        self.pushButton_2.close()
        self.progressBar.show()
        self.progressBar.setGeometry(QtCore.QRect(130, 70, 141, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.goToWork()

    def goToWork(self):
        self.thread_of_ResolveAerodom = ResolveAerodom.Resolve(self.path, self.count)
        self.thread_of_ResolveAerodom.percentageChanged.connect(self.progressBar.setValue)
        self.thread_of_ResolveAerodom.indicator_of_end_work.connect(self.close)
        self.thread_of_ResolveAerodom.start()

    def close(self):
        time.sleep(1.5)
        self.progressBar.hide()
        self.label_5.setText("Продолжительность работы: " + str(self.thread_of_ResolveAerodom.duration))
        self.pushButton_10.show()
        self.pushButton_10.clicked.connect(self.hide_window)

    def hide_window(self):
        self.hide()


class mywindow(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.check_box.clicked.connect(self.test)
        self.toolButton.clicked.connect(self.open_dialog_box)
        self.toolButton_2.clicked.connect(self.open_dialog_box_1)
        self.pushButton.clicked.connect(self.Showing)

    def test(self):
        if self.choseNumber.isVisible():
            self.choseNumber.hide()
        else:
            self.choseNumber.show()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(self, "Выберите файл", os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop'), "Excel Files *.xlsx")
        self.path = filename[0]
        if self.path != '':
            count = 0
            for i in range(len(self.path)):
                if self.path[i] == '.' and self.path[i + 1] == 'x':
                    j = i
                    countOfName = 0
                    while self.path[j] != '/':
                        j -= 1
                        countOfName += 1
                    self.pathOfName = self.path[count - countOfName + 1:]
                    i = len(self.path)
                else:
                    count += 1
            self.lineEdit.setText(self.pathOfName)
            self.lineEdit.setStyleSheet("font: 12pt \"Times New Roman\";")
            self.lineEdit.setReadOnly(True)
            return self.path

    def open_dialog_box_1(self):
        filename1 = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Excel Files *.xlsx")
        self.path1 = filename1[0]
        if self.path1 != '':
            count = 0
            for i in range(len(self.path1)):
                if self.path1[i] == '.' and self.path1[i + 1] == 'x':
                    j = i
                    countOfName = 0
                    while self.path1[j] != '/':
                        j -= 1
                        countOfName += 1
                    self.pathOfName = self.path1[count - countOfName + 1:]
                    i = len(self.path1)
                else:
                    count += 1
            self.lineEdit_2.setText(self.pathOfName)
            self.lineEdit_2.setStyleSheet("font: 12pt \"Times New Roman\";")
            return self.path1

    def Showing(self):
        if self.choseNumber.isVisible():
            self.close()
            self.waitWindow = windowWhileWork(self.path, self.path1, self.choseNumber.value())
            self.waitWindow.show()
        else:
            self.close()
            self.waitWindow = windowWhileWorkIfNotChecked(self.path, self.path1)
            self.waitWindow.show()


class closeWindow(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupDialog(self)
        self.pushButton_1.clicked.connect(self.closeProg)

    def closeProg(self):
        self.hide()


class windowWhileWorkIfNotChecked(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):
    def __init__(self, path, path1):
        super().__init__()
        self.path = path
        self.path1 = path1
        self.count = 0
        self.setupWindowWhileWork(self)
        self.pushButton_10.hide()
        self.pushButton_2.clicked.connect(self.getStart)

    def getStart(self):
        self.pushButton_2.close()
        self.progressBar.show()
        self.progressBar.setGeometry(QtCore.QRect(130, 70, 141, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.goToWork()
        time.sleep(2)

    def goToWork(self):
        self.thread_addFullNameOnPositions = AddFullNameOnPostions.AddName(self.path, self.path1, self.count)
        self.thread_addFullNameOnPositions.percentageChanged.connect(self.progressBar.setValue)
        self.thread_addFullNameOnPositions.indicator_of_end_work.connect(self.closeEvent)
        self.thread_addFullNameOnPositions.start()

    def closeEvent(self, indicator):
        self.count = self.thread_addFullNameOnPositions.count
        if indicator is True:
            self.thread_ResolveSeconds = ResolveSeconds.ResolveSeconds(self.path, self.path1, self.count)
            self.thread_ResolveSeconds.percentageChanged.connect(self.progressBar.setValue)
            self.thread_ResolveSeconds.indicator_of_end_work.connect(self.go_to_main_thread)
            self.thread_ResolveSeconds.start()

    def go_to_main_thread(self, indicator):
        self.count = self.thread_ResolveSeconds.count
        if indicator is True:
            self.thread_main = Main.Main(self.path, self.path1, self.count)
            self.thread_main.percentageChanged.connect(self.progressBar.setValue)
            self.thread_main.indicator_of_end_work.connect(self.go_to_addSumOfTime_thread)
            self.thread_main.start()

    def go_to_addSumOfTime_thread(self, indicator):
        self.count = self.thread_main.count
        if indicator is True:
            self.thread_addSumOfTime = AddSumOfTime.AddSumOfTime(self.path, self.path1, self.count)
            self.thread_addSumOfTime.percentageChanged.connect(self.progressBar.setValue)
            self.thread_addSumOfTime.indicator_of_end_work.connect(self.go_to_addTimeOfWorkUnchecked_thread)
            self.thread_addSumOfTime.start()

    def go_to_addTimeOfWorkUnchecked_thread(self, indicator):
        self.count = self.thread_addSumOfTime.count
        if indicator is True:
            self.thread_addTimeOfWorkUnchecked = AddTimeOfWorkUnchecked.AddTimeOfWork(self.path, self.path1, self.count)
            self.thread_addTimeOfWorkUnchecked.percentageChanged.connect(self.progressBar.setValue)
            self.thread_addTimeOfWorkUnchecked.indicator_of_end_work.connect(self.closeThisShit)
            self.thread_addTimeOfWorkUnchecked.start()

    def closeThisShit(self):
        self.w2 = closeWindow()
        self.w2.show()


class windowWhileWork(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self, path, path1, value):
        super().__init__()
        self.value = value
        self.path = path
        self.path1 = path1
        self.count = 0
        self.setupWindowWhileWork(self)
        self.pushButton_10.hide()
        self.pushButton_2.clicked.connect(self.getStart)

    def getStart(self):
        self.pushButton_2.close()
        self.progressBar.show()
        self.progressBar.setGeometry(QtCore.QRect(130, 70, 141, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.goToWork()

    def goToWork(self):
        self.thread_addFullNameOnPositions = AddFullNameOnPostions.AddName(self.path, self.path1, self.count)
        self.thread_addFullNameOnPositions.percentageChanged.connect(self.progressBar.setValue)
        self.thread_addFullNameOnPositions.indicator_of_end_work.connect(self.closeEvent)
        self.thread_addFullNameOnPositions.start()

    def closeEvent(self, indicator):
        self.count = self.thread_addFullNameOnPositions.count
        if indicator is True:
            self.thread_ResolveSeconds = ResolveSeconds.ResolveSeconds(self.path, self.path1, self.count)
            self.thread_ResolveSeconds.percentageChanged.connect(self.progressBar.setValue)
            self.thread_ResolveSeconds.indicator_of_end_work.connect(self.go_to_main_thread)
            self.thread_ResolveSeconds.start()

    def go_to_main_thread(self, indicator):
        self.count = self.thread_ResolveSeconds.count
        if indicator is True:
            self.thread_main = Main.Main(self.path, self.path1, self.count)
            self.thread_main.percentageChanged.connect(self.progressBar.setValue)
            self.thread_main.indicator_of_end_work.connect(self.go_to_addSumOfTime_thread)
            self.thread_main.start()

    def go_to_addSumOfTime_thread(self, indicator):
        self.count = self.thread_main.count
        if indicator is True:
            self.thread_addSumOfTime = AddSumOfTime.AddSumOfTime(self.path, self.path1, self.count)
            self.thread_addSumOfTime.percentageChanged.connect(self.progressBar.setValue)
            self.thread_addSumOfTime.indicator_of_end_work.connect(self.go_to_addTimeOfWorkUnchecked_thread)
            self.thread_addSumOfTime.start()

    def go_to_addTimeOfWorkUnchecked_thread(self, indicator):
        self.count = self.thread_addSumOfTime.count
        if indicator is True:
            self.thread_addTimeOfWork = AddTimeOfWork.AddTimeOfWork(self.path, self.path1, self.count, self.value)
            self.thread_addTimeOfWork.percentageChanged.connect(self.progressBar.setValue)
            self.thread_addTimeOfWork.indicator_of_end_work.connect(self.closeThisShit)
            self.thread_addTimeOfWork.start()

    def closeThisShit(self):
        time.sleep(1)
        self.hide()
        self.w2 = closeWindow()
        self.w2.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    startMenu = startUpMenu()
    startMenu.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
