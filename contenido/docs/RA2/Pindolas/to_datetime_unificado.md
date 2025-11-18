# Conversión a datetime

## Teoría
`pd.to_datetime` convierte texto...

## Ejemplo
```python
import pandas as pd
s=pd.Series(['2024-01-01','2024-02-05'])
df=pd.DataFrame({'fecha':s})
df['fecha']=pd.to_datetime(df['fecha'])
df['mes']=df['fecha'].dt.month
print(df)
```
