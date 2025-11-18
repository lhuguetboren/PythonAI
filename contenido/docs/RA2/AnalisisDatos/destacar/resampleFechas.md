En los ejercicios que incluyen análisis temporal (por ejemplo, cuando tienes una columna fecha/hora y quieres agrupar los datos por hora, día, mes, etc.). Por ejemplo:

Si estudias el dataset de reproducciones de Spotify donde tienes una columna ts con fecha/hora, puedes fijar esa columna como índice para luego “re-muestrear” por horas o días para ver cuántas reproducciones se hacen en cada franja.

También en un dataset bursátil donde tienes date y quieres agrupar datos de cierre por día, semana o mes para calcular medias o sumas.

Cómo utilizarlo

Aquí tienes un ejemplo de código adaptado al contexto de un DataFrame df que tiene una columna date (o ts) con tipo string o datetime:

import pandas as pd

# 1. Supongamos que hemos cargado los datos:
# df = pd.read_csv('historial.csv', parse_dates=['date'])  (o parse_dates=['ts'])
print(df.info())  # Ver tipo de dato de la columna date

# 2. Convertir la columna de fecha a datetime si no lo está:
df['date'] = pd.to_datetime(df['date'])

# 3. Fijar la columna date como índice del DataFrame:
df = df.set_index('date')
# Ahora el índice del df es un DatetimeIndex — requisito para resample. :contentReference[oaicite:1]{index=1}

# 4. Aplicar resample para agrupar los datos según frecuencia temporal:
#    Ejemplo: agrupar por hora ('H')
hourly = df.resample('H').agg({'close': 'mean', 'volume': 'sum'})
print(hourly.head())

#    Ejemplo: agrupar por día ('D')
daily = df.resample('D').agg({'close': 'mean', 'volume': 'sum'})
print(daily.head())

Explicación de la sintaxis:

df.set_index('date'): convierte la columna date en el índice del DataFrame. Esto es importante para que resample() funcione correctamente, ya que requiere un índice de tipo datetime o que especifiques el argumento on=. 
Medium
+1

df.resample('H') o df.resample('D'): crea un objeto de tipo Resampler que agrupa los datos en intervalos de frecuencia 'H' (horas) o 'D' (días). Luego se le pueden aplicar funciones de agregación (.mean(), .sum(), .agg(), etc.). 
GeeksforGeeks

En agg({...}) puedes definir qué columnas se combinan y qué función aplicar (por ejemplo, la media del precio de cierre, la suma del volumen).

✅ Consideraciones adicionales

Si no quieres cambiar el índice, puedes usar df.resample('H', on='date') en lugar de set_index, pero fijar el índice suele facilitar análisis posteriores. 
Medium

Al agrupar (downsampling) los datos, asegúrate de elegir una métrica adecuada (por ejemplo, media del precio, suma del volumen).

Si haces “upsampling” (ir de menor a mayor frecuencia) aparecerán valores faltantes y tendrás que rellenarlos (.ffill(), .bfill(), .interpolate()). 
DataCamp

Asegúrate de que la columna de fecha/hora no contenga formatos mixtos o errores antes de fijarla como índice.

import pandas as pd

df = pd.read_csv('datos_historico.csv', parse_dates=['date'])
df['date'] = pd.to_datetime(df['date'])

df = df.set_index('date')

# Agrupar por día, calcular máximo del “high”, mínimo del “low” y último valor del “close”
daily = df.resample('D').agg({
    'high': 'max',
    'low':  'min',
    'close': 'last'
})

print(daily.head())
