import math
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

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

# ---------------------------------------------------------------------------
# Ejercicio 2: Suma de cosenos
# ---------------------------------------------------------------------------
x_suma = np.cos(2 * np.pi * 5 * t) + 0.5 * np.cos(2 * np.pi * 20 * t)

plt.figure()
plt.plot(t, x_suma)
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Ejercicio 2: x(t) = cos(2π·5t) + 0,5·cos(2π·20t)")
plt.grid(True)
plt.show()

# ---------------------------------------------------------------------------
# Ejercicio 3: Lectura de un archivo de audio
# ---------------------------------------------------------------------------
carpeta_audio = os.path.join(os.path.dirname(__file__), "..", "audio")
os.makedirs(carpeta_audio, exist_ok=True)
ruta_audio_entrada = os.path.join(carpeta_audio, "entrada.wav")

# Si todavía no descargaste/grabaste un WAV propio, generamos uno de prueba
# para que el script pueda correr de punta a punta. Reemplazá
# "audio/entrada.wav" por tu propio archivo cuando lo tengas.
if not os.path.exists(ruta_audio_entrada):
    fs_prueba = 44100
    t_prueba = np.linspace(0, 2, fs_prueba * 2, endpoint=False)
    señal_prueba = np.cos(2 * np.pi * 300 * t_prueba)
    señal_prueba_int16 = np.int16(señal_prueba * 32767)
    wavfile.write(ruta_audio_entrada, fs_prueba, señal_prueba_int16)
    print(f"No se encontró un WAV propio: se generó uno de prueba en {ruta_audio_entrada}")

# 1. Leer el archivo
fs_audio, datos_audio = wavfile.read(ruta_audio_entrada)

# 2. Frecuencia de muestreo
print(f"\nFrecuencia de muestreo: {fs_audio} Hz")

# 3. Cantidad total de muestras (por canal)
cantidad_muestras = datos_audio.shape[0]
print(f"Cantidad total de muestras: {cantidad_muestras}")

# 4. Duración del audio
duracion_audio = cantidad_muestras / fs_audio
print(f"Duración: {duracion_audio:.3f} s")

t_audio = np.linspace(0, duracion_audio, cantidad_muestras, endpoint=False)

# ¿Mono o estéreo?
es_estereo = datos_audio.ndim == 2 and datos_audio.shape[1] == 2
canales = [datos_audio[:, 0], datos_audio[:, 1]] if es_estereo else [datos_audio]
nombres_canales = ["Canal izquierdo", "Canal derecho"] if es_estereo else ["Mono"]

# 5. Graficar la señal completa
plt.figure()
for canal, nombre in zip(canales, nombres_canales):
    plt.plot(t_audio, canal, label=nombre)
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Ejercicio 3: señal de audio completa")
plt.legend()
plt.grid(True)

# 6. Graficar únicamente los primeros 50 ms
muestras_50ms = int(fs_audio * 0.050)
plt.figure()
for canal, nombre in zip(canales, nombres_canales):
    plt.plot(t_audio[:muestras_50ms], canal[:muestras_50ms], label=nombre)
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Ejercicio 3: primeros 50 ms")
plt.legend()
plt.grid(True)

# 7. Graficar únicamente los primeros 500 ms
muestras_500ms = int(fs_audio * 0.500)
plt.figure()
for canal, nombre in zip(canales, nombres_canales):
    plt.plot(t_audio[:muestras_500ms], canal[:muestras_500ms], label=nombre)
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Ejercicio 3: primeros 500 ms")
plt.legend()
plt.grid(True)

plt.show()

# ---------------------------------------------------------------------------
# Ejercicio 4: Generación de tonos
# ---------------------------------------------------------------------------
DURACION_TONO_SEG = 3
FS_TONO_HZ = 44100  # frecuencia de muestreo típica para audio

t_tono = np.linspace(0, DURACION_TONO_SEG, DURACION_TONO_SEG * FS_TONO_HZ, endpoint=False)

tono1 = np.cos(2 * np.pi * 440 * t_tono)
tono2 = np.cos(2 * np.pi * 880 * t_tono)

# Convertir a PCM de 16 bits para poder guardarlo como WAV
def a_int16(señal):
    return np.int16(señal / np.max(np.abs(señal)) * 32767)

carpeta_salida = os.path.join(os.path.dirname(__file__), "..", "audio")
os.makedirs(carpeta_salida, exist_ok=True)

ruta_tono1 = os.path.join(carpeta_salida, "tono_440hz.wav")
ruta_tono2 = os.path.join(carpeta_salida, "tono_880hz.wav")

wavfile.write(ruta_tono1, FS_TONO_HZ, a_int16(tono1))
wavfile.write(ruta_tono2, FS_TONO_HZ, a_int16(tono2))

print(f"Tono de 440 Hz guardado en: {ruta_tono1}")
print(f"Tono de 880 Hz guardado en: {ruta_tono2}")
print("Reproducí ambos archivos .wav para escucharlos y comparar.")

# ---------------------------------------------------------------------------
# Ejercicio 5: Observación de una señal desconocida
# ---------------------------------------------------------------------------
t5 = np.linspace(0, 1, F_MUESTREO_HZ, endpoint=False)

x5 = (1 + 0.5 * np.cos(2 * np.pi * t5)) * np.cos(2 * np.pi * 20 * t5)
coseno_simple_20hz = np.cos(2 * np.pi * 20 * t5)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)

axs[0].plot(t5, x5, color="tab:blue")
axs[0].set_title("x(t) = (1 + 0.5·cos(2πt))·cos(2π·20t)")
axs[0].set_ylabel("Amplitud")
axs[0].grid(True)

axs[1].plot(t5, coseno_simple_20hz, color="tab:orange")
axs[1].set_title("Coseno simple de 20 Hz")
axs[1].set_xlabel("Tiempo [s]")
axs[1].set_ylabel("Amplitud")
axs[1].grid(True)

fig.suptitle("Ejercicio 5: señal modulada en amplitud vs. coseno simple")
fig.tight_layout()

plt.show()