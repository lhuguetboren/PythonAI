# Tipado estático con `typing`

Es recomendable usar **anotaciones de tipo** (type hints) con el módulo `typing` para escribir código **más legible, seguro y fácil de mantener**.

El módulo `typing` permite **especificar los tipos de datos** esperados en variables, parámetros y valores de retorno.  
No cambia el funcionamiento del programa, pero **ayuda a detectar errores antes de ejecutar** y mejora la documentación.

---

## 💡 Ejemplo básico: Función con tipos

```python
from typing import List

def sumar_numeros(numeros: List[int]) -> int:
    """Suma todos los números de una lista."""
    return sum(numeros)
```

### ✅ Explicación
- `List[int]` indica que se espera una lista de enteros.  
- `-> int` indica que la función **devuelve un entero**.  
- Si intentas pasar una lista con textos, un editor como VSCode te marcará un aviso.

---

## 🧠 Tipos comunes

| Tipo | Significado | Ejemplo |
|------|--------------|----------|
| `int`, `float`, `str`, `bool` | Tipos básicos | `edad: int = 20` |
| `List[T]` | Lista de elementos del tipo `T` | `List[str]` |
| `Dict[K, V]` | Diccionario con clave y valor | `Dict[str, int]` |
| `Tuple[T1, T2]` | Tupla de tipos fijos | `Tuple[str, int]` |
| `Optional[T]` | Valor que puede ser `T` o `None` | `Optional[str]` |
| `Any` | Cualquier tipo | `Any` |
| `Union[T1, T2]` | Puede ser uno de varios tipos | `Union[int, float]` |

---

## 🧾 Ejemplo de typing al declarar variables

```python
# Tipos simples
nombre: str = "Joan"
edad: int = 22
altura: float = 1.75
activo: bool = True

# Tipos compuestos
numeros: list[int] = [1, 2, 3, 4, 5]
emails: dict[int, str] = {1: "joan@example.com", 2: "anna@example.com"}

print(nombre, edad, altura, activo)
```
💡 Esto no cambia el comportamiento, pero hace el código más claro y ayuda al autocompletado.

---

## 📦 Ejemplo con varias funciones

```python
from typing import Dict, Optional

def obtener_email(clientes: Dict[int, str], id_cliente: int) -> Optional[str]:
    """Devuelve el email del cliente si existe."""
    return clientes.get(id_cliente)

# Ejemplo de uso
emails = {1: "joan@example.com", 2: "anna@example.com"}

print(obtener_email(emails, 1))  # joan@example.com
print(obtener_email(emails, 3))  # None
```

💡 Aquí usamos:
- `Dict[int, str]` → el diccionario tiene claves `int` y valores `str`.
- `Optional[str]` → la función puede devolver `str` **o** `None`.

---

## 🧩 Tipos en clases

```python
from dataclasses import dataclass
from datetime import date

@dataclass
class Cliente:
    id: int
    nombre: str
    email: str
    fecha_alta: date
    activo: bool = True
```

🔍 Aquí cada atributo está **tipado**: Python sabe qué tipo de dato debería contener.

---

## 🔄 Funciones genéricas

```python
from typing import TypeVar, List

T = TypeVar("T")  # T puede ser cualquier tipo

def primero(lista: List[T]) -> T:
    """Devuelve el primer elemento de una lista, sin importar el tipo."""
    return lista[0]

print(primero([10, 20, 30]))     # 10
print(primero(["a", "b", "c"]))  # a
```

💡 Esto permite crear funciones reutilizables **sin perder información de tipo**.

---

## 🚀 Bonus: Comprobación con `mypy`
Puedes comprobar los tipos con:
```bash
mypy archivo.py
```
Si hay errores de tipo (por ejemplo, pasar una cadena donde esperaba un número), `mypy` te los indicará.
