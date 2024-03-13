import time

# console program budget!
menu = "1 - Баланс\n2 - Расходы\n3 - Доходы\n4 - Добавить расход" \
       "\n5 - Добавить доход\n6 - Выйти"

doxod = []
rasxod = []
balance = 0


def get_balance():
    sum_dox = sum(i[0] for i in doxod)
    sum_ras = sum(i[0] for i in rasxod)
    print("Сумма доходов - " + str(round(sum_dox, 2)))
    print("Сумма расходов - " + str(round(sum_ras, 2)))
    print("БАЛАНС - " + str(round(sum_dox - sum_ras, 2)))


def t(s):
    e = time.time()
    f = e - s
    print("Время операции:", f, "секунд")


def p(op):
    summa = float(input("Сумма: "))
    dis = input("Описание: ")
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    op.append([summa, dis, timestamp])
    save()


def save():
    with open("text.txt", "w") as file:
        file.write("Доходы:\n")
        for summa, dis, timestamp in doxod:
            file.write(str(summa) + " - " + dis + " - " + timestamp + "\n")
        file.write("\nРасходы:\n")
        for summa, dis, timestamp in rasxod:
            file.write(str(summa) + " - " + dis + " - " + timestamp + "\n")


def load():
    with open("text.txt", "r") as file:
        lines = file.readlines()
        if '\n' in lines:
            dx = lines[1:lines.index('\n', 1)]
            rx = lines[lines.index('\n', 1) + 1:]
            for line in dx:
                abc = line.strip().split(" - ")
                doxod.append([float(abc[0]), abc[1], abc[2]])
            for line in rx:
                abc = line.strip().split(" - ")
                rasxod.append([float(abc[0]), abc[1], abc[2]])
        else:
            pass


while True:
    print(menu)
    a = input("Сделай выбор: ")
    if a == "6":
        break
    elif a == "5":
        s = time.time()
        p(doxod)
        t(s)
    elif a == "3":
        s = time.time()
        if len(doxod) > 0:
            print("--Сумма-- --Описание-- --Дата--")
            for summa, dis, timestamp in doxod:
                print(summa, " ---- " + dis, " ---- ", timestamp)
        else:
            print("У вас еще нет операции по доходам!")
        t(s)
    elif a == "4":
        s = time.time()
        p(rasxod)
        t(s)
    elif a == "2":
        s = time.time()
        if len(rasxod) > 0:
            print("--Сумма-- --Описание-- --Дата--")
            for summa, dis, timestamp in rasxod:
                print(summa, " ---- " + dis, " ---- ", timestamp)
        else:
            print("У вас еще нет операции по расходам!")
        t(s)
    elif a == "1":
        s = time.time()
        print("Подождите идёт расчёт ваши доходов и расходов")
        time.sleep(2)
        get_balance()
        t(s)
