import pandas as pd
import numpy as np

# 1. Cargar el dataset de sets de LEGO
df = pd.read_csv('lego_sets.csv')

# 2. Asegurarse de que las columnas numéricas están bien convertidas
df['pieces']         = pd.to_numeric(df['pieces'], errors='coerce')
df['US_retailPrice'] = pd.to_numeric(df['US_retailPrice'], errors='coerce')

# 3. Convertir la columna ‘pieces’ a un array NumPy
arr_pieces = df['pieces'].dropna().to_numpy()
print("Array de piezas (primeros 10):", arr_pieces[:10])

# 4. Calcular el percentil 90 del número de piezas
p90_pieces = np.percentile(arr_pieces, 90)
print("Percentil 90 del número de piezas:", p90_pieces)

# 5. Crear una nueva columna booleana que indique si un set está en el top 10% en número de piezas
df['top_10pct_pieces'] = df['pieces'] > p90_pieces

# 6. (Opcional) Crear columna con el valor del percentil para referencia
df['pieces_90th_percentile_value'] = p90_pieces

# 7. Ver resultado
print(df[['set_id', 'name', 'pieces', 'top_10pct_pieces', 'pieces_90th_percentile_value']].head(15))
