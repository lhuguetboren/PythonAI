# Análisis de datos con Pandas y NumPy  
**Dataset**: historial de reproducción de Spotify  
> Variables: `spotify_track_uri`, `ts`, `platform`, `ms_played`, `track_name`, `artist_name`, `album_name`, `reason_start`, `reason_end`, `shuffle`, `skipped`

---

## 1. Imports & configuración

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV (pista: parsear la columna `ts` como datetime).  
- Mostrar las primeras filas, `df.info()`, `df.describe()` para entender los tipos de variables y la extensión de los datos.

---

## 3. Limpieza y preparación de datos

- Verificar el tipo de la columna `ts` y convertirla a `datetime`.  
- Convertir `ms_played` a segundos o minutos para análisis más intuitivo (por ejemplo `minutes_played = ms_played / 60000`).  
- Verificar valores nulos, duplicados o datos erróneos en `ms_played` (por ejemplo valores = 0).  
- Convertir variables categóricas apropiadamente (`platform`, `reason_start`, `reason_end`, `shuffle`, `skipped`).  
- Crear columnas adicionales útiles: por ejemplo hora del día (`hour = ts.hour`), día de la semana (`weekday = ts.weekday()`), etc.


## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Número total de registros de reproducción.  
- Estadísticas de `ms_played` (o `minutes_played`): media, mediana, desviación estándar, mínimo, máximo.  
- ¿Cuántos tracks fueron “skip” (`skipped == TRUE`) vs completados?  
- ¿Cuántas sesiones con shuffle activado (`shuffle == TRUE`)?

### 4.2 Distribución por artista / álbum / pista

- Agrupar por `artist_name` para obtener:  
  - número de reproducciones (`count`)  
  - tiempo total reproducido (`sum(minutes_played)`)  
  - media de tiempo reproducido por sesión de ese artista.  
- Similarmente agrupar por `album_name` y por `track_name` para identificar pistas más reproducidas o con mayor tiempo.

### 4.3 Análisis temporal

- Extraer hora del día (`hour`) y agrupar para ver en qué horas se escuchan más tracks (o se reproducen más minutos).  
- Agrupar por día de la semana (`weekday`) para ver patrones de escucha semanal.  
- Comparar plataformas (`platform`) o si estaba activado shuffle (`shuffle`) para ver diferencias de tiempo escuchado o saltos (`skipped`).

### 4.4 Comportamiento de saltos (skipped)

- Calcular porcentaje de tracks saltados (`skipped == TRUE`) respecto del total.  
- Agrupar por `reason_start` o `reason_end` para ver qué motivos están asociados a saltos o reproducciones completas.  
- Verificar si hay diferencia en `minutes_played` entre pistas que se saltan vs que se escuchan completas.

## 5. Uso de NumPy para análisis auxiliar

- Usar `np.percentile` para calcular percentiles de `minutes_played` (por ejemplo 25th, 50th, 75th, 95th).  
- Usar `np.histogram` u otros métodos de NumPy para visualizar la distribución de tiempo reproducido.  
- Analizar correlaciones o relaciones: por ejemplo, relación entre `minutes_played` y probabilidad de ser saltada (`skipped`) o shuffle activado.

---

## 6. Preguntas para los alumnos

1. ¿Cuál artista acumula más tiempo de escucha en total? ¿Y cuál pista?  
2. ¿En qué hora del día y en qué día de la semana se realiza la mayor parte de la escucha? ¿Hay diferencias entre plataformas o uso de shuffle?  
3. ¿Cuál es el porcentaje de saltos (`skipped == TRUE`)? ¿Qué motivos de inicio (`reason_start`) o fin (`reason_end`) están más asociados a saltos?  
4. ¿Existen pistas que suelen reproducirse más tiempo (high minutes_played) y rara vez se saltan? ¿Cuáles son y por qué crees que lo son?
