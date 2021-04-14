import numpy as np
# zadanie 1

# czworki = np.arange(4, 81, 4)
# print(czworki)
# print(czworki.size)
# zadanie 2

# list = [1.2, 3.5, 6.1, 2.3]
# print(list)
# konwert = np.array(list, dtype='int64')
# print(konwert)
# print(konwert.dtype)

# zadanie 3


# def tablica(n):
#
#     tab = np.arange(1, n*n, 1)
#     print(tab)
#
#
# tablica(2)

# zadanie 4

# def potegi(n, m):
#
#     pow = np.logspace(n, n**m, m)
#     print(pow)
#
#
# potegi(2, 4)

# zadanie 5

# def wektor(leng):
#     wek = []
#     for x in range(leng):
#         wek.append(leng-x)
#     tab = np.diag([a for a in wek])
#     print(tab)
#
#
# wektor(5)
# wektor(10)

# zadanie 6

# slowo1 = 'dziobak'
# slowo2 = 'kot'
# slowo3 = 'krewetka'
#
# wykreslanka = np.array(list(slowo1))
# print(wykreslanka)

# zadanie 7

# zadanie 8

# def podzial(tab, kierunek):
#     rzedy, kolumny = tab.shape
#     if kierunek == "poziomo":
#         if kolumny % 2 == 0:
#             kolumny /= 2
#             kolumny = int(kolumny)
#             print(tab[:kolumny])
#             print(tab[kolumny:])
#         else:
#             print("liczba kolumn nie jest parzysta")
#
#     if kierunek == "pionowo":
#         if rzedy % 2 == 0:
#             rzedy /= 2
#             rzedy = int(rzedy)
#             print(tab[:, :rzedy])
#             print(tab[:, rzedy:])
#         else:
#             print("liczba rzędy nie jest parzysta")
#
# tablica = np.diag([a for a in range(6)])
# podzial(tablica, "poziomo")
# podzial(tablica, "pionowo")

# zadanie 9

ciag = np.zeros((5, 5), dtype=int)
y = 1
for x in range(25):
    y += 2
    ciag[x // 5][x % 5] = y



print(ciag)
