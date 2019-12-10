import openpyxl


def main(nameOfOutFile, nameOfInFile):
    wbIn = openpyxl.load_workbook(filename=nameOfInFile)
    sheetIn = wbIn['Sheet']
    dataIn = sheetIn.values
    dataIn = list(dataIn)

    wbOut = openpyxl.load_workbook(filename=nameOfOutFile)
    sheetOut = wbOut['Лист1']
    dataOut = sheetOut.values
    dataOut = list(dataOut)

    # СОЗДАНИЕ ЛИСТОВ С ФАМИЛИЯМИ И ВРЕМЕНЕМ ПРИХОДА И УХОДА
    i = 0
    dataNameIn = []
    while i != sheetIn.max_row:
        dataNameIn.append(dataIn[i][3])
        i += 1
    j = 0
    dataNameOut = []
    while j != sheetOut.max_row:
        dataNameOut.append(dataOut[j][4] + ' ' + dataOut[j][5] + ' ' + dataOut[j][6])
        j += 1

    i = 0
    oneSecondName = 0
    while dataNameOut[i] == dataNameOut[i + 1]:
        oneSecondName += 1
        i += 1
    print(oneSecondName)

    print(dataNameIn)
    print(dataNameOut)
    i = 0
    dataTimeIn = []
    dataTimeInExit = []
    while i != sheetIn.max_row:
        dataTimeIn.append(dataIn[i][5])
        dataTimeInExit.append(dataIn[i][6])
        i += 1
    print(dataTimeIn, "dataTimeIn")
    print(dataTimeInExit, "dataTimeInExit")
    j = 0
    dataTimeOut = []
    dataTimeOutExit = []
    while j != sheetOut.max_row:
        dataTimeOut.append(dataOut[j][7])
        dataTimeOutExit.append(dataOut[j][8])
        j += 1
    print(dataTimeOut, "dataTimeOut")
    print(dataTimeOutExit, "dataTimeOutExit")

    print("Сравнение времени входа")
    # Сравнение времени входа
    for j in range(len(dataNameIn)):
        i = 0
        while i <= len(dataNameOut):
            for h in range(oneSecondName):
                if (i + h) < len(dataNameOut):
                    if dataNameIn[j] == dataNameOut[i + h]:
                        tmpData = str(dataTimeIn[j])[0:2]
                        if tmpData != "Пр":
                            if dataTimeOut[i + int(tmpData) - 1] is None:
                                sheetOut.cell(row=i + int(tmpData), column=8).value = dataTimeIn[j]
                            else:
                                if (str(dataTimeIn[j])[:10] == str(dataTimeOut[i + int(tmpData) - 1])[:10]) and (
                                        str(dataTimeIn[j])[11:] < str(dataTimeOut[i + int(tmpData) - 1])[11:]):
                                    sheetOut.cell(row=i + int(tmpData), column=8).value = dataTimeIn[j]
                        else:
                            sheetOut.cell(row=i + int(str(dataTimeInExit[j])[0:2]), column=8).value = dataTimeIn[j]
            i += oneSecondName + 1
    wbOut.save(filename=nameOfOutFile)
    print("Время входа поменялось!")
    # Сравнение времени выхода
    for j in range(len(dataNameIn)):
        i = 0
        while i <= len(dataNameOut):
            for h in range(oneSecondName):
                if (i + h) < len(dataNameOut):
                    if dataNameIn[j] == dataNameOut[i + h]:
                        tmpData = str(dataTimeInExit[j])[0:2]
                        if tmpData != "Пр":
                            if dataTimeOutExit[i + int(tmpData) - 1] is None:
                                sheetOut.cell(row=i + int(tmpData), column=9).value = dataTimeInExit[j]
                            else:
                                if (str(dataTimeInExit[j])[:10] == str(dataTimeOutExit[i + int(tmpData) - 1])[
                                                                   :10]) and (
                                        str(dataTimeInExit[j])[11:] > str(dataTimeOutExit[i + int(tmpData) - 1])[11:]):
                                    sheetOut.cell(row=i + int(tmpData), column=9).value = dataTimeInExit[j]
                        else:
                            sheetOut.cell(row=i + int(str(dataTimeIn[j][0:2])), column=9).value = dataTimeInExit[j]
            i += oneSecondName + 1
    print("Время выхода поменялось!")
    wbOut.save(filename=nameOfOutFile)
