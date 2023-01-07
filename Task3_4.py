#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

N = int(input("Введите число: "))
dvoich = []
while True:
    dvoich.append(N%2)
    N = N//2
    if N//2 == 0 and N != 1:
        break
dvoich.reverse()
print(dvoich)