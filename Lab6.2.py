n = int((input("Введите N: ")))
arr = [float(input('Введите элемент массива: ')) for i in range(n)]
average = sum(arr) / len(arr)
arr = [average if i == 0 else i for i in arr]
print(arr)
