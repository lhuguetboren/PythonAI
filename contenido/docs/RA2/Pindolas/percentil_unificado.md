# Nueva columna con percentil

## Teoría
`np.percentile`...

## Ejemplo
```python
import pandas as pd, numpy as np
s=pd.Series([10,20,30,40,50,60])
p90=np.percentile(s,90)
df=pd.DataFrame({'valor':s})
df['top10']=df['valor']>p90
print(df)
```
