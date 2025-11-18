    # Estadísticos básicos en pandas — `describe`, medias, desviaciones...

    ## 1. ¿Qué son los estadísticos básicos?

    Los estadísticos básicos resumen rápidamente el comportamiento de una variable numérica o categórica. Entre los más utilizados:

    - **Media** (`mean`): valor promedio.
    - **Mediana** (`median`): valor central (robusto a valores extremos).
    - **Desviación estándar** (`std`): medida de dispersión.
    - **Mínimo y máximo** (`min`, `max`).
    - **Percentiles** (por ejemplo, 25%, 50%, 75%).
    - **Conteos** (`count`) y frecuencias (`value_counts`) para categóricas.

    En pandas, el punto de partida típico es:

    ```python
    df.describe()
    ```

    ---

    ## 2. Funciones clave en pandas

    - `df.describe()` — resumen estadístico de columnas numéricas (y categóricas si se indica).
    - `df["col"].mean()` — media de una columna.
    - `df["col"].median()` — mediana.
    - `df["col"].std()` — desviación estándar.
    - `df["col"].min()`, `df["col"].max()` — mínimo y máximo.
    - `df["col"].quantile(0.25)` — percentil 25, etc.
    - `df["col_cat"].value_counts()` — frecuencia de cada categoría.

    ---

    ## 3. Ejemplo completo con datos sintéticos

    ### Objetivo

    - Crear un DataFrame con información de ventas.
    - Obtener un resumen con `describe()`.
    - Calcular algunos estadísticos específicos por columna.

    ```python
    import pandas as pd
    import numpy as np

    # ---------------------------------------------------------
    # 1. Crear datos sintéticos
    # ---------------------------------------------------------
    np.random.seed(0)

    n = 50
    data = {
        "order_id": range(1, n + 1),
        "units": np.random.randint(1, 10, size=n),
        "unit_price": np.random.uniform(5.0, 20.0, size=n),
        "store": np.random.choice(["A", "B", "C"], size=n)
    }

    df = pd.DataFrame(data)
    df["total"] = df["units"] * df["unit_price"]

    print("=== Primeras filas del DataFrame ===")
    print(df.head())

    # ---------------------------------------------------------
    # 2. Resumen con describe
    # ---------------------------------------------------------

    print("
=== Estadísticos básicos (numéricos) ===")
    print(df.describe())

    # También podemos incluir categóricas
    print("
=== Estadísticos incluyendo categóricas ===")
    print(df.describe(include="all"))

    # ---------------------------------------------------------
    # 3. Estadísticos específicos
    # ---------------------------------------------------------

    print("
Media de 'total':", df["total"].mean())
    print("Mediana de 'total':", df["total"].median())
    print("Desviación estándar de 'total':", df["total"].std())
    print("Mínimo de 'total':", df["total"].min())
    print("Máximo de 'total':", df["total"].max())

    # Percentiles
    p25 = df["total"].quantile(0.25)
    p75 = df["total"].quantile(0.75)
    print("
Percentil 25 de 'total':", p25)
    print("Percentil 75 de 'total':", p75)

    # Conteo de categorías
    print("
Frecuencia por tienda:")
    print(df["store"].value_counts())

    # Ejemplo de estadísticos por grupo
    print("
Media de 'total' por tienda:")
    print(df.groupby("store")["total"].mean())
    ```

    ---

    ## 4. Ejercicios propuestos

    1. Añadir una columna `discount` (descuento en %) y calcular la media, mediana y desviación estándar por tienda.
    2. Calcular el coeficiente de variación de `total` (`std / mean`) y comentar qué indica sobre la dispersión relativa.
    3. Aplicar `describe(include="all")` a un dataset real e interpretar al menos 3 estadísticas por columna.
