# 1
# import random
# import sys
# losowe = []
# for x in range(9):
#     losowe.append(random.randint(0, 30))
# print(losowe)
# plik = open("losy.txt", "w+")
# for x in losowe:
#     x *= 2
#     plik.writelines(str(x))
#     plik.writelines(str(" "))
# plik.close()

# 2
# plik = open("losy.txt", "r")
# liczby = plik.readline()
# print(liczby)

# 3
# with open("kolory", "r+") as plik:
#     plik.write("Borsuk jest oportunistycznym wszystkożercą, łatwo przystosowującym się do zasobów pokarmowych w okolicy siedliska - jego dieta obejmuje wiele roślin i zwierząt. ")
#     plik.write("Dżdżownice stanowią najważniejsze źródło pożywienia borsuka; do ważnych należą także duże owady, małe i młode ssaki oraz przy nadarzającej się okazji ptaki, padlina, zboża i owoce. ")
#     plik.write("Ssaki, na które poluje to m.in. zające, szczury, myszy, norniki, ryjówki, krety i jeże oraz przydomowe zwierzęta znajdujące się na terenie łowieckim borsuka, tj. koty, króliki.")
#     borsuk = plik.readlines()
#     print(borsuk)

# 4
# class NaZakupy():
#     nazwa_produktu = ""
#     ilosc = 0
#     jednostka_miary = ""
#     cena_jed = 0
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
#
#     def ile_produktu(self):
#         print(str(self.ilosc) + "" + self.jednostka_miary)
#     def ile_kosztuje(self):
#         kwota = self.ilosc * self.cena_jed
#         return kwota

# 5
# class ciagia:
#     pierwszy = 0
#     roznica = 0
#     ile = 0
#     elementy_ciagu = []
#
#     def wyswietl_dane(self):
#         print(self.elementy_ciagu)
#     def pobierz_elementy(self):
#         element = input("Podaj element: ")
#         e = int(element)
#         self.elementy_ciagu.append(e)
#     def pobierz_parametry(self):
#         pierwszy = input("Podaj pierwszy element: ")
#         roznica = input("Podaj różnice: ")
#         ile = input("Podaj ile elementów chcesz wygenerować: ")
#         self.pierwszy = int(pierwszy)
#         self.roznica = int(roznica)
#         self.ile = int(ile)
#     def policz_sume(self):
#         suma = 0
#         for x in self.elementy_ciagu:
#             suma += x
#         print(suma)
#     def policz_elementy(self):
#         self.elementy_ciagu.append(self.pierwszy)
#         if self.roznica != 0:
#             for x in range(self.ile-1):
#                 an = self.pierwszy + self.roznica
#                 self.elementy_ciagu.append(an)
#                 self.pierwszy = an
# ciag = ciagia()
# ciag.pobierz_elementy()
# ciag.pobierz_parametry()
# ciag.policz_elementy()
# ciag.wyswietl_dane()
# 6
# class Robaczek:
#     def __init__(self, x=0, y=0, krok=1):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, ile_krokow):
#         self.y += (ile_krokow*self.krok)
#     def idz_w_dol(self, ile_krokow):
#         self.y -= (ile_krokow*self.krok)
#     def idz_w_prawo(self, ile_krokow):
#         self.x += (ile_krokow*self.krok)
#     def idz_w_lewo(self, ile_krokow):
#         self.x -= (ile_krokow*self.krok)
#     def pokaz_gdzie_jestes(self):
#         print("x: " + str(self.x) + " y: " + str(self.y))
#
# robal = Robaczek()
# print(robal.pokaz_gdzie_jestes())
# robal.idz_w_gore(5)
# robal.idz_w_lewo(4)
# robal.idz_w_prawo(7)
# robal.idz_w_dol(9)
# print(robal.pokaz_gdzie_jestes())


