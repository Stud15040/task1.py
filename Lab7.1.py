import math
def T(a,b,c): 
    p=(a+b+c)/2
    s=math.sqrt((p*(p-a)*(p-b)*(p-c)))
    return s
def P(a,b):
     s=a*b
     return s
def C(r):
     s=math.pi*(r**2)
     return s
tip=str(input("Введите название фигуры = "))
if tip=="треугольник":
    a=float(input("Введите сторону a = "))
    b=float(input("Введите сторону b = "))
    c=float(input("Введите сторону c = "))
    print (T(a,b,c))
elif tip=="прямоугольник":
    a=float(input("Введите сторону a = "))
    b=float(input("Введите сторону b = "))
    print(P(a,b))
elif tip=="круг":
    r=float(input("Введите радиус r = "))
    print(C(r))
input ('Нажмите Enter для выхода')
