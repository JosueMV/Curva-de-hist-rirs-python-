# hist-resis

Pequeño proyecto en Python para **graficar curvas de histéresis** a partir de mediciones de **distancia (cm)** vs **voltaje (V)**.  
El script genera **tres gráficas comparando subida y bajada** de un sensor (o sistema) para observar la diferencia entre el recorrido ascendente y descendente.

---

## 🧩 ¿Qué hace el código?

- Define una lista de **distancias** y seis series de **voltajes**:
  - `subida_1`, `bajada_1`
  - `subida_2`, `bajada_2`
  - `subida_3`, `bajada_3`
- Crea una figura con **3 subplots** (una por medición).
- En cada subplot:
  - grafica la curva de **subida** y de **bajada** (línea + marcadores),
  - etiqueta ejes, título y leyenda.
- Ajusta el layout y **muestra las gráficas** en pantalla.

> La **histéresis** aparece cuando la salida depende no solo del valor actual de la entrada, sino también de su **historial**. Aquí se ve como la curva de “bajada” no coincide exactamente con la de “subida”.

---

## 📁 Estructura mínima

