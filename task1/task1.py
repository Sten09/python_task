#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#*Пример:*

#- 6 -> да
#- 7 -> да
#- 1 -> нет

n = int(input("Ведеите день недели: "))
if n < 1 or n > 7:
    print("Вы ввели не корректный день")
elif n >= 1 and n <= 5:
    print (n, "это будни")
else:
    print(n, "это выходной")


