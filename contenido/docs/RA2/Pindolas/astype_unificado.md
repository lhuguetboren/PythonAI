# astype — Conversión de tipos

## Teoría
`astype` convierte columnas a un tipo concreto.

## Ejemplo sintético
```python
import pandas as pd

Df=pd.DataFrame({
 'store_location':['A','B','A'],
 'price':['10','20','30']})

Df['store_location']=Df['store_location'].astype('category')
Df['price']=Df['price'].astype(int)
print(Df.dtypes)
print(Df)
```
