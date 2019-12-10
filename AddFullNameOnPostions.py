import openpyxl


def AddName(nameOfOutFile, nameOfInFile):
    print("AddFullNameOnPositions")
    wbOut = openpyxl.load_workbook(filename=nameOfOutFile)
    sheetOut = wbOut['Лист1']
    sheetOut.delete_rows(1, 1)
    wbOut.save(filename=nameOfOutFile)
    dataOut = sheetOut.values
    dataOut = list(dataOut)

    i = 0
    dataFamily = []
    dataName = []
    dataMiddleName = []
    dataOtdel = []
    dataWork = []
    while i != sheetOut.max_row:
        dataFamily.append(dataOut[i][4])
        dataName.append(dataOut[i][5])
        dataMiddleName.append(dataOut[i][6])
        dataOtdel.append(dataOut[i][1])
        dataWork.append(dataOut[i][2])
        i += 1
    print(dataFamily)
    print(dataName)
    print(dataMiddleName)

    tmpDataFamily = dataFamily[0]
    tmpDataName = dataName[0]
    tmpDataMiddleName = dataMiddleName[0]
    tmpDataOtdel = dataOtdel[0]
    tmpDataWork = dataWork[0]
    pre_last_family = 0
    for i in range(1, len(dataFamily)):
        if dataFamily[i] is None:
            sheetOut.cell(row=i + 1, column=2).value = tmpDataOtdel
            sheetOut.cell(row=i + 1, column=3).value = tmpDataWork
            sheetOut.cell(row=i + 1, column=5).value = tmpDataFamily
            sheetOut.cell(row=i + 1, column=6).value = tmpDataName
            sheetOut.cell(row=i + 1, column=7).value = tmpDataMiddleName
        else:
            tmpDataOtdel = dataOtdel[i]
            tmpDataWork = dataWork[i]
            tmpDataFamily = dataFamily[i]
            tmpDataName = dataName[i]
            tmpDataMiddleName = dataMiddleName[i]
            pre_last_family = i
    wbOut.save(filename=nameOfOutFile)

    print(pre_last_family, "pre_last_family")

    oneBlock = 0
    k = 1
    while dataName[k] is None:
        oneBlock += 1
        k += 1
    print(oneBlock)

    for j in range(1, oneBlock + 1):
        sheetOut.cell(row=pre_last_family + j + 1, column=2).value = tmpDataOtdel
        sheetOut.cell(row=pre_last_family + j + 1, column=3).value = tmpDataWork
        sheetOut.cell(row=pre_last_family + j + 1, column=5).value = tmpDataFamily
        sheetOut.cell(row=pre_last_family + j + 1, column=6).value = tmpDataName
        sheetOut.cell(row=pre_last_family + j + 1, column=7).value = tmpDataMiddleName
    wbOut.save(filename=nameOfOutFile)

