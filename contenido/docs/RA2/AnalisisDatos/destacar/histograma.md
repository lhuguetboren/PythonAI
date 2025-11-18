import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el dataset
# Supongamos df contiene la tabla con columnas: transaction_qty, unit_price, product_category (= Coffee/Tea/…)
df = pd.read_csv('transacciones.csv', parse_dates=['transaction_date'], dayfirst=True)

# 2. Convertir unit_price a numérico si fuera necesario (coma decimal)
df['unit_price'] = df['unit_price'].astype(str).str.replace(',', '.').astype(float)

# 3. Filtrar solo cafés para centrarnos en ese segmento (si la categoría lo permite)
df_coffee = df[df['product_category'] == 'Coffee']

# 4. Extraer array NumPy del precio unitario para café
arr_price = df_coffee['unit_price'].dropna().to_numpy()

# 5. Calcular histograma de precios unitarios de café
hist, bin_edges = np.histogram(arr_price, bins=20)  # 20 intervalos
print("Conteos:", hist)
print("Límites de los bins:", bin_edges)

# 6. Visualización con matplotlib / seaborn para ver mejor
plt.figure(figsize=(8,5))
sns.histplot(arr_price, bins=20, kde=False)
plt.title("Distribución del precio unitario de cafés")
plt.xlabel("Precio unitario (€)")
plt.ylabel("Frecuencia")
plt.show()

# 7. Otra variable: cantidad comprada (transaction_qty)
arr_qty = df_coffee['transaction_qty'].dropna().to_numpy()
plt.figure(figsize=(8,5))
sns.histplot(arr_qty, bins=range(1, arr_qty.max()+2), discrete=True)  # si la cantidad es entera
plt.title("Distribución de la cantidad de cafés por transacción")
plt.xlabel("Cantidad de unidades")
plt.ylabel("Frecuencia")
plt.show()

# 8. Interpretación / preguntas para los alumnos
#   • ¿Cuál es el rango de precio más habitual para un café? ¿Hay “colas” de precio alto?  
#   • ¿La mayoría de transacciones son de 1 unidad o más?  
#   • ¿Existen transacciones con precio muy bajo o muy alto que podrían considerarse atípicas (outliers)?  
#   • ¿Se aprecia una ‘distribución normal’ o está sesgada hacia la derecha/izquierda?  
