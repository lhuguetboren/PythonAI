# Análisis de datos con Pandas y NumPy

**Dataset**: informes de avistamientos de objetos voladores no identificados (OVNIs)  
> Variables: `datetime`, `city`, `state`, `country`, `shape`, `duration (seconds)`, `duration (hours/min)`, `comments`, `date posted`, `latitude`, `longitude`

## 1. Imports & configuración

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV (pista: parsear la columna `datetime` como tipo fecha-hora).  
- Mostrar las primeras filas, `df.info()`, `df.describe()` para entender los tipos y el contenido de las variables.

## 3. Limpieza y preparación de datos

- Verificar que `datetime` está correctamente convertido a `datetime64`.  
- Convertir la columna `duration (seconds)` a tipo numérico.  
- Posiblemente extraer minutos/hours de la columna `duration (hours/min)` o crear una columna de duración estándar en minutos.  
- Verificar y tratar valores nulos o inconsistentes (ej: latitud/longitud vacías).  
- Convertir columnas categóricas adecuadas (`country`, `shape`).  
- Crear columnas adicionales útiles: por ejemplo `year` = año del avistamiento, `month`, `hour` del día.

## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Número total de informes de avistamientos.  
- Duración media, mediana, mínima y máxima de los eventos (`duration (seconds)` o estandarizada).  
- ¿Cuántos países distintos (`country`) y estados (`state`) están involucrados?

### 4.2 Distribución por forma (`shape`)

- Agrupar por `shape` para calcular:  
  - número de informes  
  - duración media de los avistamientos  
- Ordenar de mayor a menor por número de informes o por duración media.  
- Reflexionar: ¿qué forma de objeto es la más común? ¿Hay formas asociadas a avistamientos de mayor duración?

### 4.3 Distribución geográfica

- Agrupar por `country` (y si aplica por `state`) para ver cuántos informes por país/estado.  
- Ver latitud/longitud para posibles agrupamientos geográficos (“hotspots”).  
- (Opcional) Visualización sobre mapa de los puntos de avistamiento.

### 4.4 Análisis temporal

- Usar la columna `datetime` + nuevas columnas `year`, `month`, `hour` para:  
  - Ver evolución del número de informes por año o por mes.  
  - Ver a qué hora del día ocurren más avistamientos.  
- Comparar duración de los avistamientos según hora/día.

### 4.5 Relación entre duración y otros factores

- Ver si la duración del avistamiento (`duration (seconds)`) varía según la forma (`shape`) o el país (`country`).  
- Posible correlación: duración vs latitud/longitud (por ejemplo, ¿los avistamientos en ciertos estados duran más?).

## 5. Uso de NumPy para análisis auxiliar

- Utilizar `np.percentile` para calcular percentiles de la duración de los avistamientos (por ejemplo 25th, 50th, 75th, 95th).  
- Crear histogramas o distribuciones de duración para entender la “cola” de avistamientos largos.  
- Usar NumPy para operaciones vectorizadas si fuera necesario (por ejemplo convertir segundos a minutos: `minutes = duration_seconds / 60`).

## 6. Preguntas

1. ¿Cuál forma de objeto (`shape`) se reporta con mayor frecuencia? ¿Y cuál tiene la mayor duración media de avistamiento?  
2. ¿En qué país (o estado, si se considera) ocurren más informes de avistamientos?  
3. ¿Cómo ha evolucionado el número de informes de avistamientos por año o por década?  
4. ¿Cuál es el percentil 95 de la duración de los eventos? ¿Cuántos informes superan ese valor?
