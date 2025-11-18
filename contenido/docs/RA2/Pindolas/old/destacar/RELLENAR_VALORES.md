Estos métodos sirven para rellenar valores faltantes (NaN) en series temporales o datos ordenados:

ffill() (forward fill): rellena cada NaN con el último valor válido anterior. 
Medium

bfill() (backward fill): rellena cada NaN con el siguiente valor válido posterior. 
Stack Overflow
+1

interpolate(): interpola valores faltantes según un método (por ejemplo lineal) entre los valores existentes.

Son útiles particularmente en análisis temporal o cuando tienes lagunas en los datos que “se pueden asumir” continuas o interpolables.

Ejemplo aplicado (histórico bursátil)

Supongamos que estás trabajando con tu dataset de precios de acciones, en el que puede haber días sin cotización o valores faltantes (NaN) en close, volume, etc. El flujo podría ser:

import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv('stock_prices.csv', parse_dates=['date'])
df = df.sort_values(['symbol','date'])

# Seleccionar un símbolo para simplificar
symbol = 'AAPL'
df_sym = df[df['symbol'] == symbol].set_index('date')

# Supongamos que hay valores faltantes en 'close'
print("Antes de rellenar:")
print(df_sym['close'].isna().sum())

# 1. Forward-fill: usar el valor anterior cuando falte
df_sym['close_ffill'] = df_sym['close'].ffill()

# 2. Backward-fill: usar el siguiente valor válido cuando falte
df_sym['close_bfill'] = df_sym['close'].bfill()

# 3. Interpolación lineal: rellenar NaN entre valores existentes
df_sym['close_interpolated'] = df_sym['close'].interpolate(method='linear')

print("Después de rellenar:")
print(df_sym[['close', 'close_ffill', 'close_bfill', 'close_interpolated']].head(10))
