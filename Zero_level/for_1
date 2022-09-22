#
# def scheta():
#
#     debet = [2000, 1000, 3000, 40000]
#     kredit = [ -1000, -2000, -3000, -200, -300]
#     debit_credit_all ={}
#     for scheta_d, scheta_c in zip (debet, kredit) :
#         print(scheta_d, scheta_c)
#         debit_credit_all[scheta_d] = scheta_c
#         print(debit_credit_all)
#
# scheta()


#Пример с фиклом фор для составления  словарей пар ключ значения из двух списков. Нужная штука
# для начал делаем функцию 0 учись делать функции чтобы потом их можно было вызывать где нибудь
#
# def mainCarsMen () -> None:
#
#     cars = ["bmw", "volvo", "citroen", "lada", "mercedes"]
#     men = ["Anjey", "Vova", "Max", "Fedor", "John", "Lox"] # Lox  бех машины потому что пары не хватило
#     Cars_owners = dict(zip(cars,men))
#     print(Cars_owners)
#
# mainCarsMen()


#Как сделать так же только с циклом фор длинный путь

# def mainCarsMen () -> None:
#
#     cars = ["bmw", "volvo", "citroen", "lada", "mercedes"]
#     men = ["Anjey", "Vova", "Max", "Fedor", "John", "Lox"] # Lox  бех машины потому что пары не хватило
#     Cars_owners ={} # инициализируем дикт
#     for c,m in zip (cars, men):
#         Cars_owners[c]=m # Дичь непонятно почему мы присваиваем так c  это карс в квадратныъ скобках равно m
#
#     print(Cars_owners)
#
# mainCarsMen()
# сам придумал и решил задачу со счетами Я БУДУ программистом!!!!!!
# def scheta_sort():
#     debetSaldo =0
#     creditSaldo =0
#     dohuya_platezhek = [2000, 1000, 3000, 4000, -1000, -2000, -3000, -200, -300]
#
#     for platezhka in dohuya_platezhek:
#        if platezhka < 0:
#            creditSaldo=creditSaldo+platezhka
#        elif  platezhka > 0:
#            debetSaldo =debetSaldo+platezhka
#     print(debetSaldo)
#     print(creditSaldo)
#
# scheta_sort()

# делаем словарь из двух списков
def scheta_dict_zip():
    dolzhniki = ["Anjey", "Vova", "Max", "Fedor", "John", "Lox", "Sergey", "Misha", "los"]
    dohuya_platezhek = [2000, 1000, 3000, 4000, -1000, -2000, -3000, -200, -300]

    dolzhnik_scheta =dict(zip(dolzhniki,dohuya_platezhek))
    #print(dolzhnik_scheta)
    #Чтобы вевести все имена и все числа друг за жругом то есть сначала все ключи а потом все значения берем два списка for
    for name, numbers in dolzhnik_scheta.items():
        print(name)
    for name, numbers in dolzhnik_scheta.items(): #тут для того чтобы вывести только значения пишем items  и выврдим только числа
        print( numbers)



    # Можно взять и сложить все значения цифровые если они инт или флоат в цикле
    summ_numbers = 0
    for name, numbers in dolzhnik_scheta.items():
        summ_numbers = summ_numbers+numbers
    print(f" сумма по должникам {summ_numbers}")
    #суммируем положительные и отрицательные числа
    otric_chisla =0
    polozh_chisla =0
    for name, numbers in dolzhnik_scheta.items():
        if numbers > 0:
            polozh_chisla =polozh_chisla+numbers
        else:
            otric_chisla = otric_chisla+numbers
    print(f"сумма отрицательных чисел: {otric_chisla}", f"сумма положительных чисел: {polozh_chisla}" )

    # а если я хочу взять среднее арифматическое когда нужно все сложить и поделить на количество
    otric_chisla = 0
    polozh_chisla = 0
    for name, numbers in dolzhnik_scheta.items():
        if numbers > 0:
            polozh_chisla = (polozh_chisla + numbers)/numbers
        else:
            otric_chisla = (otric_chisla + numbers)/numbers
    print(f"среднее арифм отрицательных чисел: {otric_chisla}", f" среднее арифмет положительных чисел: {polozh_chisla}")




#Обращение к словарю по ключу
    print(dolzhnik_scheta["Anjey"])
    input_1 =str(input("Введит кто он еще кроме хуйло"))
    # обращение к словарю и добавленеи нового ключа и значения то есть пары
    #обращаемся к ключу в квадратных скобках пишем новый ключ и присваеваем ему значение, ключ неизменяемый должен быть
    dolzhnik_scheta['Путин'] = "Хуйло" # тут добавили новый ключи и значение
    print(dolzhnik_scheta)
    dolzhnik_scheta['Путин'] = input_1 # вот тут на лету инпутом преписали значение ключа с инпутом
    print(dolzhnik_scheta)

    for value in dolzhnik_scheta.values():
        print(value)

    for keys in dolzhnik_scheta.keys():
        print(keys)

    while name  in dolzhnik_scheta =="Vova":
        print (name)
        break



scheta_dict_zip()










