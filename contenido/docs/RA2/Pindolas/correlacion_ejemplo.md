    # Matriz de correlación con pandas

    ## 1. ¿Qué es la correlación?

    La **correlación** mide el grado de relación lineal entre dos variables numéricas. Los valores suelen estar entre `-1` y `1`:

    - Cerca de `1`: relación lineal positiva fuerte (cuando X sube, Y tiende a subir).
    - Cerca de `-1`: relación lineal negativa fuerte (cuando X sube, Y tiende a bajar).
    - Cerca de `0`: no hay relación lineal clara.

    En análisis de datos, se usa mucho para:

    - Detectar variables altamente relacionadas entre sí.
    - Identificar posibles problemas de multicolinealidad en modelos.
    - Explorar rápidamente patrones en datasets numéricos.

    ---

    ## 2. Matriz de correlación en pandas

    En pandas, la matriz de correlaciones se calcula con:

    ```python
    corr_mat = df.corr(numeric_only=True, method="pearson")
    ```

    Parámetros importantes:

    - `numeric_only=True`: considera solo columnas numéricas.
    - `method="pearson"`: correlación de Pearson (la más habitual). Otras opciones:
      - `"spearman"`: correlación por rangos (robusta a no linealidades suaves).
      - `"kendall"`: medida basada en concordancias/discordancias de pares.

    ---

    ## 3. Ejemplo completo con datos sintéticos

    ### Objetivo

    - Crear un DataFrame con varias columnas numéricas relacionadas.
    - Calcular la matriz de correlación.
    - Interpretar algunos de sus valores.

    ```python
    import pandas as pd
    import numpy as np

    # ---------------------------------------------------------
    # 1. Crear datos sintéticos
    # ---------------------------------------------------------

    np.random.seed(42)
    n = 100

    # Variable base: horas de estudio
    study_hours = np.random.normal(loc=5, scale=2, size=n)  # media 5 horas, sd 2

    # Nota del examen: fuertemente relacionada con study_hours
    exam_score = 50 + study_hours * 8 + np.random.normal(loc=0, scale=5, size=n)

    # Nivel de sueño: débilmente relacionado con study_hours (a veces quien estudia más duerme menos)
    sleep_hours = 8 - (study_hours - study_hours.mean()) * 0.3 + np.random.normal(loc=0, scale=1, size=n)

    # Variable casi independiente: número de cafés
    coffees = np.random.poisson(lam=2, size=n)

    df = pd.DataFrame({
        "study_hours": study_hours,
        "exam_score": exam_score,
        "sleep_hours": sleep_hours,
        "coffees": coffees
    })

    print("=== Primeras filas del DataFrame ===")
    print(df.head())

    # ---------------------------------------------------------
    # 2. Calcular la matriz de correlación
    # ---------------------------------------------------------

    corr_mat = df.corr(numeric_only=True, method="pearson")

    print("
=== Matriz de correlación ===")
    print(corr_mat)

    # ---------------------------------------------------------
    # 3. Interpretación rápida
    # ---------------------------------------------------------

    print("
Correlación study_hours vs exam_score:", corr_mat.loc["study_hours", "exam_score"])
    print("Correlación study_hours vs sleep_hours:", corr_mat.loc["study_hours", "sleep_hours"])
    print("Correlación exam_score vs coffees:", corr_mat.loc["exam_score", "coffees"])
    ```

    ---

    ## 4. Visualización (opcional)

    Si se quiere ver la matriz de correlación como un mapa de calor:

    ```python
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 5))
    plt.imshow(corr_mat, interpolation="nearest")
    plt.xticks(range(len(corr_mat.columns)), corr_mat.columns, rotation=45)
    plt.yticks(range(len(corr_mat.index)), corr_mat.index)
    plt.colorbar(label="Correlación")
    plt.title("Matriz de correlación")
    plt.tight_layout()
    plt.show()
    ```

    ---

    ## 5. Ejercicios propuestos

    1. Añadir una nueva variable `practice_tests` (número de exámenes de prueba realizados) que esté muy correlacionada con `exam_score` y comprobarlo.
    2. Cambiar el método de correlación a `"spearman"` y comentar si cambian los valores significativamente.
    3. Aplicar este mismo código a un dataset real y decidir qué pares de variables parecen más relacionados.
