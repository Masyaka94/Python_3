# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

n = int(input("Введите число n: "))
list = []
multipl = []
for i in range (1,n+1):
    list.append(i)
print(list)
if len(list) % 2 !=0:
   for i in range(0, len(list)//2+1):
       multipl.append(list[i]*list[len(list)-i-1])
elif len(list) % 2 ==0:
    for i in range(0, len(list)//2):
       multipl.append(list[i]*list[len(list)-i-1])
print(multipl)