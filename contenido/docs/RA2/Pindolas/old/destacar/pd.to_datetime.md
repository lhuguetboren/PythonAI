import pandas as pd

# Supongamos que df es tu DataFrame y 'ts' o 'date' es la columna de fecha/hora
df = pd.read_csv('tu_dataset.csv', parse_dates=['date'])  # o parse_dates=['ts']

# 1. Asegurar que la columna es tipo datetime
df['date'] = pd.to_datetime(df['date'])

# 2. Extraer componentes
df['year']       = df['date'].dt.year
df['month']      = df['date'].dt.month
df['day']        = df['date'].dt.day
df['hour']       = df['date'].dt.hour   # si hay hora
df['minute']     = df['date'].dt.minute # si interesa
df['weekday']    = df['date'].dt.weekday   # 0 = Lunes, …, 6 = Domingo
df['weekday_name']= df['date'].dt.day_name()  # nombre del día

# Mostrar primeras filas para ver resultado
print(df[['date','year','month','day','hour','weekday','weekday_name']].head())
