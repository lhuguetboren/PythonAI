# Resumen de sintaxis y funciones de Python

| Categoría | Palabra clave / Función | Descripción | En el material |
|---|---|---|---|
| **Definición y POO** | `class` | Define una clase | ✅ |
|  | `def` | Define una función | ✅ |
|  | `return` | Devuelve un valor desde una función | ✅ |
|  | `__init__` | Constructor de clase | ✅ |
|  | `self` | Referencia a la instancia actual | ✅ |
|  | `pass` | No hace nada, marcador de posición | ✅ |
| **Control de flujo** | `if` / `elif` / `else` | Condicionales | ✅ |
|  | `for` | Bucle sobre secuencias | ✅ |
|  | `while` | Bucle mientras la condición sea verdadera | ✅ |
|  | `break` | Rompe un bucle | ✅ |
|  | `continue` | Salta a la siguiente iteración | ✅ |
|  | `match` / `case` | Patrón de coincidencia (Python 3.10+) | ✅ |
|  | `in` / `not in` | Comprueba pertenencia | ✅ |
|  | `is` / `is not` | Comparación de identidad | ✅ |
| **Manejo de errores** | `try` / `except` | Captura excepciones | ✅ |
|  | `else` (en try) | Bloque si no hubo excepción | ✅ |
|  | `finally` | Se ejecuta siempre tras try/except | ✅ |
|  | `raise` | Lanza una excepción | ❌ |
| **Entrada / Salida** | `input()` | Entrada de usuario | ✅ |
|  | `print()` | Salida en pantalla | ✅ |
| **Gestión de ficheros** | `open(nombre, modo, encoding)` | Abre un archivo y devuelve un objeto fichero | ✅ |
|  | `with open(...) as f:` | Context manager que asegura cierre automático | ✅ |
|  | `f.read([size])` | Lee todo el archivo o `size` caracteres | ✅ |
|  | `f.readline()` | Lee una línea completa | ✅ |
|  | `f.readlines()` | Devuelve todas las líneas como lista | ✅ |
|  | `f.write(cadena)` | Escribe texto en un archivo | ✅ |
|  | `f.writelines(lista)` | Escribe una lista de cadenas | ❌ |
|  | `f.seek(pos)` | Cambia la posición del puntero | ✅ |
|  | `f.tell()` | Devuelve posición actual del puntero | ✅ |
|  | `os.remove()` | Elimina un archivo | ✅ |
|  | `os.rename()` | Renombra un archivo | ✅ |
|  | `os.rmdir()` | Elimina un directorio vacío | ✅ |
|  | `shutil.copy()` | Copia un archivo | ✅ |
|  | `shutil.move()` | Mueve un archivo | ✅ |
|  | `shutil.rmtree()` | Elimina un directorio con contenido | ✅ |
|  | `csv.reader()` | Lee un archivo CSV | ✅ |
|  | `csv.writer()` | Escribe en un archivo CSV | ✅ |
|  | `csv.DictReader()` | Lee CSV en forma de diccionario | ✅ |
|  | `csv.DictWriter()` | Escribe CSV desde diccionario | ✅ |
|  | `json.dump()` | Escribe objeto en JSON a archivo | ✅ |
|  | `json.dumps()` | Convierte objeto a string JSON | ✅ |
|  | `json.load()` | Carga objeto desde archivo JSON | ✅ |
|  | `json.loads()` | Convierte string JSON a objeto | ✅ |
| **Funciones útiles** | `len()` | Devuelve la longitud | ❌ |
|  | `enumerate()` | Devuelve índice y valor al iterar | ✅ |
|  | `range()` | Genera una secuencia de números | ✅ |
|  | `zip()` | Agrupa elementos de varios iterables | ✅ |
|  | `type()` | Devuelve el tipo de un objeto | ✅ |
|  | `int()`, `str()`, `float()` | Conversión de tipos | ✅ |
| **Strings** | `str.upper()` | Convierte a mayúsculas | ❌ |
|  | `str.lower()` | Convierte a minúsculas | ❌ |
|  | `str.title()` | Capitaliza cada palabra | ❌ |
|  | `str.strip()` | Elimina espacios al inicio/fin | ❌ |
|  | `str.split()` | Divide en lista | ❌ |
|  | `str.join()` | Une lista de strings | ❌ |
|  | `str.replace()` | Reemplaza subcadenas | ❌ |
|  | `str.find()` | Busca una subcadena | ❌ |
| **Listas** | `list.append()` | Añade un elemento al final | ✅ |
|  | `list.insert()` | Inserta en posición i | ✅ |
|  | `list.remove()` | Elimina la primera aparición | ✅ |
|  | `list.pop()` | Extrae un elemento | ✅ |
|  | `list.sort()` | Ordena en su lugar | ✅ |
|  | `sorted()` | Devuelve una lista ordenada | ✅ |
|  | `list.reverse()` | Invierte la lista | ✅ |
|  | `list.count()` | Cuenta apariciones | ✅ |
|  | `list.index()` | Devuelve índice de elemento | ✅ |
| **Conjuntos** | `set.add()` | Añade un elemento | ✅ |
|  | `set.remove()` | Elimina un elemento (error si no existe) | ✅ |
|  | `set.discard()` | Elimina un elemento sin error | ✅ |
|  | `set.union()` | Unión de conjuntos | ✅ |
|  | `set.intersection()` | Intersección de conjuntos | ✅ |
|  | `set.difference()` | Diferencia de conjuntos | ✅ |
|  | `set.clear()` | Vacía el conjunto | ✅ |
| **Diccionarios** | `dict.get()` | Obtiene un valor con clave | ✅ |
|  | `dict.keys()` | Devuelve claves | ✅ |
|  | `dict.values()` | Devuelve valores | ✅ |
|  | `dict.items()` | Devuelve pares clave-valor | ✅ |
|  | `dict.update()` | Actualiza con otro dict | ✅ |
|  | `dict.pop()` | Elimina clave y devuelve valor | ✅ |
| **Números** | `abs()` | Valor absoluto | ❌ |
|  | `round()` | Redondeo | ❌ |
|  | `max()` | Máximo de un iterable | ❌ |
|  | `min()` | Mínimo de un iterable | ❌ |
|  | `sum()` | Suma de un iterable | ❌ |
| **Generales avanzadas** | `map()` | Aplica una función a cada elemento | ❌ |
|  | `filter()` | Filtra elementos | ❌ |
|  | `any()` | True si algún elemento es verdadero | ❌ |
|  | `all()` | True si todos son verdaderos | ❌ |

