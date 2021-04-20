import numpy as np
# Zadanie 1
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
# a = np.arange(3)
# b = np.array([4,5,6])
# c = a * b
# print(c)

# Zadanie 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
# a = np.arange(9).reshape(3,3)
# b = np.arange(16).reshape(4,4)
# print(a.min(axis=1))
# print(b.min(axis=1))
# print(a.min(axis=0))
# print(b.min(axis=0))

# Zadanie 3
# Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.
# a = np.arange(3)
# b = np.array([4,5,6])
# print(np.dot(a,b))

# Zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.
# a = np.arange(3, dtype='int32')
# b = np.linspace(2,7,3)
# c = a * b
# print(c)
# print(c.dtype)

# Zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.
# a = np.array([[4,5,2],[6,1,3]])
# b = np.cos(a)

# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
# b = np.array([[8,12,3],[1,4,22]])
# b = np.cos(b)
# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
# print(np.add(a,b))

# Zadanie 8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

# a = np.arange(9).reshape(3,3)
# for x in a:
#     print(x)
#     print("")

# Zadanie 9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())
# a = np.arange(9).reshape(3,3)
# for x in a.flat:
#     print(x)
#     print("")

# Zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
# a = np.arange(81).reshape(9,9)
# b = a.reshape(1,81)
# print(b)
"""możemy zmienić kształt tylko na 81x1 i 1x81, ponieważ jedynie te liczby tworzą macierz 
z ilością elementów równym macierzy 9x9"""

# Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
# a = np.arange(12)
# b = a.reshape(3,4)
# c = a.reshape(4,3)
# d = a.reshape(2,6)
# b = b.flatten()
# c = c.flatten()
# d = d.flatten()
# print(b)
# print(c)
# print(d)
"""spłaszczone macierze są identyczne"""
