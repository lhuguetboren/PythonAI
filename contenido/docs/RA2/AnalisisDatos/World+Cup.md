# Ejercicio: Análisis de los partidos del Mundial 2022 con datos auxiliares  

**Dataset principal**: Partidos del Mundial 2022  
> Columnas principales del CSV 1: `MatchID`, `Date`, `Home Team`, `Away Team`, `Home Goals`, `Away Goals`, `Win Conditions`, `Stadium`, etc.  
**Dataset complementario**: Información de equipos o selecciones (CSV 2)  
> Columnas típicas del CSV 2: `Team`, `Continent`, `FIFA_Rank`, `Group`, u otras variables relevantes.

---

## 1. Carga de los datos

- Cargar el **CSV 1** con los partidos del Mundial 2022.  
- Cargar el **CSV 2** con información de los equipos/secciones.  
- Verificar estructura, tipos de datos y primeras filas de ambos.

---

## 2. Limpieza y preparación de datos

- En el DataFrame de partidos asegurar que `Home Goals`, `Away Goals` son numéricos.  
- Crear en ese DataFrame nuevas columnas:  
  - `goal_diff = Home Goals − Away Goals`  
  - `total_goals = Home Goals + Away Goals`  
- Verificar y eliminar filas del CSV 1 con datos faltantes en columnas clave (`Home Goals`, `Away Goals`, `Date`).  
- En el CSV 2, revisar que las columnas como `FIFA_Rank` o `Continent` tengan el tipo correcto o limpiarlas según sea necesario.

## 3. Extracción de componentes de fecha (en CSV 1)

- A partir de la columna `Date`, en el DataFrame de partidos extraer: año, mes, día de la semana.

---

## 4. Integración de los dos CSV

- Hacer un `merge` entre los partidos (CSV 1) y la información del equipo local o visitante (CSV 2). Por ejemplo, unir sobre `Home Team = Team`.  
- Verificar que tras la unión dispones de variables como `Continent`, `FIFA_Rank` para el equipo local.

---

## 5. Análisis exploratorio combinado

- Calcular la media de goles por partido (`total_goals`).  
- Calcular la media y desviación estándar de `goal_diff` para evaluar cuán equilibrados son los partidos.  
- Agrupar por `Continent` del equipo local (dato extraído del CSV 2) para calcular media, desviación estándar y número de partidos de `goal_diff`.  
- Calcular la correlación entre `FIFA_Rank` del equipo local y `goal_diff`, para ver si ranking más bajo (mejor equipo) se asocia a ventaja de goles.

---

## 6. Visualización / Histogramas

- Histograma de la diferencia de goles (`goal_diff`).  
- Histograma del total de goles por partido (`total_goals`).  
- (Opcional) Realizar visualización de ventaja de goles vs ranking: dispersión `FIFA_Rank` vs `goal_diff`.

---

## 7. Preguntas

1. ¿La diferencia de goles (`goal_diff`) tiene una desviación estándar alta o baja? ¿Qué nos dice sobre la igualdad de los partidos?  
2. ¿Existen diferencias entre continentes en cuanto a ventaja de goles de los equipos locales?  
3. ¿Cuál es la correlación entre el ranking FIFA del equipo local y su ventaja de goles? ¿Qué implica?  
4. ¿En qué mes o día de la semana se anotan más goles por partido? ¿Y mayor variabilidad?  
5. ¿Qué conclusiones puedes extraer de los histogramas del total de goles y de la diferencia de goles?
