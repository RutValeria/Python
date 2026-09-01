# Задание №3
# Два инвестора - Майкл и Иван хотят вложиться в стартап.
# Фаундеры сказали, что минимальная сумма инвестиций - X долларов,
# больше инвестировать можно сколько угодно. У Майкла A долларов,
# у Ивана B долларов. Если оба могут вложиться - выведите 2, если только Майкл - Mike,
# если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.
SumInvest = int(input())
Mike = int(input())
Ivan = int(input())
if (Mike >= SumInvest) and (Ivan >= SumInvest):
    print("2")
elif (Mike >= SumInvest) and (Ivan < SumInvest):
    print("Mike")
elif (Ivan >= SumInvest) and (Mike < SumInvest):
    print("Ivan")
elif ((Mike < SumInvest) or (Ivan < SumInvest)) and (Mike + Ivan >= SumInvest):
    print("1")
else:
    print("0")