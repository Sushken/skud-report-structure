from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog

import MyDesign  # импорт нашего сгенерированного файла
import sys
import AddFullNameOnPostions, ResolveSeconds, Main, AddSumOfTime, AddTimeOfWork, ResolveAerodom, AddTimeOfWorkUnchecked
import time


class choseWindow(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupChoseWindow(self)
        self.pushButton_3.clicked.connect(self.createAerodom)
        self.pushButton_4.clicked.connect(self.mainProg)

    def createAerodom(self):
        filename = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Excel Files *.xlsx")
        self.path = filename[0]
        print(self.path)
        self.WWC = windowWhileCreate(self.path)
        self.WWC.show()

    def mainProg(self):
        self.mainWindow = mywindow()
        self.mainWindow.show()


class windowWhileCreate(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.setupWindowWhileWork(self)
        self.pushButton_2.clicked.connect(self.getResolveAerodom)

    def getResolveAerodom(self):
        self.pushButton_2.close()
        self.progressBar.show()
        self.progressBar.setGeometry(QtCore.QRect(130, 70, 141, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        ResolveAerodom.Resolve(self.path)
        self.progressBar.setProperty("value", 100)


class mywindow(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.check_box.clicked.connect(self.test)
        self.toolButton.clicked.connect(self.open_dialog_box)
        self.toolButton_2.clicked.connect(self.open_dialog_box_1)
        self.pushButton.clicked.connect(self.Showing)
        # self.testbutton.clicked.connect(self.print_number)

    # def print_number(self):
    #     if self.choseNumber.isVisible():
    #         print(self.choseNumber.value())

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
            self.waitWindow = windowWhileWork(self.path, self.path1, self.choseNumber.value())
            self.waitWindow.show()
        else:
            print("ALL IS WORK!!! YEAH, VICTORY!!!!!!!")
            self.waitWindow = windowWhileWorkIfChecked(self.path, self.path1)
            self.waitWindow.show()


class closeWindow(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupDialog(self)
        self.pushButton_1.clicked.connect(self.closeProg)

    def closeProg(self):
        sys.exit(0)


class windowWhileWorkIfChecked(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):
    def __init__(self, path, path1):
        super().__init__()
        self.path = path
        self.path1 = path1
        self.setupWindowWhileWork(self)
        self.pushButton_2.clicked.connect(self.getStart)

    def getStart(self):
        self.pushButton_2.close()
        self.progressBar.show()
        self.progressBar.setGeometry(QtCore.QRect(130, 70, 141, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.goToWork()
        time.sleep(2)
        self.w2 = closeWindow()
        self.w2.show()

    def goToWork(self):
        print("AddFullNameOnPositions")
        AddFullNameOnPostions.AddName(self.path, self.path1)
        self.progressBar.setValue(20)
        print("ResolveSeconds")
        ResolveSeconds.ResolveSeconds(self.path, self.path1)
        self.progressBar.setValue(40)
        print("Main")
        Main.main(self.path, self.path1)
        self.progressBar.setValue(60)
        print("AddSumOfTime")
        AddSumOfTime.AddSumOfTime(self.path, self.path1)
        self.progressBar.setValue(80)
        print("AddTimeOfWorkUnchecked")
        AddTimeOfWorkUnchecked.AddTimeOfWork(self.path, self.path1)
        self.progressBar.setValue(100)


class windowWhileWork(QtWidgets.QMainWindow, MyDesign.Ui_MainWindow):
    def __init__(self, path, path1, value):
        super().__init__()
        self.value = value
        self.path = path
        self.path1 = path1
        self.setupWindowWhileWork(self)
        self.pushButton_2.clicked.connect(self.getStart)

    def getStart(self):
        self.pushButton_2.close()
        self.progressBar.show()
        self.progressBar.setGeometry(QtCore.QRect(130, 70, 141, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.goToWork()
        time.sleep(2)
        self.w2 = closeWindow()
        self.w2.show()

    def goToWork(self):
        print("AddFullNameOnPositions")
        AddFullNameOnPostions.AddName(self.path, self.path1)
        self.progressBar.setValue(20)
        print("ResolveSeconds")
        ResolveSeconds.ResolveSeconds(self.path, self.path1)
        self.progressBar.setValue(40)
        print("Main")
        Main.main(self.path, self.path1)
        self.progressBar.setValue(60)
        print("AddSumOfTime")
        AddSumOfTime.AddSumOfTime(self.path, self.path1)
        self.progressBar.setValue(80)
        print("AddTimeOfWork")
        print(self.value)
        AddTimeOfWork.AddTimeOfWork(self.path, self.path1, self.value)
        self.progressBar.setValue(100)


def main():
    app = QtWidgets.QApplication(sys.argv)
    _choseWindow = choseWindow()
    _choseWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
