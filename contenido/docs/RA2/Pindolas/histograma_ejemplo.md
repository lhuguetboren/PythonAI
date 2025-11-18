# Histogramas con pandas y Matplotlib

## 1. ¿Qué es un histograma?

Un **histograma** muestra la distribución de una variable numérica, agrupando los valores en **intervalos** (bins) y contando cuántas observaciones caen en cada uno.

Permite ver rápidamente:

- Si la distribución es simétrica o sesgada.
- Si hay valores extremos (outliers).
- Si la variable parece aproximadamente normal, uniforme, etc.

---

## 2. Histogramas en pandas / Matplotlib

Formas típicas de dibujar un histograma:

```python
df["col"].hist(bins=10)
```

o usando directamente Matplotlib:

```python
import matplotlib.pyplot as plt
plt.hist(df["col"], bins=10)
```

Parámetros clave:

- `bins`: número de intervalos (o una lista de bordes de los intervalos).
- `range`: rango manual `[min, max]` de la variable.
- `density=True`: normaliza el histograma para que el área total sea 1.

---

## 3. Ejemplo completo con datos sintéticos

### Objetivo

- Crear un DataFrame con dos variables numéricas (por ejemplo, importes de compra y edad).
- Dibujar histogramas separados para cada una.
- Comparar cómo cambian con distinto número de `bins`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Crear datos sintéticos
# ---------------------------------------------------------
np.random.seed(123)

n = 200
data = {
    "purchase_amount": np.random.gamma(shape=2.0, scale=20.0, size=n),  # distribución sesgada positiva
    "customer_age": np.random.normal(loc=40, scale=10, size=n)          # distribución aproximadamente normal
}

df = pd.DataFrame(data)

print("=== Primeras filas del DataFrame ===")
print(df.head())

# ---------------------------------------------------------
# 2. Histograma de purchase_amount
# ---------------------------------------------------------

plt.figure()
df["purchase_amount"].hist(bins=20)
plt.title("Histograma de purchase_amount (20 bins)")
plt.xlabel("purchase_amount")
plt.ylabel("Frecuencia")
plt.show()

# ---------------------------------------------------------
# 3. Histograma de customer_age con distinto número de bins
# ---------------------------------------------------------

plt.figure()
df["customer_age"].hist(bins=10)
plt.title("Histograma de customer_age (10 bins)")
plt.xlabel("customer_age")
plt.ylabel("Frecuencia")
plt.show()

plt.figure()
df["customer_age"].hist(bins=30)
plt.title("Histograma de customer_age (30 bins)")
plt.xlabel("customer_age")
plt.ylabel("Frecuencia")
plt.show()
```

---

## 4. Ejercicios propuestos

1. Cambiar la distribución de `purchase_amount` (por ejemplo, usando `np.random.normal`) y comparar visualmente los histogramas.
2. Crear una tercera variable, por ejemplo `items_per_order` (número de ítems por pedido), y dibujar su histograma.
3. Probar distintos valores de `bins` y comentar cómo afecta a la interpretación de la distribución.
