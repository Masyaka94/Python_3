# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonachi(F):
    if F == 1 or F == -1:
        return 1
    elif F == 0:
        return 0
    else:
        if F > 0:
            return Fibonachi(F-1) + Fibonachi(F-2)
        elif F < 0:
            return Fibonachi(F+2) - Fibonachi(F+1)

X = int(input("Введите число: "))
fib_numb = []
for i in range(-X,X+1):
    fib_numb.append(Fibonachi(i))
print(fib_numb)