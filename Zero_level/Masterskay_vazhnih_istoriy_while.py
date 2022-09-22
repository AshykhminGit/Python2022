import datetime
poem = "Буря мглою небо кроет, Вихри нежные крутя, баранкин будь человеком"

print(len(poem))

poem_len = len(poem)
print (poem_len)
index =0

letter  = "б"
while index != poem_len:
    print(index, poem[index])
    index+=1 #index = index+1
    if poem[index] == letter:
        print(f" Я нашел букву {letter} в {index}")



# d = datetime.date(2022,4,25)
# print(d.year)
# print(datetime.date.today())



