numbers =[1,2,3,4,8,0,4,6] # берем и пишем список
print(numbers)

for number in numbers:  # вместо i пиши читабельное
    print(number)  # сюда переменные


  # цикл для квадратов

for kvadrats in numbers:  # заметь похуй что я писал до
                        # эттго numbers мне нужны квадраты - бери квадарты и умножай на квадарты
    print (kvadrats*kvadrats)

for del_na_dva in numbers:
    print(del_na_dva/2)

#range

numbers = range(1,5) # взяли подрезали список рэнджем а потом выводм через цикл
for number in numbers:
    print(number)


for number in range (1,101):
    print(number)


# то что мозг выедало - вот пример для числа в рэндже от 1,6: если число
# делится на 2 и результат == нулю (равен тру) то печатаем число четное, иначе число нечетное
# все гениальное просто


for number in range (1,6):
    if number %2 == 0:
        print ('число', {number}, 'четное')
    else:
        print ('число', {number}, 'нечетное')


name = "Ashykhmin"
for eachletter in name:
    print (eachletter)

for _ in range (5):
     print ('Alarm!!')


from collections import namedtuple
Slut = namedtuple('Slut', 'name age cost')

Sluts = [Slut('Эвелина', 22, 200), Slut('Снежанна', 18, 300), Slut('Виолетта', 35, 100)]


for whore in Sluts:
    print(whore)

persons =[('Zhanna', 23),('Mia', 26), ('Anna', 39) ]
print(len(persons))

for slut_name in persons:
    print (slut_name)

# tupleunpacking

for (name, age) in persons:
    print(name, age)


#количество звездочек  через перенос строки думал а тут проще
rows =int(input('Введи количество звездочек :'))
for stars in range (rows):
    print('*' *  (stars +1))

#чЕТНОЕ НЕЧЕТНОЕ СУКА ТАК И НЕ ПОНЯЛ
limit=int(input('Введи лимито символов :'))
for x in range (limit +1):
    if x  %2 ==0:
        print({x}, 'Четное')
    else:
        print({x}, ' Не четное')

#тут вообще ничего не понял
limit=int(input('Введи лимито символов  для деления на 3 и на 5 :'))

total_sum =0
for x in range (limit +1):
    if x % 3 == 0 or x % 5 ==0:
        total_sum +=x
    else:
        continue
    print ("total sum =" , {total_sum} )

#через лист компрехеншен

limit=int(input('Введи лимито символов  для деления на 3 и на 5 :'))
total_sum =sum([x for x in range(limit +1) if x %3 ==0 or x %5 ==0])
print(total_sum)


