# Задание №1
# Сначала вводится число N, затем вводится ровно N целых чисел. 
# Подсчитайте, сколько из них равны нулю, и выведите это количество.
Chislo = int(input())
Nol = 0
for i in range(Chislo):
    Celoe = int(input())
    if (Celoe == 0):
        Nol += 1
print(Nol)

