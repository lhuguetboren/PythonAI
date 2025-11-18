# Análisis de datos con Pandas y NumPy

**Dataset**: ventas de videojuegos  
> Variables: `img`, `title`, `console`, `genre`, `publisher`, `developer`, `critic_score`, `total_sales`, `na_sales`, `jp_sales`, `pal_sales`, `other_sales`, `release_date`, `last_update`


## 1. Imports & configuración

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV correspondiente.  
- Mostrar las primeras filas, `.info()`, `.describe()` para las variables numéricas.  
- Verificar tipos de datos: por ejemplo convertir `release_date` (y `last_update` si la usas) en tipo fecha.

## 3. Limpieza y preparación de datos

- Convertir `release_date` a tipo datetime. Si `last_update` es fecha, convertirlo también.  
- Verificar valores nulos/faltantes en columnas clave, por ejemplo `critic_score`, `total_sales`.  
- Corregir formatos si fuese necesario (por ejemplo `total_sales`, `na_sales`, etc tienen coma decimal u otro formato).  
- Crear columnas derivadas que puedan facilitar el análisis, por ejemplo:  
  - `regional_sales_sum = na_sales + jp_sales + pal_sales + other_sales` (validar que suma ≈ total_sales)  
  - `sales_na_pct = na_sales / total_sales` (porcentaje de ventas en Norteamérica)  
  - `age_days_since_release = (última_fecha_de_datos – release_date).days` (opcional)

## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Calcular estadísticos (media, mediana, desviación estándar, mínimo, máximo) para `critic_score`, `total_sales`, `na_sales`, `jp_sales`, `pal_sales`, `other_sales`.  
- Contar cuántos videojuegos hay, cuántas consolas distintas (`console`), cuántos géneros (`genre`) distintos.

### 4.2 Distribución por consola/plataforma

- Agrupar por `console` para calcular:  
  - número de juegos  
  - ventas totales (`sum(total_sales)`)  
  - puntuación media de crítica (`mean(critic_score)`)  
- Ordenar consolas de mayor a menor según ventas totales.  
- Reflexionar: ¿qué consolas dominan ventas? ¿Y cuál tiene mejor puntuación media crítica?

### 4.3 Análisis por género

- Agrupar por `genre` para calcular:  
  - número de juegos  
  - ventas totales  
  - puntuación media de críticos  
- Identificar géneros con mejores resultados de ventas y mejores críticas.

### 4.4 Análisis por región de ventas

- Usar `na_sales`, `jp_sales`, `pal_sales`, `other_sales` para calcular la proporción de ventas por región del total.  
- Comparar las proporciones entre los top videojuegos (por ventas) o por género/consola.  
- Por ejemplo: ¿qué porcentaje de ventas se hace en Japón para los juegos de género “Action”? ¿Y en Europa (PAL)?

### 4.5 Relación entre puntuación crítica y ventas

- Verificar si existe correlación entre `critic_score` y `total_sales` usando NumPy (`np.corrcoef`).  
- Crear scatter-plot (opcional) de `critic_score` vs `total_sales`, para ver si los juegos mejor puntuados venden más.  
- Identificar juegos que tienen puntuación alta pero ventas bajas, o ventas altas pero puntuación baja — analizar posibles causas.

## 5. Uso de NumPy para análisis auxiliar

- Utilizar `np.percentile()` para calcular percentiles de `total_sales` y detectar juegos outliers (por ejemplo > 90 percentil).  
- Crear arrays con ventas regionales para comparar media, mediana, desviación con NumPy.  
- Usar funciones vectorizadas de NumPy para calcular nuevas métricas rápidamente (por ejemplo múltiplos o ratios de ventas por región).

## 6. Preguntas para los alumnos

1. ¿Qué consola tiene la mayor venta total de juegos en el dataset? ¿Y cuál la mejor puntuación media de crítica?  
2. ¿Qué género de juego tiene mayor venta total? ¿Y cuál tiene mayor puntuación crítica media?  
3. ¿Qué juego tiene la mayor proporción de ventas en una región específica (por ejemplo Japón) vs el total?  
4. ¿Existe una correlación significativa entre la puntuación de crítica (`critic_score`) y las ventas totales (`total_sales`)? ¿Qué juegos se desvían de la tendencia?  
5. Usa NumPy para identificar los juegos que están en el percentil 90 o superior de ventas totales y comenta: ¿qué características comunes tienen (género, consola, desarrollador, etc.)?  