#tuple или кортеж как список только не изменяется
# и скобки вместо квадратные круглые
#внутри может писать всюхурму как и в списке только поменять не можем
# после последнего элемента списка в кортеже нужно поставить ЗАПЯТУю

kortezh =(1,3,'Пися', 0,) # нужно чтобы была запятая в списке в конце так и понятнее что это кортеж и пайтон
                         # не будет думать что это говно какое то
                          # проверить тип можно через type
print(kortezh)

print (type(kortezh))
kortezh =(1,3,0)
print (type(kortezh))

list(kortezh)
print(kortezh)
print(type(kortezh))

person =('lohn', 'Silver', '22')
print(type(person))

print(len(person)) #len  длину списка можно посмотреть  напишь 3 элеметна
print(person[-1]) # -1 это кога индекс с кона надо достать

# это именованные туплы прикольная херня
# вот например список проституток сначала надо подключть named туплы
# а потом уже можно чудить классы контейнеры данных - отличное же named tuple  запомни

from collections import namedtuple
Slut = namedtuple('Slut', 'name age cost')

Sluts = [Slut('Эвелина', 22, 200), Slut('Снежанна', 18, 300), Slut('Виолетта', 35, 100)]
print (Sluts[0])

print (Sluts[0].name)
print (Sluts[0].age)
print (Sluts[2].name)

