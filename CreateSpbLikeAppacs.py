import openpyxl
import xlrd
import time
import os
import xlsxwriter
from PyQt5 import QtCore


class CreateFile:

    def __init__(self, fileName, dayCount, percent):
        super().__init__()
        self.percent = percent
        self.entryFile = fileName
        self.days = dayCount

    def run(self):
        newfile = os.path.expanduser("~\Desktop\СПБ_основа.xlsx")
        wbOut = openpyxl.Workbook()
        sheetOut = wbOut['Sheet']
        wbOut.save(newfile)
        wbOut.close()
        self.count = 0
        for j in range(25):
            self.count += 1
            self.percent.emit(self.count)

        last_data = self.remakeList()

        workbook = xlsxwriter.Workbook(newfile)
        worksheet = workbook.add_worksheet("Лист1")
        header = [
                    'Компания',
                    'Отдел',
                    'Должность',
                    'Пол',
                    'Фамилия',
                    'Имя',
                    'Отчество',
                    'Первый приход',
                    'Последний уход ',
                ]
        worksheet.write_row(0, 0, header)
        set_row = 1
        i = 0
        while i != len(last_data):
            worksheet.write_row(set_row, 0, last_data[i])
            set_row += self.days
            i += 1
        workbook.close()
        for j in range(25):
            self.count += 1
            self.percent.emit(self.count)

    def remakeList(self):
        workbook = xlrd.open_workbook(self.entryFile)
        worksheet = workbook.sheet_by_index(0)
        row = 0
        dataTest = []
        while row != worksheet.nrows:
            for col in range(worksheet.ncols - 2):
                dataTest.append(worksheet.cell_value(row, col))
            row += 1
        print(dataTest)
        new_data = []
        for i in range(0, len(dataTest) - 4, 5):
            new_data.append(dataTest[i:i + 5])
        print(new_data)
        for j in range(25):
            self.count += 1
            self.percent.emit(self.count)

        i = 1
        last_data = []
        last_data.append(new_data[0])
        while i != len(new_data):
            if new_data[i][3] != new_data[i - 1][3]:
                last_data.append(new_data[i])
            i += 1
        print(last_data)

        counts = []
        for i in range(len(last_data)):
            last_data[i][3], last_data[i][4] = last_data[i][4], last_data[i][3],
            FIO = last_data[i][4]
            j = 0
            counts.clear()
            while j < len(FIO):
                if FIO[j] == " ":
                    counts.append(j)
                j += 1
            last_data[i].append(FIO[0:counts[0]])
            last_data[i].append(FIO[counts[0] + 1:counts[1]])
            last_data[i].append(FIO[counts[1] + 1:])
            last_data[i].pop(4)
        for j in range(25):
            self.count += 1
            self.percent.emit(self.count)

        return last_data


class WorkWithNewFile(QtCore.QThread):
    percentageChanged = QtCore.pyqtSignal(int)
    indicator_of_end_work = QtCore.pyqtSignal(bool)

    def __init__(self, path, days):
        super().__init__()
        self.file = path
        self.numberOfDays = days
        # print("Введите кол-во за \который делается отчет: ")
        # self.day_of_month = int(input())

    def run(self):
        create = CreateFile(self.file, self.numberOfDays, self.percentageChanged)
        create.run()
        self.indicator = True
        self.indicator_of_end_work.emit(self.indicator)


if __name__ == '__main__':
    file = "Test.xlsx"
    print("Введите кол-во за \который делается отчет: ")
    day_of_month = int(input())
    start = WorkWithNewFile(file, day_of_month)
    start.run()
