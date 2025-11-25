# Funciones a utilizar: pandas y NumPy

Organizadas por ejercicio tipo como referencia de qué métodos pueden usar.

## Carga CSV / Gestión de valores NA / Limpieza de datos

- `pd.read_csv()` — Leer fichero CSV.  
- `df.info()` — Información de tipos, no nulos, etc. 
- `df.describe()` — Estadísticas descriptivas de columnas numéricas.  
- `df.isna()` / `df.isnull()` — Detectar valores nulos.  [ejemplo](pildoras/pildora_relleno_valores.md)
- `df.notna()` / `df.notnull()` — Detectar valores no nulos.  
- `df.dropna()` — Eliminar filas/columnas con valores nulos.  
- `df.fillna(value=…)` — Rellenar valores nulos con un valor especificado.  
- `df['new_col'] = …. ` — Crear una nueva columna con asignación directa.  
- `df.assign(new_col = …)` — Crear columna adicional mediante método assign.  
- `df.sort_values(by='col', ascending=…)` — Ordenar el DataFrame según una columna.  
- `df.rename(columns={…})` — Renombrar columnas.  
- `pd.to_numeric()` — Convertir columna a tipo numérico.   [ejemplo](pildoras/pildora_coerce.md)
- `pd.to_datetime()` — Convertir columna a tipo fecha/hora.  [ejemplo](pildoras/pildora_to_datetime.md)
- `df.astype(type)` — Cambiar tipo de una columna, por ejemplo a `float`, `int`.  [ejemplo](pildoras/pildora_astype.md)
- `np.array()` — Crear un array NumPy, útil cuando se extraen datos de un DataFrame.  [ejemplo](pildoras/pildora_numpy.md)  
- `arr.astype(new_type)` — Cambiar el tipo de un array, por ejemplo de float a int.  
- `np.isnan(arr)` — Detectar valores NaN en un array.  
- `np.where(condition, x, y)` — Crear un array nuevo basado en una condición (útil para imputación condicional).  
- Operaciones vectorizadas: por ejemplo `arr1 / arr2`, `np.log(arr)`, `np.power(arr,2)` — aplicadas a arrays derivados de pandas.  
- `np.cumsum(arr)` — Suma acumulativa, puede servir para series de tiempo.  
- `np.cumprod(arr)` — Producto acumulativo, útil para cálculos de crecimiento.  
- `np.argsort(arr)` — Obtener índices que ordenarían el array, útil para extraer top/bottom grupos.
---

## Agrupaciones (groupby) / Agregaciones 

[ejemplo](pildoras/pildora_group_by.md)

- `df.groupby('col')` — Agrupar por una o varias columnas.  
- `.agg()` — Aplicar múltiples funciones de agregación tras groupby, por ejemplo `.agg({'col1':'sum','col2':'mean'})`.  
- `.sum()` / `.mean()` / `.count()` — Funciones de agregación comunes.  
- `df.value_counts()` — Contar frecuencia de valores únicos en una columna.  
- `df.nunique()` — Número de valores únicos en una columna.

## Estadística básica y percentiles / outliers

[ejemplo](pildoras/pildora_percentiles.md)

- `df.describe()` — Ver estadísticas principales (mean, std, min, max, quartiles).  
- `df.median()` — Mediana de una columna.  
- `df.std()` — Desviación estándar de una columna.  
- `df.min()` / `df.max()` — Mínimo/máximo.  
- `df.quantile(q)` — Cuantil para una columna (por ejemplo 0.95 para percentil 95).  
- `np.mean(arr)`, `np.median(arr)`, `np.std(arr)` — Media, mediana, desviación estándar de un array.  
- `np.percentile(arr, [q1, q2, …])` — Calcular valores de percentiles específicos (ej: 25th, 50th, 75th, 95th).  
- `np.histogram(arr, bins=…)` — Obtener distribución de frecuencias en bin’s para análisis de colas.  

---

## Análisis temporal / hora del día / fecha

[ejemplo](pildoras/pildora_resample.md)

- `pd.to_datetime()` — Conversión a tipo fecha/hora.  
- `df.set_index('date')` — Fijar la columna de fecha como índice.  
- `df.resample(rule='H')`, `df.resample(rule='D')` — Re-muestreo por hora, día …  
- `df['date'].dt.hour`, `df['date'].dt.month`, `df['date'].dt.year,df['date'].dt.weekday` — Extraer componentes temporal.  

---

## Rendimiento histórico / acumulados / rentabilidad  
[ejemplo](pildoras/pildora_numpy.md)

- `df['return_daily'] = df['close'] / df['close'].shift(1) - 1` — Crear columna de rendimiento diario.  
- `df['cum_return'] = (1 + df['return_daily']).cumprod() - 1` — Rendimiento acumulado desde el inicio.  
- `df.groupby('symbol')['cum_return'].last()` — Obtener último valor de rendimiento acumulado por símbolo.  
- `np.cumprod(arr)` — Acumulado de multiplicaciones, útil para crecimiento compuesto.  
- `np.log(arr)` — Logaritmo de rendimientos si se hace análisis de crecimiento logarítmico.  
- `np.diff(arr) / arr[:-1]` — Alternativa manual para rendimiento diario en arrays.

---

## Comparaciones entre grupos / símbolos / categorías  

- `df["COLUMNA"].astype("category")` -Una **variable categórica** es aquella que toma un número limitado y fijo de valores, que representan categorías o niveles.  
- `df.get_dummies()` - One‑Hot Encoding transforma variables categóricas en columnas binarias.
- `df.groupby('category').agg({...})` — Agrupar por categoría y calcular múltiples métricas.   [ejemplo](pildoras/pildora_categorical.md)
- `pd.merge(df1, df2, how='inner', on='key')` — Unir dos DataFrames con información distinta.   [ejemplo](pildoras/pildora_merge.md)
- `df.pivot_table(index='group', columns='subgroup', values='value', aggfunc='mean')` — Tabla dinámica de comparaciones. [ejemplo](pildoras/pildora_pivot_table.md)
- `np.corrcoef(arr1, arr2)` — Matriz de correlación entre arrays, útil para relación entre métricas de grupos. [ejemplo](pildoras/pildora_correlacion.md)
