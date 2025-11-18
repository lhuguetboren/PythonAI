import pandas as pd

# Supongamos que ya has leído el archivo:
df = pd.read_csv('transacciones.csv', parse_dates=['transaction_date'], dayfirst=True)

# Ver tipos iniciales
print(df.dtypes)

# Convertimos columnas de texto a tipo categórico
df['store_location']   = df['store_location'].astype('category')
df['product_category'] = df['product_category'].astype('category')
df['product_type']     = df['product_type'].astype('category')
df['product_detail']   = df['product_detail'].astype('category')

# Ver tipos después de la conversión
print(df.dtypes)

# Ahora, por ejemplo, si miras qué categorías hay en 'product_type':
print(df['product_type'].cat.categories)
