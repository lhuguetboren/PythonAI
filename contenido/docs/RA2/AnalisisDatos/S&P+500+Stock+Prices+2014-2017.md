# Análisis de datos financieros con Pandas y NumPy

**Dataset**: histórico de precios de acciones  
> Variables: `symbol`, `date`, `open`, `high`, `low`, `close`, `volume`

---

## 1. Imports & configuración  

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV (‘symbol’, ‘date’, ‘open’, ‘high’, ‘low’, ‘close’, ‘volume’).  
- Convertir `date` al tipo `datetime`.  
- Mostrar `df.head()`, `df.info()`, `df.describe()` para entender estructura y tipos.

---

## 3. Limpieza y preparación de datos

- Verificar valores nulos o datos faltantes.  
- Asegurar que `close`, `open`, `volume` están como tipos numéricos.  
- Ordenar los datos por `symbol` y `date`.  
- Crear columnas nuevas útiles:  
  - Rendimiento diario simple  
  - Rendimiento acumulado: calcular crecimiento de inversión desde inicio.
- Filtrar fechas, símbolos o periodos para análisis.

---

## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Número total de registros, número de símbolos (`symbol`).  
- Estadísticas de rendimiento diario (`return_daily`): media, mediana, desviación estándar.  
- Volumen medio de negociación.

### 4.2 Distribución de rendimientos por símbolo

- Agrupar por `symbol` para calcular:  
  - rendimiento medio diario  
  - volatilidad (desviación estándar) diaria  
  - crecimiento acumulado al final del periodo  
- Ordenar símbolos por rendimiento acumulado o mayor volatilidad.

### 4.3 Gráficos de evolución y rentabilidad

- Para cada símbolo (o algunos seleccionados) graficar la serie de cierre (`close`) vs evolución del rendimiento acumulado.  
- Graficar histograma del rendimiento diario para ver distribución, colas, outliers.

### 4.4 Comparación entre símbolos

- Comparar crecimiento acumulado de varios símbolos (por ejemplo 5-10 símbolos) en un mismo gráfico para ver cuál “ganó” más durante el periodo.  
- Analizar relación entre rendimiento medio y volatilidad: símbolos con mayor rendimiento también tienen mayor riesgo?

---

## 5. Uso de NumPy para análisis auxiliar

- Usar `np.diff()` + división para calcular rendimientos simples manualmente como array. :contentReference[oaicite:5]{index=5}  
- Calcular percentiles de rendimiento diario (por ejemplo percentil 95) para ver extremos de rendimiento.  
- Usar `np.cumprod()` (o en pandas `cumprod()`) para calcular crecimiento de inversión

---

## 6. Preguntas

1. ¿Qué símbolo tiene el mayor rendimiento acumulado durante el periodo analizado? ¿Cuál el menor?  
2. ¿Cuál símbolo tiene la mayor volatilidad diaria (desviación estándar del rendimiento)? ¿Y cuál la menor?  
3. ¿Cuál es el rendimiento medio diario para cada símbolo? ¿Y mediana? ¿Qué supone la diferencia entre ambas?  
4. ¿Cuál es el percentil 95 del rendimiento diario para un símbolo seleccionado? ¿Cuántos días superan ese rendimiento?  
