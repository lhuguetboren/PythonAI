# Clases y funciones en Python

## Objetivos

- Entender qué es una clase y para qué se usan en Python.  
- Definir clases con atributos y métodos, incluyendo el método especial `__init__`.  
- Diferenciar entre funciones independientes y métodos y usarlos para modularizar el código.  
- Comprender cómo se definen y se llaman funciones, cómo se pasan argumentos y cómo se devuelven valores.  
- Explorar el uso de librerías estándar (`math`, `random` y `datetime`) dentro de funciones y clases.  

## 1. ¿Qué es una clase?

En Python, una clase es un tipo de objeto que agrupa datos y funcionalidad.  Crear una clase permite definir un nuevo tipo cuyas instancias pueden tener **atributos** (datos) y **métodos** (funciones) que operan sobre esos datos.  

Las clases proporcionan las características básicas de la programación orientada a objetos, como la **encapsulación** y la **herencia**, y se crean en tiempo de ejecución .  

Cada instancia puede almacenar su estado en atributos y posee métodos para modificar ese estado.

### Ventajas

- Modelan entidades del mundo real (Círculo, Alumno, Reloj) con propiedades y operaciones.  
- Facilitan la reutilización y organización del código.  
- Soportan **herencia** y **polimorfismo**  

## 2. Definición de clases y el método `__init__`

Una clase se define con la palabra clave `class`:

```python
class NombreDeLaClase:
    # bloque de declaraciones (métodos, variables de clase)
    pass
```

Cuando Python ejecuta la definición de la clase, crea un nuevo espacio de nombres y genera un objeto clase que lo envuelve

### El método `__init__`

Para inicializar los atributos de cada instancia se usa el método especial `__init__()`.  

```python
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
```

Ejemplo de uso:

```python
p = Punto2D(3, 4)
# Se ejecuta automáticamente p.__init__(3, 4)
```

## 3. Métodos de instancia y uso de `self`

Los **métodos** son funciones definidas dentro de una clase que operan sobre sus instancias.  
El primer parámetro se llama habitualmente `self`.  

```python
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

c = Circulo(5)
print(c.area())
```

Una llamada `obj.metodo(arg1, arg2)` equivale a `Clase.metodo(obj, arg1, arg2)` .  

Los atributos pueden añadirse o eliminarse dinámicamente con `del`.

## 4. Funciones y modularidad

Aunque las clases agrupan datos y métodos, las funciones independientes siguen siendo una herramienta básica para modularizar un programa. Se definen con la palabra clave def y se pueden llamar desde cualquier parte del código. Por ejemplo, para imprimir la serie de Fibonacci hasta un límite n:

```python
def fib(n):
    \"\"\"Imprime la serie de Fibonacci menor que n\"\"\"
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(2000)
```

El encabezado def debe ir seguido del nombre de la función y una lista de parámetros entre paréntesis. El cuerpo de la función se escribe indentado. La primera cadena del cuerpo puede ser una docstring, una cadena que documenta la función. Cuando se ejecuta una función:

Python crea una tabla de símbolos local para las variables y argumentos. La asignación de variables dentro de la función afecta a esta tabla local.

Los argumentos que se pasan al llamar a la función se introducen en la tabla local; el paso de argumentos se realiza por valor, pero ese valor es una referencia al objeto (lo que implica que se pueden modificar objetos mutables).

Si no se incluye ninguna instrucción return, la función devuelve el valor especial None. Para devolver un valor concreto se utiliza return expresión. Por ejemplo, la función fib2 devuelve la lista con los números de Fibonacci menores que n.

Las funciones se comportan como objetos de primera clase: se pueden asignar a variables, pasar como argumento a otras funciones o devolverlas como resultado. Esto permite construir código flexible y modular.

## 5. Uso de librerías estándar en funciones y clases

### 5.1 Módulo `math`

Ofrece funciones matemáticas como:  

- `math.sqrt(x)`  
- `math.factorial(n)`  
- `math.sin(x), math.cos(x), math.tan(x)`  

Se importa con:

```python
import math
```

---

### 5.2 Módulo `random`

Genera números pseudoaleatorios.  

Funciones útiles:  

- `random.random()` → flotante en `[0.0, 1.0)`  
- `random.randint(a, b)` → entero en `[a, b]`  
- `random.choice(seq)` → selecciona un elemento  

Se puede inicializar con `random.seed(valor)`.  



### 5.3 Módulo `datetime`

Permite manejar fechas y horas.  
Ejemplos:

- `datetime.datetime.now()`  
- `datetime.date(2025, 5, 2)`  
- `datetime1 - datetime2` → `timedelta`  

Se importa con:

```python
import datetime
```

---

## 6. Ejemplos integrados

### Ejemplo 1: Calculadora geométrica

```python
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def circunferencia(self):
        return 2 * math.pi * self.radio

def mostrar_info_circulo(radio):
    c = Circulo(radio)
    print(f"Radio: {radio}")
    print(f"Área: {c.area():.2f}")
    print(f"Circunferencia: {c.circunferencia():.2f}")

mostrar_info_circulo(3)
```

---

### Ejemplo 2: Juego de dados

```python
import random

class JuegoDado:
    def __init__(self, caras=6):
        self.caras = caras

    def lanzar(self):
        return random.randint(1, self.caras)

def jugar(dado, tiradas=5):
    print(f"Lanzando un dado de {dado.caras} caras {tiradas} veces:")
    for i in range(tiradas):
        print(f"Tirada {i+1}: {dado.lanzar()}")

dado6 = JuegoDado()
jugar(dado6)
```

---

### Ejemplo 3: Temporizador con `datetime`

```python
import datetime

class Temporizador:
    def __init__(self):
        self.inicio = datetime.datetime.now()

    def tiempo_transcurrido(self):
        return datetime.datetime.now() - self.inicio

def probar_temporizador():
    t = Temporizador()
    suma = sum(range(1_000_000))
    duracion = t.tiempo_transcurrido()
    print(f"Tiempo transcurrido: {duracion.total_seconds():.4f} segundos")

probar_temporizador()
```

## 7. Resumen y recomendaciones

- Las **clases** permiten agrupar datos y operaciones → base de la POO.  
- Los **métodos** operan sobre el estado interno de los objetos; `__init__` inicializa atributos; `self` da acceso a miembros.  
- Las **funciones** permiten modularizar y reutilizar código → crean ámbito local, aceptan parámetros, devuelven valores con `return`.  
- La **biblioteca estándar** ofrece módulos potentes:  
  - `math` para cálculos matemáticos.  
  - `random` para generar números aleatorios.  
  - `datetime` para trabajar con fechas y horas.  

Integrar funciones, clases y librerías estándar permite escribir programas **claros, reutilizables y robustos**.  
