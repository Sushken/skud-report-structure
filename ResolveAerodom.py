import openpyxl
import DeleteNullRows
import os


def Resolve(nameOfInFile):
    wbIn = openpyxl.load_workbook(filename=nameOfInFile)
    sheetIn = wbIn['Лист1']
    dataIn = sheetIn.values
    dataIn = list(dataIn)

    i = 7
    dataCompany = []
    dataStructure = []
    dataPosition = []
    dataFIO = []
    dataGender = []
    dataFirstIn = []
    dataLastOut = []
    while i != sheetIn.max_row:
        dataCompany.append(dataIn[i][0])  # +
        dataStructure.append(dataIn[i][2])  # +
        dataPosition.append(dataIn[i][5])  # +
        dataFIO.append(dataIn[i][7])  # +
        dataGender.append(dataIn[i][9])  # +
        dataFirstIn.append(dataIn[i][11])  # +
        dataLastOut.append(dataIn[i][14])  # +
        i += 1

    # print("dataCompny", dataCompany)
    # print("dataStructure", dataStructure)
    # print("dataPosition", dataPosition)
    # print("dataFIO", dataFIO)
    # print("dataGender", dataGender)
    # print("dataFirstIn", dataFirstIn)
    # print("dataLastOut", dataLastOut)

    filepath = os.path.expanduser("~/Desktop/Новый Аэродом.xlsx")
    wbOut = openpyxl.Workbook()
    sheetOut = wbOut['Sheet']

    i = 0
    while i != len(dataCompany):
        if dataCompany[i] != "Компания" and dataCompany[i] != '':
            sheetOut.cell(row=i + 1, column=1).value = dataCompany[i]
        if dataStructure[i] is not None and dataStructure[i] != "Отдел":
            sheetOut.cell(row=i + 1, column=2).value = dataStructure[i]
        if dataPosition[i] is not None and dataPosition[i] != "Должность":
            sheetOut.cell(row=i + 1, column=3).value = dataPosition[i]
        if dataFIO[i] is not None and dataFIO[i] != "ФИО":
            sheetOut.cell(row=i + 1, column=4).value = dataFIO[i]
        if dataGender[i] is not None and dataGender[i] != "Пол":
            sheetOut.cell(row=i + 1, column=5).value = dataGender[i]
        if dataFirstIn[i] is not None and dataFirstIn[i] != "Первый вход":
            sheetOut.cell(row=i + 1, column=6).value = dataFirstIn[i]
        if dataLastOut[i] is not None and dataLastOut[i] != "Последний уход":
            sheetOut.cell(row=i + 1, column=7).value = dataLastOut[i]
        i += 1
        print(i)
    wbOut.save(filepath)
    DeleteNullRows.main(filepath)
