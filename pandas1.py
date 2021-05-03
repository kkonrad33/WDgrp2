import pandas as pd
import numpy as np
import xlrd
import openpyxl
# zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# print(df)

# zadanie 2

# print(df[df['Liczba']<1000])

# print(df.loc[df['Imie'] == 'KONRAD'])
# print(df['Liczba'].sum())

# new_df = (df[((df.Rok >= 2005) & (df.Rok <= 2010))])
# print(new_df['Liczba'].sum())

# new_df = (df[((df.Rok == 2010) & (df.Plec == 'M'))])
# print(new_df['Liczba'].sum())

# for year in range(2000, 2018):
#     ndf = (df[((df.Rok == year) & (df.Plec == 'M'))])
#     print(ndf.iloc[ndf.Liczba.argmax(), 0:4])
#
# for year in range(2000, 2018):
#     ndf = (df[((df.Rok == year) & (df.Plec == 'K'))])
#     print(ndf.iloc[ndf.Liczba.argmax(), 0:2])

# ndf = df.loc[df['Plec'] == 'M']
# grouped = ndf.groupby(['Imie'])
#
# men = grouped.get_group()
# print(men)
