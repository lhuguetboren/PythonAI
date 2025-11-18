# GROUPBY + CONTEO + NAN

## 1) Contar calles por distrito

``` python
conteo = (
    df.groupby("Distrito")["Calle"]
      .count()                      # cuenta filas (aunque se repitan nombres)
      .reset_index(name="N_Calles")
)
```

## 2) Contar calles ÚNICAS por distrito

``` python
conteo_unicas = (
    df.groupby("Distrito")["Calle"]
      .nunique()                    # cuenta valores únicos
      .reset_index(name="Calles_unicas")
)
```

## 3) Listar calles dentro de cada distrito

``` python
listado = (
    df.groupby("Distrito")["Calle"]
      .apply(list)                  # convierte cada grupo en lista
      .reset_index(name="Listado_calles")
)
```

## 🟥 4) Eliminar NaN

### Eliminar filas con cualquier NaN:

``` python
df = df.dropna()
```

### Eliminar filas solo si faltan valores en columnas clave:

``` python
df = df.dropna(subset=["Distrito", "Calle"])
```

### Eliminar columnas con NaN:

``` python
df = df.dropna(axis=1)
```

## 🟩 5) Rellenar NaN

### Rellenar con texto:

``` python
df["Calle"] = df["Calle"].fillna("SIN NOMBRE")
```

### Rellenar con cadena vacía:

``` python
df["Calle"] = df["Calle"].fillna("")
```

## 🟦 6) Ordenar distritos por número de calles

``` python
conteo = (
    df.groupby("Distrito")["Calle"]
      .count()
      .reset_index(name="N_Calles")
      .sort_values("N_Calles", ascending=False)
)
```

## 🟨 7) Iterar por grupos (para revisión manual)

``` python
for distrito, datos in df.groupby("Distrito"):
    print("Distrito:", distrito)
    print(datos)
```
