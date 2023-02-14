#Напишите программу, которая на вход принимает два числа A и B,
#и возводит число А в целую степень B с помощью рекурсии. >

numberA=int(input("Введите целое число A: "))
numberB=int(input("Введите целое число A: "))

def exponention (numberA,numberB):
    if numberB == 1:
        return numberA
    return (numberA*exponention(numberA,numberB-1))
print(exponention(numberA,numberB))