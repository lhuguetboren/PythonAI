# Análisis de datos con Pandas y NumPy

**Dataset**: vinos  
> Variables: `id`, `country`, `description`, `designation`, `points`, `price`, `province`, `region_1`, `region_2`, `taster_name`, `taster_twitter_handle`, `title`, `variety`, `winery`


## 1. Imports & configuración

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV correspondiente.  
- Mostrar las primeras filas, información general (`.info()`), estadístico básico para variables numéricas.  
- Verificar tipos de datos: por ejemplo `points`, `price` → numéricos; `country`, `province`, `variety`, `winery` → strings; `description` → texto.

---

## 3. Limpieza y preparación de datos

- Convertir `price` a numérico si no lo es (puede haber valores faltantes).  
- Verificar valores nulos o faltantes (por ejemplo `taster_twitter_handle`, `region_2`, `price`).  
- Normalizar/limpiar columnas de texto si es relevante (por ejemplo quitar espacios en `variety`, unificar mayúsculas/minúsculas en `country`).  
- Crear columnas derivadas que puedan facilitar el análisis, por ejemplo:  
  - `has_price = price.notnull()` (booleano si el vino tiene precio registrado)  
  - `review_length = description.str.len()` (longitud del texto de descripción)  
  - `region_combined = region_1.fillna('') + ' / ' + region_2.fillna('')` (combinación de regiones si aplica)

## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Calcular la media, mediana, desviación estándar, mínimo/máximo de variables numéricas: `points`, `price`, `review_length`.  
- Contar cuántos registros hay, cuántos países distintos (`country`), cuántas bodegas distintas (`winery`).

### 4.2 Análisis por país o provincia

- Agrupar por `country` (o `province`) para calcular:  
  - número de vinos registrados  
  - precio medio (`price`)  
  - puntuación media (`points`)  
- Ordenar países de mayor a menor según puntuación media o precio medio.  
- Reflexionar: ¿qué países destacan en precio vs. puntuación?

### 4.3 Variedad de uva (`variety`)

- Agrupar por `variety` para calcular:  
  - número de vinos  
  - puntuación media (`points`)  
  - precio medio (`price`)  
- Identificar las variedades con mayor puntuación media, y las que están por debajo del promedio.

### 4.4 Relación entre precio y puntuación

- Verificar si los vinos con mayor `points` tienden a tener mayor `price`.  
- Crear una nueva columna `price_per_point = price / points` (solo donde `price` no está nulo) y analizar su distribución.  
- Verificar correlación entre `price` y `points` usando NumPy (por ejemplo `np.corrcoef()`).

### 4.5 Análisis de longitud de reseña

- Verificar distribución de `review_length` (longitud de la descripción).  
- Ver si existe relación entre `review_length` y `points` o `price`: por ejemplo, ¿las descripciones largas corresponden a vinos mejor puntuados?


## 5. Uso de NumPy para análisis auxiliar

- Usar `np.percentile()` para calcular percentiles de `price`, `points`, `price_per_point` y detectar valores atípicos.  
- Utilizar funciones vectorizadas de NumPy para operaciones en arrays, por ejemplo calcular diferencia `price - median_price` o proporción respecto al precio medio.  
- Crear histogramas o distribuciones de variables como `price`, `points` o `price_per_point` usando NumPy.


## 6. Preguntas

1. ¿Qué país tiene los vinos con mayor puntuación media (`points`) y cuál tiene los más bajos?  
2. ¿Existe una relación clara entre `price` y `points`? ¿Dónde están los vinos con precio alto pero puntuación baja o con puntuación alta pero precio bajo?  
3. ¿Qué variedad (`variety`) de uva presenta una puntuación media más alta? ¿Y cuál la más baja?  
4. ¿Qué porcentaje de vinos no tienen precio (`price` nulo)? ¿Cómo afecta eso al análisis y qué recomendarías hacer al respecto?  
5. ¿Los vinos con descripciones más largas (`review_length`) reciben mejores puntuaciones o tienen mayor precio? Analízalo.  
