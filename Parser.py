import array

print(
    "Программа сканирует файл file.csv в папке запуска скрипта, сканирует каждую строку и выводит отсутствующие значения согласно введенных крайних номеров")


def start_end():
    first = input("Отсчет ОТ #: ")
    last = input("Отсчет ДО #: ")
    i = int(first)
    j = int(last)
    # i = 0
    num = array.array('i', [])
    while i < j:
        num.append(i)
        i += 1
        # print(num)
    return num


def parseFile():
    with open("file.csv") as fp: #you can replace file.csv 
        File = fp.readlines()
        count = 0
        # print(start_end())
        arrayList = start_end()
        # print(arrayList)
        for everyLine in File:  # parse csv file STR into INT and remove from array
            try:
                count += 1
                nextI = int(everyLine.format(count, everyLine.strip()))
                # print(nextI)
                try:
                    arrayList.remove(nextI)
                    # print(arrayList)
                except ValueError:
                    continue
            except ValueError:
                continue
        # print(arrayList)
        return arrayList


def finish(a):
    x = 0
    # print(a)
    length = a.__len__()
    try:
        with open("output.csv", "w") as delete:
            delete.writelines("")
    except PermissionError:
        print("\n---- Нет доступа к записи файла. Возможно файл открыт ----\n")
        # print("\nГотово. Загляните в output.csv")
    else:
        while x < length:
            with open("output.csv", "a") as fileAppendData:
                fileAppendData.writelines("{}\n".format(arr[x]))
                # print("PPC :", arr[x])
                x += 1
                fileAppendData.close()
        print("\nГотово. Загляните в output.csv")


arr = parseFile()
finish(arr)
