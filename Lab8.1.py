import random
pol = 0
s = 0
N = int(input('Ввод N: '))
A = []
#ввод массива
for i in range (N):
    b = []
    for j in range(N):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    A.append(b)
#вывод массива
for i in range (N):
    for j in range(N):
        print(A[i][j], end=' ')
    print()
#вычисление суммы и числа положительных элементов над главной диагонолью 
for i in range(N):
    for j in range(i+1, N):
        if A[i][j] <= 0:
           continue
        if A[i][j] > 0:
            pol += 1
            s += A[i][j]

print('Сумма:', s)
print('Число:', pol)
input ('Нажмите Enter для выхода')
