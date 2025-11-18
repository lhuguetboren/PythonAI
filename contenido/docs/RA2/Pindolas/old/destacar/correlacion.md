# Plantilla: Matriz de correlaciones con pandas/NumPy  
Guía para aplicar matriz de correlaciones en distintos datasets.

---

## 1. Selección de columnas numéricas  
- `df.select_dtypes(include=['number'])` — Seleccionar columnas numéricas en pandas.  
- `num_df = df[['col1','col2',…]]` — Especificar manualmente las columnas a analizar.  

---

## 2. Calcular la matriz de correlación  
- `corr_mat = num_df.corr(method='pearson')` — Calcular matriz de correlaciones (por defecto método Pearson).  
- `print(corr_mat)` — Mostrar matriz en consola.  

---

## 3. Visualizar la matriz de correlaciones  
- `import seaborn as sns; import matplotlib.pyplot as plt` — Importar librerías de visualización.  
- `plt.figure(figsize=(w,h))` — Definir tamaño de figura.  
- `sns.heatmap(corr_mat, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)` — Dibujar mapa de calor con anotaciones.  
- `plt.title("Título del gráfico")` — Añadir título al gráfico.  
- `plt.show()` — Mostrar el gráfico.  

---

## 4. Interpretación de resultados  
- Valores cercanos a **+1** → fuerte correlación positiva.  
- Valores cercanos a **-1** → fuerte correlación negativa.  
- Valores cerca de **0** → poca o ninguna correlación lineal.  
- Diagonal principal siempre = 1 (variable consigo misma).  
- Atención: correlación **no implica causalidad**.  

---

## 5. Cuándo tiene sentido usarla en los casos de estudio  
- Si tienes varias **variables cuantitativas** y quieres estudiar cómo se relacionan entre sí (por ejemplo: piezas ↔ precio, consumo ↔ temperatura, rendimiento ↔ volumen).  
- Para **detectar multicolinealidad** antes de análisis más complejos o modelos.  
- Para obtener **insights rápidos** sobre qué variables podrían influenciar a otras.  
- Para hacer **filtrado o selección de variables** basándote en relaciones fuertes.  

---

## 6. Buenas prácticas  
- Asegúrate de limpiar los datos (eliminar NAs, convertir tipos) antes de calcular la correlación.  
- Considera escalado o transformación si las disciplinas de las variables difieren mucho.  
- Verifica si los datos cumplen supuestos de normalidad si planeas interpretar valores de Pearson.  
- Considera usar otros métodos de correlación (`method='spearman'` o `method='kendall'`) si los datos no son lineales o contienen rangos ordinales.  
- Si hay muchas variables (por ejemplo > 20), limita a un subconjunto o usa clustering de variables para evitar gráficos muy densos.  

---

## 7. Entrega para los alumnos  
- Entrega el notebook con el cálculo y visualización de la matriz.  
- Incluye en el notebook, en formato Markdown, una breve interpretación de los resultados:  
  * ¿Qué pares de variables muestran correlación fuerte?  
  * ¿Hay alguna variable con correlación inesperada?  
  * ¿Qué implicación podrían tener esos resultados para el negocio/análisis?  
  
- (Opcional) Exporta la matriz a un archivo CSV:  
  ```python
  corr_mat.to_csv('matriz_correlacion.csv')

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('transacciones.csv', parse_dates=['transaction_date'], dayfirst=True)

# Crear columna total_price si no está
df['unit_price']   = df['unit_price'].astype(str).str.replace(',', '.').astype(float)
df['total_price']  = df['transaction_qty'] * df['unit_price']

# Selección de columnas numéricas relevantes
num_df = df[['transaction_qty', 'unit_price', 'total_price']]

# Calcular la matriz de correlación
corr_mat = num_df.corr()

# Mostrar
print(corr_mat)

# Visualizar
plt.figure(figsize=(6,5))
sns.heatmap(corr_mat, annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlación entre cantidad, precio unitario e importe total")
plt.show()
```