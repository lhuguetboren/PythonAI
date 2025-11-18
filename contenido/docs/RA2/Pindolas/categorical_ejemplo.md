    # Variables categóricas en pandas — `astype("category")`

    ## 1. ¿Qué es una variable categórica?

    Una variable categórica es aquella que toma un **conjunto limitado de valores** que representan categorías o etiquetas, no cantidades:

    - Ejemplos: país, ciudad, tipo de producto, método de pago, tamaño (`"S"`, `"M"`, `"L"`), etc.

    En pandas, el tipo `category`:

    - Almacena las categorías como **códigos internos** (0, 1, 2, …).
    - Permite reducir uso de memoria cuando hay muchas repeticiones.
    - Hace más explícito que la variable no es numérica continua.
    - Puede ser **ordenada** (por ejemplo: `Small < Medium < Large`).

    ---

    ## 2. ¿Cómo convertir a `category` con `astype`?

    Forma básica:

    ```python
    df["col"] = df["col"].astype("category")
    ```

    Conversión múltiple:

    ```python
    df = df.astype({
        "col1": "category",
        "col2": "category"
    })
    ```

    Ventajas:

    - Menor memoria utilizada en DataFrames grandes.
    - Operaciones de agrupación (`groupby`), filtros y joins más eficientes.
    - Posibilidad de trabajar con un conjunto de valores bien definido.

    ---

    ## 3. Ejemplo completo con datos sintéticos

    ### Objetivo

    - Crear un DataFrame con columnas de texto que representan categorías.
    - Convertirlas a tipo `category`.
    - Explorar categorías, códigos internos y orden.

    ```python
    import pandas as pd

    # ---------------------------------------------------------
    # 1. Crear datos sintéticos
    # ---------------------------------------------------------
    data = {
        "customer_id": [1, 2, 3, 4, 5, 6],
        "country": ["ES", "ES", "FR", "DE", "ES", "FR"],
        "product_size": ["M", "L", "S", "M", "M", "L"],
        "payment_method": ["Card", "Cash", "Card", "Card", "App", "Cash"]
    }

    df = pd.DataFrame(data)

    print("=== DataFrame original ===")
    print(df)
    print("
=== Tipos originales ===")
    print(df.dtypes)

    # ---------------------------------------------------------
    # 2. Conversión a tipo category
    # ---------------------------------------------------------
    df["country"] = df["country"].astype("category")
    df["product_size"] = df["product_size"].astype("category")
    df["payment_method"] = df["payment_method"].astype("category")

    print("
=== DataFrame tras convertir a category ===")
    print(df)
    print("
=== Tipos tras conversión ===")
    print(df.dtypes)

    # ---------------------------------------------------------
    # 3. Inspeccionar categorías y códigos internos
    # ---------------------------------------------------------

    print("
Categorías de 'country':", df["country"].cat.categories)
    print("Códigos de 'country':", df["country"].cat.codes.tolist())

    print("
Categorías de 'product_size':", df["product_size"].cat.categories)
    print("Códigos de 'product_size':", df["product_size"].cat.codes.tolist())

    # ---------------------------------------------------------
    # 4. Definir un orden lógico en una variable categórica
    # ---------------------------------------------------------

    # Definimos 'S' < 'M' < 'L'
    df["product_size"] = df["product_size"].cat.reorder_categories(["S", "M", "L"], ordered=True)

    print("
Categorías de 'product_size' con orden lógico:")
    print(df["product_size"].cat.categories)
    print("¿Es ordenada?:", df["product_size"].cat.ordered)

    # Comparaciones usando el orden
    print("
Filas con product_size > 'S':")
    print(df[df["product_size"] > "S"])

    # ---------------------------------------------------------
    # 5. Ejemplo de groupby con categorías
    # ---------------------------------------------------------

    # Suponemos unidades compradas
    df["units"] = [3, 1, 4, 2, 5, 2]

    units_by_country = df.groupby("country")["units"].sum()
    print("
Unidades totales por país:")
    print(units_by_country)
    ```

    ---

    ## 4. Ejercicios propuestos

    1. Convertir otras columnas del DataFrame (por ejemplo, una columna con nombre de tienda) a `category` y comprobar el uso de memoria con `df.info(memory_usage="deep")` antes y después.
    2. Definir un orden para un conjunto de categorías temporales (`"Morning"`, `"Afternoon"`, `"Evening"`) y filtrar solo las filas con `"Afternoon"` y `"Evening"`.
    3. A partir de un dataset real, elegir al menos 3 columnas categóricas candidatas y convertirlas a `category`, justificando por qué tiene sentido.
