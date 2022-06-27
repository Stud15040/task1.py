n = int((input("Введите N: ")))
arr = [int(input('Введите элемент массива: ')) for i in range(n)]
print('Вывод массив в обратном порядке',list(reversed(arr)))
print('Максимальный элемент массива',(max(arr)))
