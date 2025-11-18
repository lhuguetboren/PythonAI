# Relleno de valores

## Teoría
Métodos: ffill, bfill, interpolate...

## Ejemplo
```python
import pandas as pd
s=pd.Series([1,None,3,None,5])
df=pd.DataFrame({'x':s})
df['ffill']=df['x'].ffill()
df['bfill']=df['x'].bfill()
df['interp']=df['x'].interpolate()
print(df)
```
