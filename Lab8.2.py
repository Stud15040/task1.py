N = int(input('Ввод N: '))
M = int(input('Ввод M: '))
B = []
#ввод массива
for i in range (N):
    a = []
    for j in range(M):
        print('Введите [',i,',',j,'] элемент')
        a.append(int(input()))
    B.append(a)
#вывод массива
for i in range (N):
    for j in range(M):
        print(B[i][j], end=' ')
    print()
#обмен макс. и мин.элементы с первым и последним элементами строки
for x in range(len(B)) :
    idx = B[x].index(max(B[x]))
    B[x][idx], B[x][0] = B[x][0], B[x][idx]
    idx = B[x].index(min(B[x]))
    B[x][idx], B[x][-1] = B[x][-1], B[x][idx]
#вывод измененного массива
print ('Вывод измененного массива')
for i in range (N):
    for j in range(M):
        print(B[i][j], end=' ')
    print()
input ('Нажмите Enter для выхода')
