import numpy as np

# 1. Crear arrays
a = np.array([1, 2, 3, 4, 5])           # un array 1-D :contentReference[oaicite:1]{index=1}
b = np.arange(10)                       # array de 0 a 9 :contentReference[oaicite:2]{index=2}
c = np.zeros((3,2))                     # array 3×2 de ceros :contentReference[oaicite:3]{index=3}

print("a:", a)
print("b:", b)
print("c:", c)

# 2. Operaciones vectorizadas
print("a * 2:", a * 2)
print("a + b[:5]:", a + b[:5])
print("a ** 2:", a ** 2)                # potencia de cada elemento

# 3. Agregaciones / estadísticas
print("mean(a):", np.mean(a))
print("std(a):", np.std(a))
print("min(b):", np.min(b))
print("max(b):", np.max(b))

# 4. Percentiles
pct = np.percentile(a, [25, 50, 75])
print("Percentiles 25/50/75 de a:", pct)

# 5. Indexado, slicing, reshape
d = np.arange(12).reshape((3,4))
print("d:", d)
print("d[1,2]:", d[1,2])
print("d[:,1]:", d[:,1])                # toda la segunda columna

# 6. Broadcasting
e = np.array([1, 2, 3])
f = e + 10                              # añade 10 a cada elemento de e
print("e:", e)
print("f:", f)

# 7. Uso combinado para un caso sencillo
# Supongamos que tenemos rendimientos diarios de una inversión:
returns = np.array([0.01, -0.005, 0.02, 0.0, 0.015])   # 1% , -0.5% , 2% , 0% , 1.5%
growth = np.cumprod(1 + returns)                       # crecimiento acumulado :contentReference[oaicite:4]{index=4}
print("Rendimientos diarios:", returns)
print("Crecimiento acumulado:", growth)
