# Estructuras de Control

## Objetivos

- Dominar las instrucciones condicionales y comprender que Python basa su sintaxis en la sangría, no en llaves ni paréntesis.

- Repetir tareas con bucles for y while, incluyendo técnicas de iteración como range(), enumerate() y zip(), y comprender cómo interrumpir o continuar la ejecución.

- Gestionar el flujo de ejecución cuando ocurren errores mediante bloques try/except/else/finally y aprender a lanzar excepciones propias.

- Conocer nuevas construcciones de control como la expresión condicional en línea y la sentencia match introducida en Python 3.10.

### 1. Condicionales

Las sentencias condicionales permiten ejecutar bloques de código sólo si se cumple una condición. En Python no se utilizan paréntesis ni llaves como en Java o PHP; la sintaxis se basa en la palabra clave (if, elif, else), seguida de dos puntos (:) y un bloque indentado.

- if → Evalúa una condición. Si es verdadera, ejecuta el bloque de código que contiene.
- elif (else if) → Permite comprobar una condición adicional si la primera no se cumple. Se pueden encadenar varios elif.
- else → Se ejecuta solo si ninguna de las condiciones anteriores (if o elif) se cumple.
- : → Marca el inicio del bloque de código que depende de la condición.

**Indentación (tabulación) → En Python es obligatoria; indica qué instrucciones pertenecen al bloque.**

``` mermaid
flowchart TD
    A([Inicio]) --> C1{¿condición 1?}
    C1 -- Sí --> B1[Bloque if]
    C1 -- No --> C2{¿condición 2?}
    C2 -- Sí --> B2[Bloque elif]
    C2 -- No --> BE[ Bloque else ]
    B1 --> Z([Fin])
    B2 --> Z
    BE --> Z
    %% Estructura if / elif / else

```

```python
edad = 18

if edad < 12:
    print("Eres un niño")
elif edad < 18:
    print("Eres adolescente")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres mayor")

```

**Expresión condicional (operador ternario)**

Python dispone de una expresión condicional para asignar valores según una condición. Su forma es valor_si_verdadero if condicion else valor_si_falso. Permite escribir decisiones simples en una sola línea y equivale al operador ternario condición ? a : b de otros lenguajes.

``` mermaid
flowchart TD
    A([Inicio]) --> C{¿condición?}
    C -- Sí --> T[valor_si_verdadero]
    C -- No --> F[valor_si_falso]
    T --> AS[Asignar a variable]
    F --> AS
    AS --> Z([Fin])
    %% Expresión condicional: v = a if cond else b
```

```python
mensaje = "par" if numero % 2 == 0 else "impar"
```

**La sentencia match**

Desde Python 3.10 existe la sentencia match para comparar un valor contra varios patrones, similar al switch pero más potente. Solo se ejecuta el primer patrón que coincide se puede usar _ como comodín y agrupar varios valores con |

``` mermaid
flowchart TD
    A([Inicio]) --> M[match estado]
    M --> C400{==400}
    C400 -- Si --> R400[Peticion incorrecta]
    C400 -- No --> C404{==404}
    C404 -- Si --> R404[No encontrado]
    C404 -- No --> C418{==418}
    C418 -- Si --> R418[Soy una tetera]
    C418 -- No --> DEF[_ -> Error desconocido]
    R400 --> Z([Fin])
    R404 --> Z
    R418 --> Z
    DEF --> Z
```

```python
def http_error(status):
    match status:
        case 400:
            return "Petición incorrecta"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"
        case _:
            return "Error desconocido"
```

La sentencia match puede desempaquetar tuplas o atributos de objetos, lo que la hace útil para comparar estructuras de datos complejas

### 2. Bucles

**Bucle for**

El bucle for de Python itera directamente sobre los elementos de una secuencia (listas, tuplas, cadenas, conjuntos, diccionarios, generadores, etc.), no sobre índices como en C, Java o PHP. Para recorrer números en progresión se utiliza la función integrada range() que genera una sucesión aritmética sin crear una lista completa en memoria.

- range(fin) genera números desde 0 hasta fin-1.
- range(inicio, fin, paso) permite especificar un valor inicial, final (exclusivo) y un incremento (puede ser negativo)
- Es posible iterar sobre los índices de una lista combinando range() y len(), aunque la función enumerate() resulta más cómoda porque devuelve pares (índice, elemento) y evita tener que calcular la longitud manualmente.

``` mermaid
flowchart TD
    A([Inicio]) --> I[Iterador]
    I --> L{Quedan elementos}
    L -- No --> ELS[Ejecuta else] --> Z([Fin])
    L -- Si --> GET[Tomar elemento]
    GET --> B?{break}
    B? -- Si --> Z
    B? -- No --> C?{continue}
    C? -- Si --> L
    C? -- No --> BODY[Cuerpo for]
    BODY --> L


```


```python
# Recorrer una lista de forma directa
nombres = ["Ana", "Luis", "Sofía"]
for nombre in nombres:
    print(nombre.upper())

# Recorrer números con range
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# Range con inicio y paso
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

# Usando enumerate para obtener índice y valor
for indice, valor in enumerate([10, 20, 30]):
    print(f"Índice {indice}: {valor}")

# Iterar dos listas a la vez con zip
nombres = ["Ana", "Luis", "Sofía"]
edades  = [20, 22, 19]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

```

**Control de bucles**

- `break` sale inmediatamente del bucle más interno.
- `continue` salta a la siguiente iteración del bucle, sin ejecutar el resto del bloque
- Un bucle `for` o `while` puede tener un `else`, que se ejecuta solo si el bucle termina sin un `break` . Es útil para buscar elementos: si no se encuentran, el else notifica la ausencia.
- `pass`:  no hace nada y sirve como marcador de posición en bloques vacío



```python
# Buscar un número primo utilizando for-else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} es igual a {x} × {n//x}")
            break  # sale del bucle interior
    else:
        # se ejecuta si no se encontró divisor (no hubo break)
        print(f"{n} es un número primo")

# Uso de continue para saltar números pares
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Encontrado par {num}")
        continue  # salta a la siguiente iteración
    print(f"Encontrado impar {num}")
```

```python
# Tabla de multiplicar del 1 al 3 (for anidado)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")
    print("---")
```

**Bucle while**

El bucle while repite su cuerpo mientras la condición se mantenga verdadera. Es útil para bucles de duración indeterminada y se debe actualizar la condición dentro del bucle para evitar iteraciones infinitas. Al igual que en el for, se puede utilizar un else para ejecutar un bloque cuando el bucle termina de forma natura

``` mermaid
flowchart TD
    A([Inicio]) --> C{condicion while}
    C -- No --> ELS[Ejecuta else] --> Z([Fin])
    C -- Si --> BODY[Cuerpo while]
    BODY --> B?{break}
    B? -- Si --> Z
    B? -- No --> CONT?{continue}
    CONT? -- Si --> C
    CONT? -- No --> C


```

```python
x = 5
while x > 0:
    print(x)
    x -= 1
else:
    print("¡Despegue!")
```

**Bucles anidados y pass**

Se pueden anidar bucles for y while dentro de otros. Python dispone de la sentencia pass que no hace nada y sirve como marcador de posición en bloques vacío

```python
# Tabla de multiplicar del 1 al 3 (for anidado)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")
    print("---")

# Bucle while anidado dentro de otro while
fila = 1
while fila <= 3:
    columna = 1
    while columna <= 3:
        print(f"Fila {fila}, Columna {columna}")
        columna += 1
    fila += 1

# Bloque pass como placeholder
for i in range(3):
    pass  # se usa cuando aún no se ha implementado el bloque
```

### 3. Manejo de errores

Python diferencia entre errores de sintaxis y excepciones. Los errores sintácticos impiden que el programa arranque, mientras que las excepciones ocurren durante la ejecución y pueden ser atrapadas y gestionadas. Las excepciones predefinidas como ZeroDivisionError, NameError o TypeError indican qué clase de problema ocurrió.

`try...except`

El bloque `try` se utiliza para envolver el código que podría generar un error. Si se produce una excepción dentro del bloque, se buscan cláusulas `except` que la manejen. Se pueden capturar tipos específicos o un conjunto de ellos usando una tupla. Capturar excepciones específicas ayuda a identificar mejor los problemas y no ocultar errores inesperados.

```else  finally```

La cláusula `else` debe seguir a todos los except y se ejecuta solo si el bloque `try` no genera ninguna excepción. Es útil para colocar código que debe ejecutarse cuando todo ha ido bien, evitando interceptar excepciones fuera de lugar.

La cláusula `finally` se ejecuta siempre, tanto si hay una excepción como si no. Se usa para realizar tareas de limpieza: cerrar archivos, liberar recursos o mostrar mensajes finales.

``` mermaid
flowchart TD
    A([Inicio]) --> TRY[try]
    TRY --> EXC{excepcion?}
    EXC -- No --> ELSE[else]
    EXC -- Si --> CHK1{except 1}
    CHK1 -- Si --> H1[Manejar exc 1]
    CHK1 -- No --> CHK2{except 2}
    CHK2 -- Si --> H2[Manejar exc 2]
    CHK2 -- No --> PROP[Propagar error]
    ELSE --> FINALLY[finally]
    H1 --> FINALLY
    H2 --> FINALLY
    PROP --> FINALLY
    FINALLY --> Z([Fin])

```

```python
try:
    num = int(input("Introduce un número: "))
    resultado = 10 / num
except ZeroDivisionError:
    print("No puedes dividir entre 0")
except ValueError:
    print("Debes introducir un número válido")
except (TypeError, NameError):
    print("Otro tipo de error")
else:
    # se ejecuta solo si no hubo excepción
    print(f"El resultado es {resultado}")
finally:
    # se ejecuta siempre, haya o no excepción
    print("Ejecución finalizada")
```
