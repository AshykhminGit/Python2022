import random as r #Вызвали нужную рандом функцию и переименовали ее в r
hp = 0  #Создали переменные с жизнями дамагом и монтеами вообще для всех
coins = 0
damage = 0


def printParameters():  #создали функцию с выводом параметров персонажа  позже ее можно вызвать
    print("У тебя {0}  жизней, {1} монет , и {2} урона.".format(hp, coins, damage))


def printHp():
    print(f" У тебя  {hp} Жизней")

def printCoins():
    print(f" У тебя   {hp} Жизней")


def printDamage():
    print(f"У тебя {damage} урона")



def meetMonster():
    global hp
    global coins
    global damage


    monsterLvl =r.randint(1,3)
    monsterHp = monsterLvl
    monsterDmg =monsterLvl *2 -1  #  с вычетом - 1 из уровня дамага можно и без этого

    monsters = ["Гуль", "Вампир", "Виверна", "Утопец", "Троль"]

    monster = r.choice(monsters)

    print("Ты  набрел на монстра  {0} у него  {1}  уровень {2}  жизней и {3}  урона ".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()
    # шанс свалить и выбор длраться или нет
    while monsterHp > 0:
        choice = input("Что будешь делать ведьмак? атака/бег?").lower()

        if choice == "атака":
            monsterHp-= damage  #  тут отнимаешт от жизни монстра наш дамаг
            print("Ты ударил монстра и у него осталось",monsterHp, "жизней")
        if choice == "бег":
            chance =r.randint(0, monsterLvl)
            if chance == 0:
                print("Тебе удалось сбежать!!!")
                break
            else:
                print("Монстр оказался сильнее и догнал тебя")
        else:
            continue

        #монстр дерется

        if monsterHp > 0:
            hp -= monsterDmg
            print("Монстр атаковал и у тебя осталось", hp, "жизней")

        if  hp <= 0:
            break
            print("Ты умер")
    else:
        loot = r.randint(0,2) + monsterLvl #  лутим в зависимости от монстра колияесвто денег

        coins += loot
        print("Ты убил его ведьмак" "Твоя награда ", loot, "монет")


def meetShop (): # функция магазина это потом можно будет разнести по файлам и классам
    global hp
    global coins
    global damage

    def buy (cost): # логика покупки если монт больше иоли равно стоимости кост? то сравниваем и вычитаем
        global coins  # делаем для того чтобы вывести доступ к функции наружу из функции
        if coins >= cost: # если монты больше или равно стоимости
            coins -= cost# то монеты мину стоимость - покупка
            printCoins()# печатаем сколько монет осталось
            return True# булево говоорим что это правильная ветка для покупки- покупка свершилась
        print("У тебя не хватает монет")
        return False

    weaponLvl = r.randint(1,3) # рандомный уровень оружия
    weaponDmg = r.randint(1,5) * weaponLvl #рандомный уровень дамага оружие  уноженный на лвл оружия

# список оружия создаем
    weapons = ["АК-47", "Ржавый меч", "лук", "лопата", " Палка-копалка"]
    weaponRarities = ["Испорченный", "Редкий", "Легендарный",]
    weaponRarity = weaponRarities[weaponLvl - 1] # вот тут пока не понял

    weaponCost =r.randint(3, 10) * weaponLvl     #Расчт стоимости от балды с помощью рандоминт

    weapon =r.choice(weapons) # выбор оружия от балды с помощью чойс от рэндом

    oneHpCost = 5 # Одно очко злоровья стоит 5 монет
    threeHpCost = 12 # три очка здлровья 12 монет - потом перепишу

    print("На пути тебе встретился торговец")
    printParameters()


    while input("Ты смотришь на магазин. Что ты будешь делать дальше? зайти? уйти?").lower() == "зайти":
        print(f" 1) Одна бутылка здоровья стоит {oneHpCost} монет ")
        print(f" 2) три  бутылки здоровья стоят {threeHpCost} монет ")
        print(" 3) {0} {1} - {2} монет".format(weaponRarity, weapon, weaponCost))

        choice = input("Что хочешь приобрести? 1 первое  или 2 второе  или 3 третье?")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
                print("Здоровье увеличилось!!!")
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
                print("ТЫ еще сильнее мой герой")
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg # не прибавляем к предыдущему дамага а типа заменяем дамаг на дамаг того оружия что купили
                printDamage()
                print("Пздравляю Меченый. новое пуляло")

        else:
            print("Я такое не продаю, извини")



















def InitGame (InitHp, InitCoins, InitDmg):
    global hp
    global coins
    global damage

    hp = InitHp
    coins = InitCoins
    damage = InitDmg
    print("Мы отправились в путешествие! ")
    printParameters() #  тут ты вызываешь функцию внутри функции  функцию с параметрами ты написал выше

def gameLoop():
    ''' Вот тут основаня движуха в игре '''
    situation = r.randint(0, 10)  # тут цикл самой игры? ходим бродим в рэндже случайных чисел ю выпало 0 - зашел магазин? выпало
    if situation == 0:            # выпало 1 - монстр другое - блуждаем? можно добавлять случаи
        meetShop() #  тут была вот такая заглушка  -  мы ее заменили на фукнцию мит шоп input("Shop")
    elif situation == 1:
        meetMonster()# Тут была заглушка  input("Monster") ее заменили на фукнцию ммит монстр
    else:
        input("Блуждаю...")


###########################А вот после этой строчки начинается инициализация фукнций? игра начинается тут

InitGame(100, 999, 10)
printHp()

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала ? Да?Нет").lower == "да":
            InitGame(100, 0, 10)
        else:
            break

printHp()




