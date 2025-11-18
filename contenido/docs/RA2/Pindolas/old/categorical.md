# Plantilla: Conversión de variables de texto a variables categóricas en pandas  
Guía para preparar el dataset y convertir variables de texto a tipo categórico.

---

## 1. Importar librerías  
```python
import pandas as pd
import numpy as np

2. Carga de datos

    Leer el fichero CSV.

    Verificar tipos, por ejemplo con df.info().

3. Identificar columnas de texto que conviene convertir

    Variables de tipo texto con número limitado de valores repetidos (por ejemplo: país, categoría, tipo de producto) son candidatas.

    Por ejemplo: country, shape, platform, theme, category, etc.

4. Conversión a tipo ‘category’

df['columna_texto'] = df['columna_texto'].astype('category')

Repetir para cada variable relevante.
5. Verificación de los tipos

print(df.dtypes)

Comprobar que las columnas deseadas tienen el tipo category.
6. ¿Por qué convertir a ‘category’?

    Reduce el uso de memoria al almacenar valores repetidos como códigos internos.

    Mejora el rendimiento en operaciones de agrupación o filtrado.

    Hace más explícito que la variable es categórica, no continua.

    Posibilidad de definir orden lógico si tiene sentido (por ejemplo: Small < Medium < Large).

df['size'] = pd.Categorical(df['size'], categories=['Small','Medium','Large'], ordered=True)

7. Buenas prácticas

    Antes de la conversión, limpiar valores atípicos o faltantes en la columna.

    Tener cuidado si la variable de texto contiene muchos valores únicos distintos (en ese caso puede no convenir usar ‘category’).

    Documentar en el notebook que has hecho esta conversión y por qué.

8. Entrega para los alumnos

    El notebook debe incluir una sección explicativa (Markdown) donde se indique qué variables se han convertido a categoría y por qué.

    Incluir un pequeño análisis: ¿ha cambiado algo al usar tipo ‘category’ (por ejemplo memoria, velocidad de agrupación)?

    (Opcional) Comparar df.groupby('variable') antes y después de la conversión para ver si funciona correctamente.


