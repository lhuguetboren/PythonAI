# Análisis de datos con Pandas y NumPy

**Dataset**: datos meteorológicos y consumo de energía  
> Variables: `Datetime`, `Temperature`, `Humidity`, `WindSpeed`, `GeneralDiffuseFlows`, `DiffuseFlows`, `PowerConsumption_Zone1`, `PowerConsumption_Zone2`, `PowerConsumption_Zone3`

---

## 1. Imports & configuración  

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV correspondiente, asegurando que la columna `Datetime` se interprete como tipo datetime y se establezca como índice del DataFrame.  
- Mostrar las primeras filas (`.head()`), `.info()` y `.describe()` para las variables numéricas.  
- Verificar la frecuencia de la serie (por ejemplo intervalos cada 10 minutos) y comprobar que no haya saltos importantes.

---

## 3. Limpieza y preparación de datos

- Convertir `Datetime` al tipo `datetime64[ns]`.  
- Verificar valores nulos, duplicados o registros faltantes; documentar cómo se tratan.  
- Crear columnas derivadas que puedan facilitar el análisis, por ejemplo:  
  - `total_power = PowerConsumption_Zone1 + PowerConsumption_Zone2 + PowerConsumption_Zone3`  
  - `hour = Datetime.dt.hour`, `day_of_week = Datetime.dt.dayofweek`  
  - (Opcional) `diffuse_ratio = DiffuseFlows / GeneralDiffuseFlows` (si tiene sentido)  
- (Opcional) Resamplear los datos a otra frecuencia (por ejemplo cada hora) usando funciones de tiempo de `pandas`. 

---

## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Calcular media, mediana, desviación estándar, mínimos y máximos de `Temperature`, `Humidity`, `WindSpeed`, `GeneralDiffuseFlows`, `DiffuseFlows`, `total_power`.  
- Contar cuántos registros actuales, intervalo temporal analizado (desde – hasta).

### 4.2 Distribución por hora / día de la semana

- Agrupar (o resamplear) por `hour` para calcular el consumo medio (`total_power`) por hora del día, la media de temperatura, etc.  
- Agrupar por `day_of_week` para ver si hay patrones semanales en el consumo o en las otras variables.

### 4.3 Relación entre variables ambientales y consumo

- Estudiar la correlación entre variables como `Temperature`, `DiffuseFlows`, `WindSpeed` y `total_power`.  
- Ver si cuando la radiación difusa (`GeneralDiffuseFlows` / `DiffuseFlows`) aumenta, el consumo total baja (o viceversa).  
- Usar funciones de NumPy para calcular `np.corrcoef` o `df.corr()`.

### 4.4 Análisis de patrones de radiación y consumo

- Visualizar la evolución temporal de `GeneralDiffuseFlows` y de `total_power` (gráfico de líneas) para ver patrones diarios.  
- Identificar horas pico de consumo de energía en relación con variables ambientales (por ejemplo baja temperatura, alta humedad, poca radiación).  
- Detectar outliers o días inusuales donde el patrón típico no se cumple.

---

## 5. Uso de NumPy para análisis auxiliar

- Utilizar `np.percentile()` para calcular percentiles de `total_power` (por ejemplo percentil 90) y detectar intervalos de consumo muy altos.  
- Crear un array con, por ejemplo, `Temperature` o `DiffuseFlows` y usar operaciones vectorizadas de NumPy para comparaciones rápidas.  
- Usar técnicas de ventana y desplazamiento (`.rolling()`, `.shift()`) para calcular diferencias entre periodos sucesivos y ver cambios rápidos.

---

## 6. Preguntas

1. ¿Cuál es la hora del día con mayor consumo medio (`total_power`)?  
2. ¿Existe una relación clara entre radiación difusa (`DiffuseFlows` / `GeneralDiffuseFlows`) y consumo de energía? Describe lo que observas.  
3. ¿Qué tan alta es la variabilidad del consumo diario? Usa percentiles de `total_power` para responder.  
4. ¿Hay diferencias de consumo entre días de semana y fines de semana (`day_of_week`)?  
5. Identifica un período donde el consumo fue muy alto respecto al promedio (por ejemplo por encima del percentil 90) y analiza las condiciones ambientales en ese momento (temperatura, humedad, radiación).  
