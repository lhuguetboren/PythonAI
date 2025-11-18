    # `pd.to_numeric(..., errors="coerce")` — Conversión numérica tolerante a errores

    ## 1. ¿Qué hace `errors="coerce"`?

    `pd.to_numeric` intenta convertir una serie (o array) a valores numéricos (`int`/`float`).

    - Forma básica:
      ```python
      pd.to_numeric(serie, errors="raise" | "ignore" | "coerce")
      ```

    - `errors="raise"` (por defecto): si encuentra un valor no convertible (por ejemplo `"A"`), lanza un error.
    - `errors="ignore"`: devuelve la serie original sin modificar, aunque haya valores no numéricos.
    - `errors="coerce"`: los valores no convertibles se transforman en `NaN` (faltantes), el resto se convierten a número.

    Es especialmente útil cuando:

    - Los datos provienen de ficheros “sucios” (CSV, Excel, etc.) con texto mezclado.
    - Queremos calcular medias, sumas o correlaciones y necesitamos todo en formato numérico.
    - Preferimos marcar los valores problemáticos como `NaN` para tratarlos después (imputación, filtrado, etc.).

    ---

    ## 2. Casos típicos de uso

    1. Convertir una columna que debería ser numérica, pero contiene caracteres:
       ```python
       df["age"] = pd.to_numeric(df["age"], errors="coerce")
       ```

    2. Limpiar datos antes de un análisis estadístico:
       ```python
       df["income_clean"] = pd.to_numeric(df["income"], errors="coerce")
       ```

    3. Detección de valores problemáticos:
       ```python
       numeric_col = pd.to_numeric(df["col"], errors="coerce")
       problematic = df[numeric_col.isna() & df["col"].notna()]
       ```

    ---

    ## 3. Ejemplo completo con datos sintéticos

    ### Objetivo

    - Crear una serie con números mezclados con texto.
    - Intentar convertirla a numérico con distintos modos de `errors`.
    - Ver el comportamiento específico de `errors="coerce"` y cómo localizar los errores.

    ```python
    import pandas as pd

    # ---------------------------------------------------------
    # 1. Crear datos sintéticos con algunos valores no numéricos
    # ---------------------------------------------------------
    s = pd.Series(["10", "12", "15", "20", "A", "31", "C", "40"])

    print("=== Serie original ===")
    print(s)
    print("dtype:", s.dtype)

    # ---------------------------------------------------------
    # 2. Intentar conversión con distintos modos de errors
    # ---------------------------------------------------------

    # a) Modo 'raise' (por defecto): lanza error en cuanto encuentra algo no convertible.
    try:
        s_raise = pd.to_numeric(s, errors="raise")
        print("
Conversión con errors='raise':")
        print(s_raise)
    except Exception as e:
        print("
Error con errors='raise':", e)

    # b) Modo 'ignore': devuelve la serie original, sin tocarla.
    s_ignore = pd.to_numeric(s, errors="ignore")
    print("
Conversión con errors='ignore':")
    print(s_ignore)
    print("dtype tras 'ignore':", s_ignore.dtype)

    # c) Modo 'coerce': convierte lo posible y el resto a NaN
    s_coerce = pd.to_numeric(s, errors="coerce")
    print("
Conversión con errors='coerce':")
    print(s_coerce)
    print("dtype tras 'coerce':", s_coerce.dtype)

    # ---------------------------------------------------------
    # 3. Localizar valores problemáticos
    # ---------------------------------------------------------

    # Problema: valores que han terminado en NaN pero que originalmente no eran NaN
    problematic_mask = s_coerce.isna() & s.notna()
    problematic_values = s[problematic_mask]

    print("
Valores problemáticos (no convertibles a número):")
    print(problematic_values)

    # ---------------------------------------------------------
    # 4. Uso posterior: cálculo de media ignorando NaN
    # ---------------------------------------------------------
    mean_value = s_coerce.mean()  # por defecto, pandas ignora NaN en las operaciones
    print("
Media de los valores numéricos (ignorando NaN):", mean_value)
    ```

    ---

    ## 4. Ejercicios propuestos

    1. Añadir más valores problemáticos a la serie (`"??"`, `"N/A"`, `"None"`) y ver cuántos `NaN` aparecen.
    2. A partir de `s_coerce`, reemplazar los `NaN` por la media o la mediana y comentar las ventajas/inconvenientes.
    3. Usar `pd.to_numeric` sobre una columna de un DataFrame real (por ejemplo, importado de CSV) y:
       - Contar cuántos valores pasan a `NaN`.
       - Listar las filas originales que contenían esos valores.
