# Análisis de datos con Pandas y NumPy

**Dataset**: películas  
> Variables: `movie_title`, `movie_info`, `critics_consensus`, `rating`, `genre`, `directors`, `writers`, `cast`, `in_theaters_date`, `on_streaming_date`, `runtime_in_minutes`, `studio_name`, `tomatometer_status`, `tomatometer_rating`, `tomatometer_count`, `audience_rating`, `audience_count`

---

## 1. Imports & configuración

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV correspondiente.  
- Mostrar las primeras filas, información general (`.info()`), estadístico básico (`.describe()` para numéricas).  
- Verificar tipos de datos: por ejemplo `in_theaters_date`, `on_streaming_date` → tipo fecha; `runtime_in_minutes`, `tomatometer_rating`, `audience_rating`, `tomatometer_count`, `audience_count` → numéricas.

---

## 3. Limpieza y preparación de datos  

- Convertir `in_theaters_date` y `on_streaming_date` a tipo datetime.  
- Verificar valores nulos o faltantes en campos clave (por ejemplo fechas, ratings).  
- Normalizar el campo `genre` si contiene múltiples géneros (por ejemplo separar en lista, o elegir género principal).  
- (Opcional) Extraer del campo `rating` o `studio_name` o `tomatometer_status` algunas categorías limpias.  
- Crear columnas derivadas que puedan facilitar el análisis, por ejemplo:  
  - `days_to_streaming = on_streaming_date - in_theaters_date` (número de días entre estreno en cines y streaming)  
  - `is_certified_fresh = tomatometer_status == "Certified Fresh"` (booleano)  
  - `total_votes = tomatometer_count + audience_count` (suma simple)  

---

## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Calcular la media, mediana, desviación estándar, mínimo/máximo de variables numéricas: `runtime_in_minutes`, `tomatometer_rating`, `audience_rating`, `tomatometer_count`, `audience_count`, `days_to_streaming`.  
- Contar cuántas películas hay, cuántos estudios distintos (`studio_name`), cuántos directores distintos (`directors`).  

### 4.2 Análisis por género

- Agrupar por `genre` para calcular:  
  - número de películas  
  - duración media (`runtime_in_minutes`)  
  - rating medio de críticos (`tomatometer_rating`)  
  - rating medio de audiencia (`audience_rating`)  

- Ordenar géneros de mayor a menor según rating medio de audiencia.  
- Reflexionar: ¿qué géneros tienden a obtener mejores valoraciones de audiencia? ¿Y de críticos?

### 4.3 Análisis por estudio o director

- Agrupar por `studio_name` (o por `directors`) y calcular:  
  - número de películas  
  - rating medio de audiencia y de críticos  
  - duración media  
- Identificar qué estudios o directores tienen mejores resultados de audiencia y si coinciden con los de críticos.

### 4.4 Análisis temporal

- Usando `in_theaters_date`, extraer el año de estreno (`year = in_theaters_date.year`).  
- Agrupar por año para calcular:  
  - número de películas por año  
  - rating medio de audiencia por año  
- (Opcional) Visualizar la tendencia a lo largo del tiempo: ¿ha mejorado el rating de audiencia en los últimos años?

### 4.5 Análisis de retraso a streaming (si aplica)

- Usar la columna `days_to_streaming` (calculada) para ver distribución del retraso entre estreno en cines y streaming.  
- Verificar si existe relación entre `days_to_streaming` y `audience_rating` o `tomatometer_rating`: ¿las películas que llegan más rápido a streaming tienen mejor audiencia?  
  - Puedes utilizar `np.corrcoef()` para ver correlación.

---

## 5. Uso de NumPy para análisis auxiliar

- Usar `np.percentile()` para calcular percentiles de variables como `runtime_in_minutes`, `audience_rating` o `tomatometer_rating`, y detectar películas “fuera de lo común” (por ejemplo muy largas o con rating muy bajo).  
- Usar funciones vectorizadas de NumPy para comparar dos arrays: por ejemplo calcular la diferencia `audience_rating - tomatometer_rating` y ver su media y desviación.  
- Crear histogramas o distribuciones de alguna variable relevante (duración, rating) usando NumPy.

---

## 6. Preguntas

1. ¿Qué género tiene el rating medio de audiencia más alto y cuál el más bajo?  
2. ¿Hay diferencias significativas entre el rating de los críticos (`tomatometer_rating`) y el de la audiencia (`audience_rating`)? Por ejemplo, ¿qué películas tienen una gran disparidad entre ambos?  
3. ¿Cuál estudio produce las películas con duración media más alta? ¿Y cuál las que tienen mejor rating de audiencia medio?  
4. ¿Ha cambiado la duración promedio de las películas a lo largo de los años? ¿Ha cambiado también el rating medio de audiencia?  
5. ¿Existe alguna relación entre el retraso hasta streaming (`days_to_streaming`) y el rating de audiencia? ¿Las películas que llegan más rápido al streaming obtienen mejores valoraciones?  