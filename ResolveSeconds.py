import openpyxl


def ResolveSeconds(nameOfOutFile, nameOfInFile):
    wbOut = openpyxl.load_workbook(filename=nameOfOutFile)
    sheetOut = wbOut['Лист1']
    dataOut = sheetOut.values
    dataOut = list(dataOut)

    wbIn = openpyxl.load_workbook(filename=nameOfInFile)
    sheetIn = wbIn['Sheet']
    dataIn = sheetIn.values
    dataIn = list(dataIn)

    j = 0
    dataTimeOut = []
    dataTimeOutExit = []
    while j != sheetOut.max_row:
        dataTimeOut.append(dataOut[j][7])
        dataTimeOutExit.append(dataOut[j][8])
        j += 1
    print("YES")

    j = 0
    dataTimeIn = []
    dataTimeInExit = []
    while j != sheetIn.max_row:
        dataTimeIn.append(dataIn[j][5])
        dataTimeInExit.append(dataIn[j][6])
        j += 1

    # Перевод времени входа Ленинградка
    for t in range(0, len(dataTimeOut)):
        if dataTimeOut[t] is not None:
            tmpStr = str(dataTimeOut[t])
            year = tmpStr[:4]
            month = tmpStr[5:7]
            day = tmpStr[8:10]
            time = tmpStr[10:19]
            finalString = day + '.' + month + '.' + year + time
            dataTimeOut[t] = tmpStr
            sheetOut.cell(row=t + 1, column=8).value = finalString

    # Перевод времени выхода Ленинградка
    for t in range(0, len(dataTimeOutExit)):
        if dataTimeOutExit[t] is not None:
            tmpStr = str(dataTimeOutExit[t])
            year = tmpStr[:4]
            month = tmpStr[5:7]
            day = tmpStr[8:10]
            time = tmpStr[10:19]
            finalString = day + '.' + month + '.' + year + time
            dataTimeOutExit[t] = tmpStr
            sheetOut.cell(row=t + 1, column=9).value = finalString
    wbOut.save(filename=nameOfOutFile)

    # Перевод времени входа Аэродом
    for t in range(0, len(dataTimeIn)):
        if dataTimeIn[t] is not None and len(str(dataTimeIn[t])) == 18:
            tmpStr = str(dataTimeIn[t])
            day = tmpStr[:2]
            month = tmpStr[3:5]
            year = tmpStr[6:10]
            time = tmpStr[11:19]
            finalString = day + '.' + month + '.' + year + ' 0' + time
            dataTimeIn[t] = tmpStr
            sheetIn.cell(row=t + 1, column=6).value = finalString

    # Перевод времени выхода Аэродом
    for t in range(0, len(dataTimeInExit)):
        if dataTimeInExit[t] is not None and len(str(dataTimeInExit[t])) == 18:
            tmpStr = str(dataTimeInExit[t])
            day = tmpStr[:2]
            month = tmpStr[3:5]
            year = tmpStr[6:10]
            time = tmpStr[11:19]
            finalString = day + '.' + month + '.' + year + ' 0' + time
            dataTimeInExit[t] = tmpStr
            sheetIn.cell(row=t + 1, column=7).value = finalString
    wbIn.save(filename=nameOfInFile)

