import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
# zad 1. Wygeneruj wykres liniowy dla z od 0 do 2pi, x = sin(z), y = 2cos(z).
# fig = plt.figure()
# ax = fig.gca(projection = '3d')
#
# z = np.linspace(0,2*np.pi,100)
# x = np.sin(z)
# y = 2 * np.cos(z)
# ax.plot(x, y, z, label='zadanie 1')
# ax.legend()
# plt.show()

# zad 2. Wygeneruj wykres punktowy dla 5 różnych losowych serii z użyciem różnych znaczników i kolorów.
# s = pd.Series(np.random.randn(30))
# d = pd.Series(np.random.randn(20))
# f = pd.Series(np.random.randn(40))
# g = pd.Series(np.random.randn(50))
# h = pd.Series(np.random.randn(60))
# plt.plot(s, 'r.', d, 'g1', f, 'kp', g, "mP", h, 'c^')
# plt.show()

# zad 3. Wygeneruj wykres z przykładu 3 w 5 różnych kolorystkach.
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5,5,0.25)
# Y = np.arange(-5,5,0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# 1
# surf = ax.plot_surface(X, Y, Z, cmap=cm.binary, linewidth=0, antialiased=False)
# 2
# surf = ax.plot_surface(X, Y, Z, cmap=cm.bone, linewidth=0, antialiased=False)
# 3
# surf = ax.plot_surface(X, Y, Z, cmap=cm.summer, linewidth=0, antialiased=False)
# 4
# surf = ax.plot_surface(X, Y, Z, cmap=cm.autumn, linewidth=0, antialiased=False)
# 5
# surf = ax.plot_surface(X, Y, Z, cmap=cm.cool, linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()

# zad 4. Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu 4 wykorzystując 5 różnych kombinacji wyglądu.
# fig = plt.figure(figsize=(8,3))
# ax = fig.gca(projection='3d')
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x,_y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = deph = 1
# ax.bar3d(x, y, bottom, width, deph, top, shade=True, color='r')
# plt.show()

# zad 5. W przykładzie 3 zmień gęstość próbek do wykresu na krok 0.1 oraz włącz antyaliasing. Wyświetl pierwotny i nowy wykres obok siebie.
fig = plt.figure()
ax = fig.add_subplot(1,2,1,projection='3d')
X = np.arange(-5,5,0.1)
Y = np.arange(-5,5,0.1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)

ax = fig.add_subplot(1,2,2,projection='3d')
X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()