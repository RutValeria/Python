# Урок 2 Установка VS и Python
# тут я 
# print(7)

# Урок 3 Ввод-вывод и базовые переменные
# a = 3 + 5
# b = 3 - 5
# c = 5 / 2
# d = 5 // 2
# e = 3 * 4
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# Урок 4 Float, int и арифметические операции
# a = 5
# a += 10
# print(a)
# a = int(input())
# b = int(input())
# print(a * b)
# a, b, c = map(int, input().split())
# print(a * 2)
# a, b = map(int, input().split())
# c = a + b
# print(c)
# a = 10
# b = 3
# print(a / b * 3)
# print(float(input()))

# Урок 5 Логические и условные операторы
# a = 5
# b = 7
# print(a < b)
# a = int(input())
# b = int(input())
# if a < b:
#     print("Yes")
# else:
#     if a == b:
#         print("Maybe")
#     else:
#         print("No")
# a = int(input())
# if a <= 2:
#     print(1)
# elif a <= 4:
#     print(2)
# elif a <= 5:
#     print(3)
# else:
#     print(4)
# cash = int(input())
# cost = int(input())
# cassa = int(input())
# if (cash >= cost) and ((cash - cost) <= cassa):
#     print("Кола наша")
# else:
#     print("В этот раз на воде держимся")
# cash = int(input())
# cola = int(input())
# baykal = int(input())
# if (cola <= cash) or (baykal <= cash):
#     print("Купили")
# else:
#     print("Не повезло, не фортануло(")
# cash = int(input())
# mac = int(input())
# if not cash >= mac:
#     print("Сорян")

# Урок 6 Циклы While и For
# a = int(input())
# cnt = 0
# while a >= 0:
#     a -= 2
#     cnt += 1
#     print(cnt)

# a = int(input())
# cnt = 0
# while a > 0:
#     a -= 2
#     print(a)

# clients = int(input())
# cola = int(input())
# cnt = 0
# while (clients > 0) and (cola >= 0):
#     cans = int(input())
#     clients -= 1
#     if cola >= cans:
#         cnt += 1
#         cola -= cans
# print(cnt)

# for i in range(1, 11):
#     print(i)

# a = int(input())
# b = int(input())
# for i in range(a, b, 2):
#     print(i)

# a = int(input())
# b = int(input())
# for i in range(b, a - 1, -1):
#     print(i)

# for i in range(3, 10):
#     print(i)

# a = 1
# while a < 5:
#     a += 1
#     print(a)
# else:
#     print("Чебурек")

# a = 1
# while a < 5:
#     a += 1
#     print(a)
#     print("Чебурек")

# n = int(input())
# for i in range(n):
#     salary = int(input())
#     if salary % 2 == 0:
#         print(i + 1, "fired")

# Урок 7 Строки
# tmp = 'abcdef'
# print(tmp[-1])

# s1 = 'abcdef'
# s2 = 'abcd'
# s3 = s1 + s2
# print(s3)

# s1 = 'abcdef'
# print(len(s1))

# s1 = 'abcdefghijk'
# print(s1[0:5:2])

# s1 = 'abcdefghijk'
# print(s1[5::1])

# s1 = 'abcdefghijk'
# print(s1[:5])

# s1 = 'abcdefghijk'
# print(s1[3:])

# tmp = [4, 3, 2, 9, 7]
# t2 = tmp[::2]
# print(t2)

# tmp = "3 + 8 + 9 + 10"
# t = tmp.split(' + ')
# print(t)

# tmp = ['3', '4', '9', '157']
# print(' + ' .join(tmp))

# name = input()
# test = f"Hello, {name}"
# print(test)

# a1 = input()
# a2 = input()
# res = f'{a1} + {a2} = love'
# print(res)

# s1 = "asasddasadsasdhgajs"
# print(s1.upper())

# s1 = "SAGFASGAJSGJHKLASGHKJ"
# print(s1.lower())

# print(chr(97))

# print(ord('a'))

# t = 'abzr'
# for c in t:
#     code = ord(c) + 3
#     if code > 122:
#         print(chr(97 + code - 122), end="")
#     else:
#         print(chr(code), end="")

#Урок 8 Списки
# a = [3, 4, -150, 1, 2]
# # 3, 4, -150, 1, 2
# # 0, 1, 2, 3, 4, 5 index
# print(a[-10])

# a = [3, 4, -150, 1, 2]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# a[1] = 10
# print(a[1])

# a = [3, 4, -150, 1, 2]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# a.append(190)
# print(a[-1])

# a = [3, 4, -150, 1, 2]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# a.append(7)
# print(len(a))

# a = [3, 4, -150, 1, 2]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# print(*a)

# a = [3, 4, -150, 1, 2]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# a.insert(3, 99)
# print(*a)

# a = [3, 4, -150, 1, 2]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# a.pop(2)
# print(*a)

# a = [3, 4, -150, 1, 2]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# a.clear()
# print(*a)

# a = [3, 4, -150, 1, 2]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# a.reverse()
# print(*a)

# a = [3, 4, -150, 1, 2, 4, 9, 4]
# 3, 4, -150, 1, 2
# 0, 1, 2, 3, 4, 5 index
# print(a.count(4))

# n = int(input())
# res = []
# for i in range(n):
#     a = int(input())
#     res.append(a)
# print(res)

# res = list(map(int, input().split()))
# print(res)

# 10 50 50 100 500 50 1000 - что вводим
# 10 100 500 1000 - что должны увидеть
# n = int(input())
# tmp = list(map(int, input().split()))
# res = []
# for i in range(0, len(tmp)):
#     if tmp[i] != 50:
#         res.append(tmp[i])
# print(res)

# tmp = [1, 4, 3, 5]
# for i in tmp:
#     print(i)

# a = [3 for i in range(10)]
# print(a)
# print(len(a))

# a = 5
# b = a
# a += 1
# print(b)

# a = [5]
# b = a
# a[0] = 3
# print(b)

#Урок 9 Множества
# tmp = set()
# tmp2 = {2, 3, 3, 4}
# print(tmp2)

# tmp = {2, 3, 3, 4}
# tmp.add(7)
# print(tmp)

# tmp = {2, 3, 3, 4}
# tmp.add(7)
# tmp.discard(3)
# print(tmp)

# n = int(input())
# used = set()
# for i in range(n):
#     promo = input()
#     if promo in used:
#         print("Sorry, already used")
#     else:
#         used.add(promo)
# print(len(used))

# tmp = {1, 2, 3, 4, 5}
# tmp.clear()
# print(tmp)

# c1 = int(input())
# cl1 = []
# for i in range(c1):
#     name = input()
#     cl1.append(name)
# uc1 = set(cl1)

# c2 = int(input())
# cl2 = []
# for i in range(c2):
#     name = input()
#     cl2.append(name)
# uc2 = set(cl2)

# print(uc1.union(uc2))

# c1 = int(input())
# cl1 = []
# for i in range(c1):
#     name = input()
#     cl1.append(name)
# uc1 = set(cl1)

# c2 = int(input())
# cl2 = []
# for i in range(c2):
#     name = input()
#     cl2.append(name)
# uc2 = set(cl2)

# print(uc1.intersection(uc2))

# s1 = set()
# s2 = s1
# s2.add(7)
# print(s1)

# s1 = frozenset()
# s2 = s1
# s2.add(7)

# tmp = {1, 2, 3, 9, 0}
# for el in tmp:
#     print(el)

#Урок 10 Словари
# bank = {'anton': 10, 'dima': 20, 'petya': 4}
# print(bank['anton'])

# bank = {'anton': 10, 'dima': 20, 'petya': 4}
# bank['anton'] = 159
# print(bank['anton'])

# bank = {'anton': 10, 'dima': 20, 'petya': 4, 'anton': 15}
# print(bank)

# bank = dict()
# n = int(input())
# for i in range(n):
#     req = input()
#     if req == "create":
#         k = input()
#         bank[k] = 0
#     elif req == "add":
#         k = input()
#         amount = int(input())
#         if k in bank.keys():
#             bank[k] += amount
#         else:
#             print("sorry, no such key")
#     else:
#         print("sorry, bad request")
# print(bank)

# tmp = {'k1': 1, 'k2': 10, 'qwerty': 5}
# print(tmp.keys())
# print(tmp.values())
# print(tmp.items())

# tmp = {'k1': 1, 'k2': 10, 'qwerty': 5}

# for k in tmp.values():
#     print(k)

# tmp = {'k1': 1, 'k2': 10, 'qwerty': 5}
# tmp.pop('k1')
# print(tmp)

# tmp = {1.5: 1, 10.4: 10, 20.9: 5}
# print(tmp.keys())

#Урок 11 Функции
# def chet(a):
#     if a % 2 == 0:
#         return True
#     a += 2
#     print(a)
# print(chet(5))

# def chet(a):
#     if a % 2 == 0:
#         return True
#     return False
# print(chet(5))
# print(chet(4))

# def tmp(name):
#     print(f'Hello, {name}')

# tmp('MARK')

# def vis(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     return False
# y = int(input())
# print(vis(y))

# def nechet(n):
#     return (n % 2 != 0)

# def res(l):
#     for el in l:
#         if nechet(el):
#             print(el)

# tmp = [1, 3, 4, 9, 2, 7]
# res(tmp)

# def new_year():
#     print('Happy New Year!')

# def birthday():
#     print('Tell us the name of a person')
#     name = input()
#     print(f'Happy Birthday, {name}!')

# def mart8():
#     print('Happy 8th of March')

# n = int(input())
# for i in range(n):
#     cm = input()
#     if cm == 'new year':
#         new_year()
#     elif cm == 'birthday':
#         birthday()
#     elif cm == '8 march':
#         mart8()
#     else:
#         print("wrong command")

#Урок 12 Сортировки
# a = [4, 9, 0, 17, 23, 4, 1, 0]

# c1 = 3
# c2 = 4
# c3 = 5

# c1, c2, c3 = c2, c3, c1
# print(c1, c2, c3)


# a = [4, 9, 0, 17, 23, 4, 1, 0]

# a[0], a[2] = a[2], a[0]

# print(a[0], a[2])


# a = [4, 9, 0, 17, 23, 4, 1, 0]
# n = len(a)

# for i in range(n):
#     for j in range(n - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]

# print(*a)


# a = [4, 9, 0, 17, 23, 4, 1, 0]

# a.sort()

# print(a)


# def cmp(x):
#     return x % 10

# a = [4, 9, 0, 17, 23, 4, 1, 0]

# a.sort(key=cmp)
# print(a)


# n = 5
# sph = [12, 30, 97, 5, 6]
# hs = [10, 120, 4, 8, 9]

# res = []
# for i in range(n):
#     r = sph[i] * hs[i]
#     res.append(r)

# res.sort()
# print(res)


# def cmp(x):
#     return (x // 10) * (x % 10)

# tmp = [12, 34, 35, 12, 68, 29]

# tmp.sort(key=cmp)

# print(tmp)


# a = 5
# b = 8
# c = 1
# d = -19

# print(max(a, b, c, d))

# a = 5
# b = 8
# c = 1
# d = -19

# print(min(a, b, c, d))

# tmp = [1, 4, -19, 30, 56]
# print(max(tmp))

# tmp = [1, 4, -19, 30, 56]
# print(min(tmp))


# a = (2, 4, 9, 7, 2)
# print(len(a))
# print(a.count(2))
# print(a)


# poets = [('Ptushkin', 1203, 1299), ('Cheburashkin', 999, 1201), ('Petrogradskiy', 1931, 1956)]
# poets[0][1] = 1204

# print(poets)


# poets = [('Ptushkin', 1203, 1299), ('Cheburashkin', 999, 1201), ('Petrogradskiy', 1931, 1956)]
# poets[0] = ('Ptushkin', 1204, 1299)
# print(poets)

#Урок 13 Двумерные списки
# tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]
# # 0 [1, 2, 3]
# # 1 [4, 5]
# # 2 [9, 8, 7]

# print(tmp[1][0])


# tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]

# print(tmp[1][0])

# tmp[1][0] = 9
# tmp[1] = [4, 9, 0, 3]
# print(tmp[1])

# tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]
# tmp.append([6, 9, 2])
# for i in tmp:
#     print(*i)


# def pl(t):
#     for i in t:
#         print(*i)
        
# n = int(input())
# tmp = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     tmp.append(a)

# pl(tmp)


# def pl(t):
#     for i in t:
#         print(*i)

# tmp = [[1 for i in range(7)] for i in range(5)]
# pl(tmp)


# def pl(t):
#     for i in t:
#         print(*i)

# x = int(input())
# y = int(input())

# house = [[0 for i in range(y)] for i in range(x)]
# cnt = 1

# for i in range(-1, -x - 1, -1):
#     print(i)

# def pl(t):
#     for i in t:
#         print(*i)

# x = int(input())
# y = int(input())

# house = [[0 for i in range(y)] for i in range(x)]
# cnt = 1

# for i in range(-1, -x - 1, -1):
#     if i % 2 == 1:
#         for j in range(y):
#             house[i][j] = cnt
#             cnt += 1
#     else:
#         for j in range(-1, -y - 1, -1):
#             house[i][j] = cnt
#             cnt += 1

# pl(house)


# def pl(t):
#     for i in t:
#         print(*i)

# t3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# print(t3[0][0][1])

#Урок 14 Рекурсия
# def test(a, b, c = 8):
#     return a + b + c

# d = test(3, 4, 9)
# print(d)


# def test(a, b, c):
#     return a + b + c

# d = test(3, 8, 10)
# print(d)


# def tmp():
#     return 1

# a = tmp() + tmp()
# print(a)


# def tmp(x):
#     if x < 0:
#         return
#     print(x)
#     tmp(x - 1)

# n = int(input())
# tmp(n)


# def tmp(x):
#     if x < 0:
#         return
#     tmp(x - 1)
#     print(x)
    
# n = int(input())
# tmp(n)


# 0 1 1 2 3 5 8 13 ...

# def fib(n):
#     if n < 0:
#         return 0
#     res = fib(n - 1) + fib(n - 2)
#     return res

# x = 2
# print(fib(x))


# def fib(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     res = fib(n - 1) + fib(n - 2)
#     return res

# x = 6
# print(fib(x))

# import sys

# def tmp(n):
#     if n < 0:
#         return
#     print(n)
#     tmp(n - 1)

# sys.setrecursionlimit(5000)
    
# tmp(2000)

#Урок 15 ООП
# class Human(object):
#     name = "Ivan"
#     height = 175
#     age = 25

# default_human = Human()
# default_human.name = "Anton"
# print(default_human.name)



# class Human(object):
#     name = "Ivan"
#     height = 175
#     age = 25

#     def __init__(self, n, h, a):
#         self.name = n
#         self.height = h
#         self.age = a


# h1 = Human("Anton", 120, 12)
# h2 = Human("Dima", 190, 23)

# print(h1.name)
# print(h2.name)



# class Human(object):
#     name = "Ivan"
#     height = 175
#     age = 25

#     def __init__(self, n, h, a):
#         self.name = n
#         self.height = h
#         self.age = a

#     def privet(self):
#         print(f"My name is {self.name}, my age is {self.age}")


#     def get_older(self):
#         self.age += 5


#     def goodbye(self):
#         print("Goodbye")


# h1 = Human("Anton", 120, 12)
# h2 = Human("Dima", 190, 23)

# h2.privet()
# print(h1.age)
# h1.get_older()
# h1.get_older()
# print(h1.age)
# h1.privet()
# h1.goodbye()

#Урок 16 Классы и объекты
# class Car(object):
#     brand = "Mazda"
#     max_speed = 100
#     color = "black"

#     def __init__(self, b, ms):
#         self.brand = b
#         self.max_speed = ms

#     def upgrade(self):
#         self.max_speed += 25

# class Truck(Car):
#     max_weight = 10

#     def __init__(self, b, ms, mw):
#         super().__init__(b, ms)
#         self.max_weight = mw

#     def add(self):
#         self.max_weight += 10

#     def upgrade(self):
#         self.max_speed += 15

# # mazda = Car("Mazda", 200)
# # mazda.upgrade()
# # print(mazda.max_speed)

# gazel = Truck("Gazel", 60, 120)
# print(gazel.brand, gazel.color, gazel.max_speed, gazel.max_weight)



# class Car(object):
#     brand = "Mazda"
#     max_speed = 100
#     color = "black"
#     disk_size = 25

#     def __init__(self, b, ms):
#         self.brand = b
#         self.max_speed = ms

#     def upgrade(self):
#         self.max_speed += 25

# tmp = Car("lada", 2)
# tmp.disk_size = 45
# print(tmp.disk_size)




# class Car(object):
#     brand = "Mazda"
#     max_speed = 100
#     color = "black"
#     __password = 1234

#     def __init__(self, b, ms):
#         self.brand = b
#         self.max_speed = ms

#     def __update_password(self):
#         self.__password = 234 

#     def upgrade(self):
#         self.max_speed += 25
#         self.__update_password()

#     def get_password(self):
#         return self.__password

# tmp = Car("Mazda", 3)
# print(tmp.get_password())
# tmp.upgrade()
# print(tmp.get_password())

#Урок 17 О-нотация
# t = [1, 2, 5]
# try:
#     print("TEST")
#     print(t[10])
#     # print(45 // 0)
# except ZeroDivisionError:
#     print("Ну не надо так, на ноль делить низя!")
# except IndexError:
#     print("Тут ничего нет, попробуйте другой индекс")
# except Exception:
#     print("abcd")
# else:
#     print("Все гуд")
# finally:
#     print("Finish")
# print("TEST")



# a = 1
# for i in range(100000000):
#     a += 1
# print(1)



# n = int(input())
# m = int(input())
# a = 1
# for i in range(n):
#     for j in range(n):
#         a += 1
# for k in range(100):
#     for j in range(m):
#         a += 1