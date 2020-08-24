import sys
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
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog


class choseWindow(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupChoseWindow(self)
        self.pushButton_3.clicked.connect(self.createAerodom)
        self.pushButton_4.clicked.connect(self.mainProg)
        self.pushButton_5.clicked.connect(self.fileDelivery)

    def createAerodom(self):
        filename = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Excel Files *.xlsx")
        self.path = filename[0]
        print(self.path)
        if self.path:
            self.WWC = windowWhileCreate(self.path)
            self.WWC.show()

    def mainProg(self):
        self.mainWindow = mywindow()
        self.mainWindow.show()

    def fileDelivery(self):
        self.share = fileSharing()
        self.share.show()


class fileSharing(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupFileSharingWindow(self)
        self.toolButtonForFirst.clicked.connect(self.openDialogBox)
        self.pushStartButton.clicked.connect(self.goSharing)

    def openDialogBox(self):
        filename = QFileDialog.getOpenFileName(self, "Выберите файо", "", "Excel Files *.xlsx")
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
            print(self.path)
            return self.path

    def goSharing(self):
        treadSharing = SharingFIles.WorkWithFile(self.path, self.comboForSecond.currentText(), self.lineForThird.text())
        treadSharing.indicator_of_end_work.connect(self.closeOne)
        treadSharing.run()
        # time.sleep(1)
        # self.labelPNG.show()
        # self.labelEnd.show()
        # self.endButton.show()
        # self.endButton.clicked.connect(self.closeOne)
        # self.setStyleSheet("background-color: white;")

    def closeOne(self):
        time.sleep(1)
        self.hide()
        self.w2 = closeWindow()
        self.w2.show()
        # self.close()


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
            self.lineEdit.setText(self.pathOfName)
            self.lineEdit.setStyleSheet("font: 12pt \"Times New Roman\";")
            self.lineEdit.setReadOnly(True)
            print(self.path)
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
            print(self.path1)
            return self.path1

    def Showing(self):
        if self.choseNumber.isVisible():
            self.close()
            self.waitWindow = windowWhileWork(self.path, self.path1, self.choseNumber.value())
            self.waitWindow.show()
        else:
            print("ALL IS WORK!!! YEAH, VICTORY!!!!!!!")
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
        print("AddFullNameOnPositions")
        self.thread_addFullNameOnPositions = AddFullNameOnPostions.AddName(self.path, self.path1, self.count)
        self.thread_addFullNameOnPositions.percentageChanged.connect(self.progressBar.setValue)
        self.thread_addFullNameOnPositions.indicator_of_end_work.connect(self.closeEvent)
        self.thread_addFullNameOnPositions.start()

    def closeEvent(self, indicator):
        self.count = self.thread_addFullNameOnPositions.count
        print(self.count, "count after first thread")
        if indicator is True:
            if self.thread_addFullNameOnPositions.isFinished():
                print("fork is down!")
            else:
                print("fork is not down!")
            print("start the 2 thread")
            self.thread_ResolveSeconds = ResolveSeconds.ResolveSeconds(self.path, self.path1, self.count)
            self.thread_ResolveSeconds.percentageChanged.connect(self.progressBar.setValue)
            self.thread_ResolveSeconds.indicator_of_end_work.connect(self.go_to_main_thread)
            self.thread_ResolveSeconds.start()

    def go_to_main_thread(self, indicator):
        self.count = self.thread_ResolveSeconds.count
        print(self.count, "count after second thread")
        if indicator is True:
            if self.thread_ResolveSeconds.isFinished():
                print("fork is down!")
            else:
                print("fork is not down!")
            print("start the 3 thread")
            self.thread_main = Main.Main(self.path, self.path1, self.count)
            self.thread_main.percentageChanged.connect(self.progressBar.setValue)
            self.thread_main.indicator_of_end_work.connect(self.go_to_addSumOfTime_thread)
            self.thread_main.start()

    def go_to_addSumOfTime_thread(self, indicator):
        self.count = self.thread_main.count
        print(self.count, "count after third thread")
        if indicator is True:
            if self.thread_main.isFinished():
                print("fork is down!")
            else:
                print("fork is not down!")
            print("start the 4 thread")
            self.thread_addSumOfTime = AddSumOfTime.AddSumOfTime(self.path, self.path1, self.count)
            self.thread_addSumOfTime.percentageChanged.connect(self.progressBar.setValue)
            self.thread_addSumOfTime.indicator_of_end_work.connect(self.go_to_addTimeOfWorkUnchecked_thread)
            self.thread_addSumOfTime.start()

    def go_to_addTimeOfWorkUnchecked_thread(self, indicator):
        self.count = self.thread_addSumOfTime.count
        print(self.count, "count after fourth thread")
        if indicator is True:
            if self.thread_addSumOfTime.isFinished():
                print("fork is down!")
            else:
                print("fork is not down!")
            print("start the 5 thread")
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
        print("AddFullNameOnPositions")
        self.thread_addFullNameOnPositions = AddFullNameOnPostions.AddName(self.path, self.path1, self.count)
        self.thread_addFullNameOnPositions.percentageChanged.connect(self.progressBar.setValue)
        self.thread_addFullNameOnPositions.indicator_of_end_work.connect(self.closeEvent)
        self.thread_addFullNameOnPositions.start()

    def closeEvent(self, indicator):
        self.count = self.thread_addFullNameOnPositions.count
        print(self.count, "count after first thread")
        if indicator is True:
            if self.thread_addFullNameOnPositions.isFinished():
                print("fork is down!")
            else:
                print("fork is not down!")
            print("start the 2 thread")
            self.thread_ResolveSeconds = ResolveSeconds.ResolveSeconds(self.path, self.path1, self.count)
            self.thread_ResolveSeconds.percentageChanged.connect(self.progressBar.setValue)
            self.thread_ResolveSeconds.indicator_of_end_work.connect(self.go_to_main_thread)
            self.thread_ResolveSeconds.start()

    def go_to_main_thread(self, indicator):
        self.count = self.thread_ResolveSeconds.count
        print(self.count, "count after second thread")
        if indicator is True:
            if self.thread_ResolveSeconds.isFinished():
                print("fork is down!")
            else:
                print("fork is not down!")
            print("start the 3 thread")
            self.thread_main = Main.Main(self.path, self.path1, self.count)
            self.thread_main.percentageChanged.connect(self.progressBar.setValue)
            self.thread_main.indicator_of_end_work.connect(self.go_to_addSumOfTime_thread)
            self.thread_main.start()

    def go_to_addSumOfTime_thread(self, indicator):
        self.count = self.thread_main.count
        print(self.count, "count after third thread")
        if indicator is True:
            if self.thread_main.isFinished():
                print("fork is down!")
            else:
                print("fork is not down!")
            print("start the 4 thread")
            self.thread_addSumOfTime = AddSumOfTime.AddSumOfTime(self.path, self.path1, self.count)
            self.thread_addSumOfTime.percentageChanged.connect(self.progressBar.setValue)
            self.thread_addSumOfTime.indicator_of_end_work.connect(self.go_to_addTimeOfWorkUnchecked_thread)
            self.thread_addSumOfTime.start()

    def go_to_addTimeOfWorkUnchecked_thread(self, indicator):
        self.count = self.thread_addSumOfTime.count
        print(self.count, "count after fourth thread")
        if indicator is True:
            if self.thread_addSumOfTime.isFinished():
                print("fork is down!")
            else:
                print("fork is not down!")
            print("start the 5 thread")
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
    _choseWindow = choseWindow()
    _choseWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
