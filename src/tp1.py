import math
import matplotlib.pyplot as plt
import numpy as np

F_MUESTREO_HZ = 1000
DURACION_MUESTRA_SEG = 1

# 1. Crear un vector de ángulos (por ejemplo, de 0 a 2*pi con 10 elementos)
t = np.linspace(0, DURACION_MUESTRA_SEG, DURACION_MUESTRA_SEG * F_MUESTREO_HZ)
# print("Vector de tiempo:\n", t)

# 2. Cargar el vector con los valores del coseno
x1 = np.cos(2*np.pi*5*t)
x2 = 2 * np.cos(2*np.pi*5*t)
x3 = np.cos(2*np.pi*10*t)
x4 = np.cos(2*np.pi*5*t + np.pi/2)

# Graficar las cuatro señales en un mismo plot
plt.plot(t, x1, label="x1 = cos(2π·5t)")
plt.plot(t, x2, label="x2 = 2·cos(2π·5t)")
plt.plot(t, x3, label="x3 = cos(2π·10t)")
plt.plot(t, x4, label="x4 = cos(2π·5t + π/2)")

plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Señales x1, x2, x3, x4")
plt.legend()
plt.grid(True)

# Comparaciones de x1 contra cada una de las demás señales
pares = [
    (x2, "x2 = 2·cos(2π·5t)"),
    (x3, "x3 = cos(2π·10t)"),
    (x4, "x4 = cos(2π·5t + π/2)"),
]

for xi, label in pares:
    plt.figure()
    plt.plot(t, x1, label="x1 = cos(2π·5t)")
    plt.plot(t, xi, label=label)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.title(f"x1 vs {label}")
    plt.legend()
    plt.grid(True)

plt.show()