#определение функции вычисления
def Resultat(massiv):
    s=sum(massiv)
    sr=s/len(massiv)
    return print ('Сумма элементов массива',s, ', Cреднеарифметическое значение ',sr)

#определение функции для ввода элементов массива
def Vvod():
    n = int((input("Введите размерность массива: ")))
    if n<=15:
        arr = [int(input('Введите элемент массива: ')) for i in range(n)]
        Resultat(arr)
    else:
        input("Размерность массива не должна превышать 15 элементов")
        Vvod()
    
#основная программа
Vvod()
Vvod()
Vvod()
input ('Нажмите Enter для выхода')
