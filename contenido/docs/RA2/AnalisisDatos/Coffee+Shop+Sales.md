# Análisis de datos con Pandas y NumPy

**Dataset**: transacciones de tienda  
> Variables: `transaction_id`, `transaction_date`, `transaction_time`, `transaction_qty`, `store_id`, `store_location`, `product_id`, `unit_price`, `product_category`, `product_type`, `product_detail`

---

## 1. Imports & configuración

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV (pista: parsear fechas si corresponde).  
- Mostrar las primeras filas, el resumen informativo y estadístico para entender las variables.

---

## 3. Limpieza y preparación de datos

- Convertir `transaction_time` al tipo apropiado.  
- Corregir formatos inconsistentes .  
- Crear una nueva columna `total_price` como producto de `transaction_qty` y `unit_price`.  
- Detectar y tratar los valores nulos, duplicados o valores atípicos.

---

## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Calcular la media, la mediana, la desviación estándar y los valores mínimo/máximo de `unit_price`, `total_price` y `transaction_qty`. 

- Determinar cuántas transacciones hay, cuántas tiendas distintas (`store_id`) y cuántas ubicaciones distintas (`store_location`).

### 4.2 Distribución por categoría de producto

- Agrupar por `product_category` para calcular:  
  - número de transacciones  
  - importe total por categoría  
  - importe medio por transacción  
- Ordenar las categorías de mayor a menor por importe total.  
- Reflexionar: ¿qué categoría genera más ingresos? ¿por qué crees que es así?

### 4.3 Agrupaciones por tienda / ubicación

- Agrupar por `store_location` (o `store_id`) y calcular:  
  - número de transacciones  
  - importe total  
  - importe medio  
- Comparar las tiendas: ¿cuál tiene el mayor importe medio? ¿la mayor cantidad de transacciones? ¿qué factores podrían estar influyendo?

### 4.4 Análisis temporal

- Extraer la hora del día de la columna `transaction_time`.  
- Agrupar por hora para ver cuántas transacciones se realizan en cada franja horaria.  
- Opcional: comparar los patrones de hora entre diferentes ubicaciones de tienda.  
- Reflexionar: ¿a qué horas se concentra la actividad? ¿cómo podrían ajustar el negocio según estos datos?

---

## 5. Uso de NumPy para análisis auxiliar

- Utilizar funciones de NumPy para calcular percentiles (por ejemplo del `total_price`) y detectar posibles valores atípicos.  
- Crear histogramas o distribuciones para `unit_price` o `transaction_qty` usando NumPy.  
- Interpretar: ¿qué percentiles consideras como “alto”, “bajo”? ¿qué transacciones podrían ser anómalas?

---

## 6. Preguntas

1. ¿Cuál categoría de producto genera más ingresos y cuál menos?  
2. ¿La tienda con mayor número de transacciones es la misma que la de mayor importe medio? Analiza y comenta.  
3. ¿A qué hora del día se concentra la mayoría de las transacciones? ¿Varía según la ubicación de la tienda?  
4. ¿Existen precios unitarios que parecen atípicos (muy altos o muy bajos) respecto a la media? Identifícalos usando percentiles.  

