# Funciones a utilizar: pandas y NumPy

Organizadas por ejercicio tipo como referencia de qué métodos pueden usar.

## Ejercicio: Gestión de valores NA / Limpieza de datos

### pandas

- `pd.read_csv()` — Leer fichero CSV.  
- `df.info()` — Información de tipos, no nulos, etc.  
- `df.describe()` — Estadísticas descriptivas de columnas numéricas.  
- `df.isna()` / `df.isnull()` — Detectar valores nulos.  
- `df.notna()` / `df.notnull()` — Detectar valores no nulos.  
- `df.dropna()` — Eliminar filas/columnas con valores nulos.  
- `df.fillna(value=…)` — Rellenar valores nulos con un valor especificado.  
- `pd.to_numeric()` — Convertir columna a tipo numérico.  
- `pd.to_datetime()` — Convertir columna a tipo fecha/hora.  
- `df.astype(type)` — Cambiar tipo de una columna, por ejemplo a `float`, `int`.  

### NumPy

- `np.array()` — Crear un array NumPy, útil cuando se extraen datos de un DataFrame.  
- `arr.astype(new_type)` — Cambiar el tipo de un array, por ejemplo de float a int.  
- `np.isnan(arr)` — Detectar valores NaN en un array.  
- `np.where(condition, x, y)` — Crear un array nuevo basado en una condición (útil para imputación condicional).  



## Ejercicio: Creación de columnas nuevas / Conversión de formatos  
### pandas

- `df['new_col'] = …. ` — Crear una nueva columna con asignación directa.  
- `df.assign(new_col = …)` — Crear columna adicional mediante método assign.  
- `df['date'].dt.hour` — Extraer hora del día de una columna datetime.  
- `df['date'].dt.weekday` — Extraer día de la semana de una columna datetime.  
- `df.sort_values(by='col', ascending=…)` — Ordenar el DataFrame según una columna.  
- `df.rename(columns={…})` — Renombrar columnas.  

### NumPy

- Operaciones vectorizadas: por ejemplo `arr1 / arr2`, `np.log(arr)`, `np.power(arr,2)` — aplicadas a arrays derivados de pandas.  
- `np.cumsum(arr)` — Suma acumulativa, puede servir para series de tiempo.  
- `np.cumprod(arr)` — Producto acumulativo, útil para cálculos de crecimiento.

---

## Ejercicio: Agrupaciones (groupby) / Agregaciones

### pandas

- `df.groupby('col')` — Agrupar por una o varias columnas.  
- `.agg()` — Aplicar múltiples funciones de agregación tras groupby, por ejemplo `.agg({'col1':'sum','col2':'mean'})`.  
- `.sum()` / `.mean()` / `.count()` — Funciones de agregación comunes.  
- `df.value_counts()` — Contar frecuencia de valores únicos en una columna.  
- `df.nunique()` — Número de valores únicos en una columna.

### NumPy

- Después de extraer arrays, usar por ejemplo `np.mean(arr)`, `np.std(arr)` para estadísticas del grupo.  
- `np.argsort(arr)` — Obtener índices que ordenarían el array, útil para extraer top/bottom grupos.

---

## Ejercicio: Estadística básica y percentiles / outliers

### pandas

- `df.describe()` — Ver estadísticas principales (mean, std, min, max, quartiles).  
- `df.median()` — Mediana de una columna.  
- `df.std()` — Desviación estándar de una columna.  
- `df.min()` / `df.max()` — Mínimo/máximo.  
- `df.quantile(q)` — Cuantil para una columna (por ejemplo 0.95 para percentil 95).  

### NumPy

- `np.mean(arr)`, `np.median(arr)`, `np.std(arr)` — Media, mediana, desviación estándar de un array.  
- `np.percentile(arr, [q1, q2, …])` — Calcular valores de percentiles específicos (ej: 25th, 50th, 75th, 95th).  
- `np.histogram(arr, bins=…)` — Obtener distribución de frecuencias en bin’s para análisis de colas.  

---

## Ejercicio: Análisis temporal / hora del día / fecha  
### pandas

- `pd.to_datetime()` — Conversión a tipo fecha/hora.  
- `df.set_index('date')` — Fijar la columna de fecha como índice.  
- `df.resample(rule='H')`, `df.resample(rule='D')` — Re-muestreo por hora, día …  
- `df['date'].dt.hour`, `df['date'].dt.month`, `df['date'].dt.year` — Extraer componentes temporal.  

### NumPy

- `np.diff(arr)` — Diferencia entre valores consecutivos, útil en series temporales.  
- Uso de arrays de tiempos convertidos a números (timestamp) y operaciones vectorizadas.

---

## Ejercicio: Rendimiento histórico / acumulados / rentabilidad

### pandas

- `df['return_daily'] = df['close'] / df['close'].shift(1) - 1` — Crear columna de rendimiento diario.  
- `df['cum_return'] = (1 + df['return_daily']).cumprod() - 1` — Rendimiento acumulado desde el inicio.  
- `df.groupby('symbol')['cum_return'].last()` — Obtener último valor de rendimiento acumulado por símbolo.  

### NumPy

- `np.cumprod(arr)` — Acumulado de multiplicaciones, útil para crecimiento compuesto.  
- `np.log(arr)` — Logaritmo de rendimientos si se hace análisis de crecimiento logarítmico.  
- `np.diff(arr) / arr[:-1]` — Alternativa manual para rendimiento diario en arrays.

---

## Ejercicio: Comparaciones entre grupos / símbolos / categorías  

### pandas

- `df.groupby('category').agg({...})` — Agrupar por categoría y calcular múltiples métricas.  
- `df.sort_values(by='metric', ascending=False)` — Ordenar grupos según métrica para ranking.  
- `pd.merge(df1, df2, how='inner', on='key')` — Unir dos DataFrames con información distinta.  
- `df.pivot_table(index='group', columns='subgroup', values='value', aggfunc='mean')` — Tabla dinámica de comparaciones.

### NumPy

- `np.corrcoef(arr1, arr2)` — Matriz de correlación entre arrays, útil para relación entre métricas de grupos.  
- `np.argsort(arr)` — Obtener orden de valores para ranking.  
- `np.where(condition)` — Identificar índices que cumplen una condición, útil para filtrar grupos especiales.
