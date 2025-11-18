import pandas as pd
import numpy as np

# 1. Cargar los datos
df = pd.read_csv('lego_sets.csv')

# 2. Convertir columnas numéricas
df['US_retailPrice'] = pd.to_numeric(df['US_retailPrice'], errors='coerce')
df['pieces']         = pd.to_numeric(df['pieces'], errors='coerce')
df['minifigs']       = pd.to_numeric(df['minifigs'], errors='coerce')

# 3. Filtrar filas con datos completos respecto a lo que vamos analizar
df2 = df.dropna(subset=['US_retailPrice', 'pieces', 'theme'])

# 4. Aplicar One-Hot Encoding sobre la columna 'theme'
df2 = pd.get_dummies(df2, columns=['theme'], drop_first=True, dtype=int)  # ▶️ Reemplaza df2

# 5. Ahora df2 incluye las columnas dummy; por ejemplo podríamos ver las nuevas columnas
print("Columnas tras get_dummies:", df2.columns)

# 6. Ahora podemos incluir una columna dummy como predic-tora en una regresión:
#    Por ejemplo, usar piezas, minifigs y las columnas dummy de tema como variables independientes
X = df2.drop(columns=['set_id', 'name', 'US_retailPrice', 'agenrange_min', 'minifigs'])  # ajusta lo que necesites
y = df2['US_retailPrice']

# 7. Si quieres, calcular correlación entre cada dummy y el precio
corr = df2.corr()['US_retailPrice'].sort_values(ascending=False)
print("Correlaciones con precio:", corr.head(10))

# 8. Seguir con análisis o modelado (por ejemplo regresión lineal usando scikit-learn)
