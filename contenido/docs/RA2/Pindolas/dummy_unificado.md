# One-Hot Encoding — get_dummies

## Teoría
`pd.get_dummies` transforma categorías en columnas binarias.

## Ejemplo sintético
```python
import pandas as pd

df=pd.DataFrame({
 'theme':['StarWars','City','City','Technic'],
 'price':[30,20,25,50]})

encoded=pd.get_dummies(df,columns=['theme'],drop_first=True)
print(encoded)
```
