# Ejercicio: Análisis histórico de enfrentamientos internacionales y probabilidades de victoria  
**Datasets**:  
- **CSV 1**: `international_matches.csv`  
  > Columnas: `ID`, `Tournament`, `Date`, `Home Team`, `Home Goals`, `Away Goals`, `Away Team`, `Win Conditions`, `Home Stadium`  
- **CSV 2**: `2022_world_cup_matches.csv`  
  > Columnas: `ID`, `Year`, `Date`, `Stage`, `Home Team`, `Away Team`, `Host Team`  

En este ejercicio se pide combinar estos datos con información adicional de los continentes a los que pertenecen los equipos y luego asignar una probabilidad de victoria basada en los históricos.

---

## 1. Carga de los datos  
- Cargar el CSV 1 (`international_matches.csv`) asegurando que `Date` se convierta a formato fecha.  
- Cargar el CSV 2 (`2022_world_cup_matches.csv`) asegurando también `Date` como fecha.  
- Revisar la estructura de ambos dataframes (tipos de datos, primeras filas) para familiarizarse con los datos.

---

## 2. Limpieza y preparación de datos  
- En el dataframe de CSV 1 asegurar que las columnas de goles (`Home Goals`, `Away Goals`) sean numéricas.  
- Crear en ese dataframe al menos estas dos nuevas variables:  
  - `goal_diff = Home Goals − Away Goals` (ventaja del equipo local)  
  - `total_goals = Home Goals + Away Goals` (goles totales del partido)  
- Verificar y eliminar filas con datos faltantes críticos (por ejemplo en `Home Goals`, `Away Goals`, o `Date`).  
- En el dataframe CSV 2, revisar que las columnas estén consistentes, y que puedas identificar claramente el equipo local (`Home Team`) y visitante (`Away Team`).

---

## 3. Preparación de datos adicionales y merge  
- Crear un nuevo CSV o DataFrame auxiliar (`teams_info.csv`) con información de los equipos nacionales, al menos con columnas: `Team`, `Continent`. Puedes crear este fichero manualmente con los equipos que aparecen en los datasets.  
- Realizar un merge entre el dataframe de CSV 1 y `teams_info` para añadir el continente del equipo local (`Home Team`).  
- También hacer un merge (o unión similar) para añadir el continente del equipo visitante (`Away Team`). Esto te permitirá tener, en cada fila de partido, el continente del equipo local y del visitante.  
- A continuación, combinar los datos del CSV 2 con el merge obtenido, para tener una vista histórica más amplia que cubre los partidos del Mundial 2022 y los enfrentamientos previos.

---

## 4. Cálculo de probabilidades de victoria basada en histórico  
- Usar el dataframe combinado para calcular, por cada par equipo local-visitante (o por continente local-continente visitante), la frecuencia de victorias del equipo local.  
  - Por ejemplo: agrupar por `Home Team`, `Away Team` y calcular: número de partidos, número de victorias locales (condición `Home Goals > Away Goals`), número de empates, número de victorias visitantes.  
  - Calcular la probabilidad `P_local_win = (victorias locales) / (número de partidos)`  
- Crear una nueva columna en el dataframe con esta probabilidad (por ejemplo `prob_local_win`).  
- Alternativamente, calcular la probabilidad de victoria según continentes: agrupar por `Continent_home`, `Continent_away` y calcular la proporción de victorias del equipo local según continente-visitante.

---

## 5. Análisis exploratorio  
- Ver cuáles equipos locales tienen mayor o menor probabilidad de victoria histórica.  
- Ver si existe alguna ventaja significativa según continente vs continente (por ejemplo, equipos de Europa vs África, etc.).  
- Analizar si los partidos del Mundial 2022 (CSV 2) repiten patrones históricos en términos de ventaja local o no.  
- Calcular la media y desviación estándar de la probabilidad de victoria para ver la dispersión entre equipos.

---

## 6. Visualización  
- Crear un histograma de las probabilidades de victoria (`prob_local_win`) para ver su distribución.  
- Crear un gráfico de barras de los 10 equipos con mayor `prob_local_win`.  
- Crear una matriz (heatmap) de probabilidades de victoria entre continentes (`Continent_home` vs `Continent_away`).  
- (Opcional) Crear una línea temporal para un equipo específico que muestre cómo ha cambiado su probabilidad de victoria local a lo largo del tiempo.

---

## 7. Preguntas para los alumnos  
1. ¿Qué equipos tienen históricamente la probabilidad más alta de ganar en casa? ¿Y los más débiles?  
2. ¿Se observa una ventaja local más pronunciada en ciertos continentes?  
3. ¿La variabilidad de la probabilidad de ganar (`std`) es alta o baja entre equipos? ¿Qué implica esto?  
4. ¿Los resultados del Mundial 2022 confirman o contradicen el patrón histórico de ventaja local que han calculado?  
5. ¿Cómo cambiaría la probabilidad de victoria si sólo consideras los últimos 10 años de enfrentamientos en lugar de todo el histórico?

---

## 8. Entrega  
- Un notebook (.ipynb) que:  
  - Contenga carga de los dos CSV, limpieza, transformación, unión de datos.  
  - Incluya análisis exploratorio, visualizaciones y respuestas a las preguntas.  
- Dentro del notebook incluir una sección en Markdown con tus conclusiones.  
- Exportar (opcional) un CSV resumen con: `Home Team`, `Away Team`, `matches_played`, `prob_local_win`.

---

¡Ready para que los alumnos trabajen con **dos CSV**, integren datos y realicen un análisis avanzado del histórico de enfrentamientos y probabilidades de victoria!
