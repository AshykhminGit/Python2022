import random as r
hp =0

def meetRareFree (): # функция магазина это потом можно будет разнести по файлам и классам
    global hp
    global coins
    global damage




    print ("Ты набрел на сундук с сокровищами")

    while input("Будешь пробовать вскрыть? да/нет?").lower() == "1":
        print("Ну давай попробуем")
        brosok = r.randint(0, 1)
        if brosok == 0:
            print(" Выпало", brosok, "Не открылся пробуем еще раз?")

        elif brosok == 1:
            print("Ты открыл замок")

            hp += brosok
            print("Ты получил прибавление к здоровью", hp)

        else:
            print("Ну не хочешь как хочешь")
            break




meetRareFree()
