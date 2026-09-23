# Informe - TP Señales y Sistemas: Modulación AM (Parte 1)

## Ejercicio 1: Generación de cosenos

Señales generadas:

- x1(t) = cos(2π·5t)
- x2(t) = 2·cos(2π·5t)
- x3(t) = cos(2π·10t)
- x4(t) = cos(2π·5t + π/2)

### Preguntas

**1. ¿Qué efecto produce aumentar la amplitud?**

Al comparar x1 con x2 (multiplicada por 2), la forma y la frecuencia de la señal no cambian: sigue oscilando exactamente igual en el tiempo, con los mismos cruces por cero. Lo único que cambia es la "altura" de la onda: pasa de oscilar entre -1 y 1 a oscilar entre -2 y 2. En términos de audio, la amplitud está relacionada con el volumen/intensidad de la señal, no con su tono.

**2. ¿Qué efecto produce aumentar la frecuencia?**

Al comparar x1 (5 Hz) con x3 (10 Hz), la amplitud se mantiene igual (entre -1 y 1), pero la señal oscila más rápido: en el mismo intervalo de tiempo (1 segundo) se completan el doble de ciclos (10 en vez de 5). Visualmente se ven más "compresiones" de la onda en el mismo lapso de tiempo. En audio, la frecuencia determina el tono/altura del sonido (más frecuencia = sonido más agudo).

**3. ¿Qué efecto produce modificar la fase?**

Al comparar x1 con x4 (que agrega π/2), la forma, amplitud y frecuencia de la señal son idénticas; lo único que cambia es un corrimiento horizontal (temporal) de la onda. Con un desfasaje de π/2, el coseno se convierte efectivamente en un seno negativo (cos(θ+π/2) = -sen(θ)), por lo que la curva arranca en un punto distinto del ciclo: mientras x1 empieza en su valor máximo (t=0 → x1=1), x4 empieza en 0. La fase no cambia "qué tan rápido" ni "qué tan grande" es la señal, sino en qué punto del ciclo se encuentra en cada instante.

## Ejercicio 2: Suma de cosenos

Señal analizada:

x(t) = cos(2π·5t) + 0,5·cos(2π·20t)

### Preguntas

**1. ¿La señal sigue siendo periódica?**

Sí. Es la suma de dos señales periódicas cuyas frecuencias (5 Hz y 20 Hz) están en una relación racional: 20/5 = 4. Cuando el cociente de frecuencias es racional, la suma sigue siendo periódica, con período igual al mínimo común múltiplo de los períodos individuales. En este caso, el período de x(t) es 1/5 s (el período del componente de menor frecuencia), durante el cual el componente de 20 Hz completa exactamente 4 ciclos.

**2. ¿Puede identificarse visualmente la presencia de más de una frecuencia?**

Sí. En el gráfico se ve la forma general de una oscilación lenta (de 5 Hz), pero con "ondulaciones" u oscilaciones más rápidas superpuestas sobre esa curva principal (correspondientes a la componente de 20 Hz). El resultado ya no es una sinusoide simple y suave como en el Ejercicio 1: la curva tiene pequeños "rizos" o cambios de pendiente adicionales que delatan la presencia de la segunda frecuencia, de menor amplitud (0,5).

**3. Compare esta señal con las obtenidas en el ejercicio anterior.**

Las señales del Ejercicio 1 (x1, x2, x3, x4) son todas sinusoides puras: cada una contiene una única componente de frecuencia, y su forma es la clásica curva suave del coseno (variando solo en amplitud, frecuencia o fase). La señal de este ejercicio, en cambio, es la combinación de dos frecuencias distintas, por lo que ya no es una sinusoide pura: su forma es más compleja, no se puede describir como un simple coseno desplazado o escalado. Sigue siendo periódica (como las del ejercicio anterior), pero visualmente se distingue claramente por la presencia de esa "textura" adicional producto de la segunda componente en 20 Hz.

## Ejercicio 3: Lectura de un archivo de audio

*Pendiente.*

## Ejercicio 4: Generación de tonos

Señales generadas (guardadas como `.wav`, 3 segundos, 44100 Hz):

- x1(t) = cos(2π·440t)
- x2(t) = cos(2π·880t)

### Preguntas

**1. ¿Cuál de los dos sonidos parece más grave?**

x1, el tono de 440 Hz, se percibe más grave.

**2. ¿Cuál parece más agudo?**

x2, el tono de 880 Hz, se percibe más agudo. De hecho, al ser exactamente el doble de frecuencia que x1 (880 = 2×440), x2 suena una octava por encima de x1.

**3. ¿Qué parámetro de la señal determina esta diferencia?**

La frecuencia. Es el parámetro que el oído humano percibe como "tono" o "altura" del sonido: a mayor frecuencia, el sonido se percibe más agudo, y a menor frecuencia, más grave. La amplitud (que en ambos casos es la misma) afecta el volumen, no el tono.

## Ejercicio 5: Observación de una señal desconocida

Señal analizada:

x(t) = (1 + 0,5·cos(2πt))·cos(2π·20t)

comparada contra un coseno simple de 20 Hz.

### Preguntas

**1. Grafique la señal.**

Ver gráfico generado por el script (`src/tp1.py`, sección Ejercicio 5): se observa una portadora de 20 Hz cuya amplitud varía lentamente a lo largo del tiempo, dibujando una envolvente que sube y baja.

**2. Compare el resultado con un coseno simple de frecuencia 20 Hz.**

El coseno simple de 20 Hz tiene amplitud constante: siempre oscila entre -1 y 1 de manera uniforme. En cambio, x(t) también oscila a 20 Hz (misma frecuencia de la portadora), pero su amplitud no es constante: va cambiando en el tiempo siguiendo el término (1 + 0,5·cos(2πt)), que varía lentamente (a 1 Hz) entre 0,5 y 1,5.

**3. Describa las diferencias observadas.**

- La señal x(t) no tiene amplitud fija: está "envuelta" por una curva más lenta (1 + 0,5·cos(2πt)) que hace que sus picos crezcan y decrezcan periódicamente, alcanzando un máximo de 1,5 y un mínimo de 0,5, en vez de mantenerse siempre en 1 como el coseno simple.
- Esta envolvente es justamente el principio de la modulación en amplitud (AM): una señal de baja frecuencia (1 Hz, la "moduladora") controla la amplitud de una señal de alta frecuencia (20 Hz, la "portadora").
- A diferencia del coseno simple, que es una señal de una sola frecuencia pura, x(t) contiene múltiples componentes frecuenciales (esto se puede verificar expandiendo el producto con identidades trigonométricas, lo que da lugar a componentes en 19 Hz, 20 Hz y 21 Hz), aunque visualmente en el dominio del tiempo esto se manifiesta solo como la envolvente que varía la amplitud.
