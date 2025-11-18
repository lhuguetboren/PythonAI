# Resample de fechas

## Teoría
`resample` agrupa por frecuencia temporal.

## Ejemplo
```python
import pandas as pd
rng=pd.date_range('2024-01-01',periods=6,freq='H')
df=pd.DataFrame({'fecha':rng,'valor':[1,2,3,4,5,6]}).set_index('fecha')
diario=df.resample('D').mean()
print(diario)
```
