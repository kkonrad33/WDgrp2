#1
# liczby = [1,2,3,4,5,6,7,8,9,10]
# zbior1 = [1-x for x in liczby]
# print(zbior1)
#
# zbior2 = [4**y for y in range(8)]
# print(zbior2)
#
# zbior3 = [z for z in zbior2 if z % 2 == 0]
# print(zbior3)
#2
# import random
# losowe = []
# for x in range(9):
#     losowe.append(random.randint(1, 30))
# print(losowe)
# parzyste = [x for x in losowe if x % 2 == 0]
# print(parzyste)
#3
# produkty = {"jajka": "sztuki", "mąka": "kg", "cukier": "kg", "jabłka": "sztuki"}
# sztuki = [keys for keys, values in produkty.items() if values == "sztuki"]
# print(produkty)
# print(sztuki)

#4
# def pitagoras(a, b, c):
#     boki = a**2 + b**2
#     przeciw = c**2
#     if boki == przeciw:
#         print("Trójkąt o bokach", a, b, c, "jest prostokątny.")
#         return 1
#     else:
#         print("Trójkąt o bokach", a, b, c, "nie jest prostokątny.")
#         return 0
# print(pitagoras(3,4,5))
# print(pitagoras(2,4,5))

#5
# def trapez(a=2, b=4, h=3):
#     pole = ((a+b)*h)/2
#     print("Pole trapezu: ")
#     return pole
# print(trapez())

#6
# def ciag(a1=1, b=4, ile=10):
#     for i in range(ile):
#         a1 *= b
#     return a1
# print(ciag())

#7
# def ciag2(a1=1, b=4, ile=10):
#     a1 = (a1*b)**ile
#     return a1
# print(ciag2())

#8
# zakupy = {"jajka": 12, "chleb": 3, "makaron": 7}
# def lista(a):
#     b = 0
#     c = 0
#     for x in a.values():
#         b = b + x
#         c += 1
#     print('Wartość zakupów to', b, "zł.\nWszyskich produktów jest: ")
#     return c
# print(lista(zakupy))

#9
from ciagi import arytmetyczne
from ciagi import geometryczne



