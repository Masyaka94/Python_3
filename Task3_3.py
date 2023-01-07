#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу
#между максимальным и минимальным значением дробной части элементов, отличной от 0.

list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)
help = []
for i in list:
    if i%1 != 0:
      help.append(round(i%1,3))
minimum = min(help)
maximum = max(help)
print(maximum-minimum)