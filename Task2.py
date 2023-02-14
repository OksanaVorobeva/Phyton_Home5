#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

numberA=int(input("Введите целое число A: "))
numberB=int(input("Введите целое число A: "))
sum=0
def summa (numberA,numberB):
    if numberB == 0:
        return numberA
    else:
        if numberB>0:
            return summa(numberA+1,numberB-1)
        else:
            return summa(numberA-1,numberB+1)
print(summa(numberA,numberB))