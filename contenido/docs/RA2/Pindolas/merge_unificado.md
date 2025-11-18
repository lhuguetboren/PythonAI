# Merge en pandas

## Teoría
`merge` une DataFrames...

## Ejemplo sintético
```python
import pandas as pd
A=pd.DataFrame({'id':[1,2,3],'valor':[10,20,30]})
B=pd.DataFrame({'id':[1,2,4],'categoria':['X','Y','Z']})
C=A.merge(B,on='id',how='left')
print(C)
```
