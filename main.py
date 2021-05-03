import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# wykres = grupa.plot()
# wykres.set_ylabel('liczba dzieci')
# wykres.set_xlabel('rok')
# wykres.legend()
# plt.title('Liczba urodzonych dzieci w każdym roku')
# plt.show()

# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.bar()
# wykres.set_ylabel('liczba dzieci')
# wykres.set_xlabel('Płeć')
# wykres.legend()
# plt.title('Ilość urodzonych dzieci z podziałem na płeć')
# plt.show()

# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
#
# ndf = (df[((df.Rok >= 2012) & (df.Rok <= 2017))])
#
# grupa = ndf.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=16, figsize=(5,5), legend=(0,0))
# plt.legend(loc="upper right")
# plt.title('Ilość urodzonych dzieci z podziałem na płeć')
# plt.show()
