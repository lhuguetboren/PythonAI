# Clases y `@dataclass`

El decorador `@dataclass` (disponible desde Python 3.7) **automatiza** gran parte del trabajo repetitivo al crear clases:

- Crea automáticamente el método `__init__` (constructor).
- Crea `__repr__` (representación legible del objeto).
- Crea `__eq__` (comparación entre objetos).

**Código más limpio y legible**.

## Ejemplo básico con `@dataclass`

```python
# ---------------------------
# Clases
# ---------------------------
from dataclasses import dataclass
from datetime import date

# Clase Cliente
@dataclass
class Cliente:
    id: int
    nombre: str
    email: str
    fecha_alta: date
```

## Uso práctico

```python
# Crear un cliente
cliente1 = Cliente(
    id=1,
    nombre="Joan Huguet",
    email="joan@example.com",
    fecha_alta=date(2025, 11, 4)
)

# Mostrar información
print(cliente1)
```

**Salida:**

```
Cliente(id=1, nombre='Joan Huguet', email='joan@example.com', fecha_alta=datetime.date(2025, 11, 4))
```

---

## 🛠️ Acceso a atributos

```python
print(cliente1.nombre)      # Joan Huguet
print(cliente1.email)       # joan@example.com
```

Y puedes modificarlos:

```python
cliente1.email = "nuevo_email@example.com"
```

