# Análisis de datos con Pandas y NumPy

**Dataset**: detalles de pedidos de pizzas  
> Variables: `order_details_id`, `order_id`, `pizza_id`, `quantity`

---

## 1. Imports & configuración

Importacion de librerias

## 2. Carga de datos

- Leer el archivo CSV correspondiente.

- Mostrar las primeras filas, el resumen informativo y estadístico para entender las variables.

## 3. Limpieza y preparación de datos

- Verificar tipos de datos correctos (por ejemplo `quantity` como entero).  
- Detectar y tratar valores nulos, duplicados o valores atípicos.  
- (Opcional) Si tienes otro fichero con información de pizzas (precio, tipo), considera hacer merge para añadir más contexto.

---

## 4. Análisis exploratorio

### 4.1 Estadísticas globales

- Calcular cuántos registros de detalle de pedido hay.  
- Calcular la cantidad total de pizzas (`sum(quantity)`).  
- Calcular la cantidad promedio de pizzas por pedido.

### 4.2 Distribución por pizza

- Agrupar por `pizza_id` para calcular:  
  - la cantidad total vendida (`sum(quantity)`)  
  - la cantidad de pedidos en los que aparece (`count(order_id)` o `nunique(order_id)`)  
- Identificar las pizzas más populares (más cantidad vendida) y menos populares.

### 4.3 Análisis por pedido

- Agrupar por `order_id` para calcular:  
  - cantidad total de pizzas en cada pedido (`sum(quantity)`)  
  - número de líneas de detalle en cada pedido (`count(order_details_id)`)  
- Verificar distribución de tamaño de los pedidos (por ejemplo: ¿cuántos pedidos tienen 1 pizza, más de 2, más de 3?).

---

## 5. Uso de NumPy para análisis auxiliar

- Usar `np.percentile` para calcular percentiles de la `cantidad total de pizzas por pedido`.  
- Crear histogramas o distribuciones para ver qué tan frecuente son pedidos grandes vs. pequeños.

---

## 6. Preguntas para los alumnos

1. ¿Cuál es la pizza (pizza_id) más vendida en cuanto a cantidad y cuál la menos vendida?  
2. ¿Cuál es la cantidad promedio de pizzas por pedido? ¿Y la mediana?  
3. ¿Qué porcentaje de los pedidos tienen solo 1 pizza? ¿Y más de 2 pizzas?  
4. ¿Existen pedidos que destaquen por tener una cantidad muy alta de pizzas? Identifícalos usando percentiles.  
5. Si tuvieras los datos de precio de cada pizza, ¿cómo calcularías el valor estimado de cada pedido y cómo variarían los resultados anteriores?
