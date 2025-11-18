import pandas as pd

# Ejemplo sencillo
s = pd.Series(['10', '12', '15', '20', 'A', '31', 'C', 'D'])
print("Original Series:")
print(s)
print("Tipos:", s.dtype)

# Intentar conversión sin 'coerce' (modo por defecto)
s1 = pd.to_numeric(s, errors='raise')  # esto lanzará un error cuando encuentre 'A','C','D'
# Si quieres evitar el error:
# s1 = pd.to_numeric(s, errors='ignore')  # las entradas inválidas simplemente se quedan como texto

# Conversión con 'coerce'
s2 = pd.to_numeric(s, errors='coerce')
print("\nTras to_numeric(errors='coerce'):")
print(s2)
print("Tipos:", s2.dtype)

# Mostrar cuántos valores se volvieron NaN
print("\nNúmero de valores NaN tras coerce:", s2.isna().sum())
