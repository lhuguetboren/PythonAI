# Glosario de fundamentos matemáticos y estadísticos en análisis de datos

## 1. Fundamentos numéricos y algebraicos

### Array (vector, matriz, tensor)
Estructura matemática que representa un conjunto ordenado de valores.
- Un vector es una lista de números (una dimensión).
- Una matriz es una tabla de números (dos dimensiones).
- Un tensor es una generalización a más dimensiones.
Permiten representar datos numéricos y realizar operaciones como suma, producto o transposición.

### Dimensión y forma (shape)
La dimensión describe cuántos ejes tiene un conjunto de datos (1D, 2D, 3D...), mientras que la forma indica el número de elementos en cada eje.

### Tipos de datos numéricos
Definen el rango y precisión de los valores: enteros (int), reales (float), booleanos (bool), complejos (complex).
Su correcta elección afecta la memoria y la precisión de los cálculos.

### Operaciones vectorizadas
Operaciones aplicadas simultáneamente a todos los elementos de un conjunto (vector o matriz), sin usar bucles.
Matemáticamente equivalen a sumar, multiplicar o aplicar funciones a vectores completos.

### Álgebra lineal
Base matemática de muchas técnicas de análisis de datos. Incluye:
- Multiplicación de matrices (combinación lineal de vectores).
- Determinante: mide la escala o volumen transformado por una matriz cuadrada.
- Inversa: matriz que revierte la transformación (si existe).
- Autovalores y autovectores: direcciones de variación, fundamentales en reducción de dimensiones.

### Broadcasting
Regla que permite operar entre estructuras de distintas dimensiones cuando es matemáticamente coherente.


## 2. Fundamentos estadísticos descriptivos

### Variable
Propiedad medible que puede tomar distintos valores.
- Cuantitativa: numérica (edad, peso, temperatura).
- Cualitativa: categórica (sexo, color, país).

### Población y muestra
- Población: conjunto completo de elementos a estudiar.
- Muestra: subconjunto representativo que se analiza para inferir propiedades de la población.

### Media (promedio)
Medida de tendencia central que representa el valor medio de los datos.

### Mediana y moda
- Mediana: valor central al ordenar los datos.
- Moda: valor más frecuente.

### Varianza y desviación estándar
Miden la dispersión de los datos respecto a la media.
En análisis de datos, se usan para detectar variabilidad o anomalías.

### Distribución de frecuencias
Describe cuántas veces aparece cada valor o rango. Se representa mediante histogramas o gráficos de densidad.

### Percentiles y cuartiles
Dividen el conjunto de datos en partes según su posición relativa. El cuartil 1 (Q1) es el valor por debajo del cual está el 25% de los datos.

### Boxplot (diagrama de caja)
Representación visual de los cuartiles y valores atípicos. Permite identificar simetría, dispersión y extremos.


## 3. Fundamentos de relación y correlación

### Covarianza
Mide cómo varían dos variables juntas. Valores positivos indican que crecen juntos; negativos, que una crece cuando la otra disminuye.

### Correlación
Versión normalizada de la covarianza. Indica fuerza y dirección de la relación lineal entre variables (de -1 a +1).

### Mapa de calor (heatmap)
Representación visual de una matriz de correlaciones. Permite detectar grupos de variables relacionadas o redundantes.


## 4. Fundamentos de agrupación y resumen de datos

### Agrupación (grouping)
Proceso de dividir los datos en subconjuntos según una o más variables (por ejemplo, ciudad o género).

### Agregación
Aplicación de una función resumen (media, suma, conteo, etc.) sobre los grupos definidos.

### Ordenación y clasificación
Permite comparar observaciones y extraer jerarquías o rankings según algún criterio.

### Reindexación
Reorganización de los datos para mantener coherencia entre filas y columnas tras operaciones o combinaciones.


## 5. Fundamentos de representación gráfica

### Ejes y escalas
Los ejes de un gráfico representan las variables analizadas. La elección correcta de escala afecta la interpretación visual.

### Gráfico de líneas
Representa series temporales o tendencias continuas. Permite observar evolución o patrones a lo largo del tiempo.

### Gráfico de barras
Usado para comparar categorías discretas o valores agrupados.

### Histograma
Divide los datos en intervalos (bins) y muestra la frecuencia de aparición en cada uno, representando la distribución.

### Gráfico de dispersión (scatterplot)
Muestra la relación entre dos variables numéricas. Permite visualizar correlaciones o agrupamientos.


## 6. Fundamentos de limpieza y preparación de datos

### Valores nulos (NaN)
Representan datos faltantes o no definidos. Su tratamiento es crucial para evitar sesgos o errores en cálculos.

### Duplicados
Registros repetidos que distorsionan los resultados estadísticos.

### Conversión de tipos de datos
Transformar valores entre categorías, números o fechas permite aplicar funciones estadísticas adecuadas.

### Normalización y estandarización
Técnicas que ajustan la escala de las variables para compararlas o alimentar modelos.
- Normalización: escala los datos entre 0 y 1.
- Estandarización: ajusta media = 0, desviación estándar = 1.


## 7. Fundamentos del análisis exploratorio

### Exploración de datos (EDA)
Etapa inicial del análisis para entender el comportamiento general de los datos, su calidad y sus relaciones.

### Detección de outliers (valores atípicos)
Identificación de puntos que se alejan significativamente del resto de los datos.

### Patrones y tendencias
Identificación de comportamientos repetidos o direcciones de cambio en los datos.


## 8. Fundamentos para etapas posteriores (IA y ML)

### Datos como vectores de características
Cada observación (fila) se interpreta como un vector en un espacio multidimensional. Base para los modelos de aprendizaje automático.

### Transformaciones lineales
Cambios de base, proyecciones o rotaciones comunes en la reducción de dimensiones (por ejemplo, PCA).

### Preparación de datasets
Implica limpiar, escalar y estructurar los datos para alimentar algoritmos de predicción o clasificación.
