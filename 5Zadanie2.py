# Задание №2
# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? 
# Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв 
# Если какой-то из перечисленных букв нет - Выведите False
slovo = input()
a = slovo.count('a')
e = slovo.count('e')
i = slovo.count('i')
o = slovo.count('o')
u = slovo.count('u')
Glas = a + e + i + o + u
Soglas = len(slovo) - Glas
print("Гласных:", Glas)
print("Согласных:", Soglas)
if a > 0:
    print("a: ", a)
else:
    print("a: False")
if e > 0:
    print("e: ", e)
else:
    print("e: False")
if i > 0:
    print("i: ", i)
else:
    print("i: False")
if o > 0:
    print("o: ", o)
else:
    print("o: False")
if u > 0:
    print("u: ", u)
else:
    print("u: False")