x, k, summ = 1, 0, -1
while x != 0:
    summ += x
    k += 1
    x = int(input("Введите последовательность чисел поэлементно: "))
print('Сумма: ', summ, 'Количество: ',k)
