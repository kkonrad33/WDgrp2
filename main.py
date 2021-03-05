#1
#lista_sportow = ['piłka_nożna', 'siatkówka', 'baseball']
#lista_sportow.reverse()
#lista_sportow.append('koszykówka')
#print(lista_sportow)

#2
#slownik = {"np": "na przykład", "m.in.": "między innymi", "pt": "pod tytułem"}

#3
#gry = {"League of Legends": "PC", "Cyberpunk2077": "PC", "The Legend Of Zelda": "NS", "Red Dead Redemption 2": "PS4"}
#print(len(gry))

# 4
# zdanie = input("Napisz dowolne zdanie: ")
# ilosc = 0
# for a in zdanie:
#     if a == "a":
#         ilosc += 1
# print(ilosc)

#5
# import sys as system
# system.stdout.write("wpisz 1 liczbę całkowitą: ")
# a = system.stdin.readline()
# system.stdout.write("wpisz 2 liczbę całkowitą: ")
# b = system.stdin.readline()
# system.stdout.write("wpisz 3 liczbę całkowitą: ")
# c = system.stdin.readline()
# a = int(a)
# b = int(b)
# c = int(c)
# wynik = a ** b + c
# system.stdout.write(str(wynik))

#6
# print("Wpisz 1 liczbę całkowitą: ")
# a = input()
# print("Wpisz 2 liczbę całkowitą: ")
# b = input()
# print("Wpisz 3 liczbę całkowitą: ")
# c = input()
# if a>b:
#     if c>a:
#         print("Największa jest 3 liczba.")
#     else:
#         print("Największa jest 1 liczba.")
# elif b>a:
#     if c>b:
#         print("Największa jest 3 liczba.")
#     else:
#         print("Największa jest 2 liczba.")
# else:
#     if a == c:
#         print("Liczby są równe.")
#     else:
#         print("Największa jest 3 liczba.")
#7
# liczby = [2, 4, 5.65, 12, 5, 12.332, 6.93, 7369]
# for kwadrat in liczby:
#     print(kwadrat ** 2)
#8
# i = 0
# lista = []
# while i < 10:
#     print("Podaj liczbe: ")
#     a = input()
#     parzysta = int(a)%2
#     if parzysta == 0:
#         lista.append(a)
#     i += 1
# print(lista)

#9
# lista = [1, 2, 3, 4, 5]
# for liczba in lista:
#     a = int(liczba)%2
#     if a == 0:
#         print("E")
#     else:
#         print("EEEEEE")
#10
# import math
# print("Podaj liczbę do spierwiastkowania: ")
# a = int(input())
# try:
#     a = (math.sqrt(a))
#     print(a)
# except:
#     print("Nie wolno pierwiastkować liczb ujemnych!!!")

