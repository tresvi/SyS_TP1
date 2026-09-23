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

*Pendiente.*

## Ejercicio 3: Lectura de un archivo de audio

*Pendiente.*

## Ejercicio 4: Generación de tonos

*Pendiente.*

## Ejercicio 5: Observación de una señal desconocida

*Pendiente.*
