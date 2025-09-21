# Practica 3

## Objetivos

- Integrar clases, conjuntos y ficheros CSV en un único proyecto.
- Leer información de horarios de un archivo CSV, crear objetos que representen cada registro y procesarla.
- Utilizar sets para eliminar duplicados y aplicar operaciones de unión, intersección y diferencia【435315475632304†L480-L518】.
- Guardar los resultados en un nuevo archivo CSV utilizando el módulo csv de la biblioteca estándar

## 1. Enunciado de la práctica

Supongamos que gestionas los horarios de un grupo de empleados. Tienes un fichero `horarios.csv` con los campos:

```csv
nombre_empleado;dia;hora_entrada;hora_salida
```

Cada línea contiene el nombre de un empleado, el día de la semana y sus horas de entrada y salida (valores enteros de 0–23). El objetivo de la práctica es:

- Leer el fichero CSV y convertir cada línea en un objeto de una clase `RegistroHorario` que almacene los datos de forma estructurada.
- Construir conjuntos de empleados para cada día y aplicar operaciones de teoría de conjuntos (unión, intersección y diferencia) para responder a preguntas como: ¿qué empleados trabajaron en todos los días? ¿Quiénes trabajaron sólo en un día concreto?.
- Calcular estadísticas (por ejemplo, horas totales trabajadas por cada empleado) y guardar los resultados en un nuevo fichero `resumen_horarios.csv`.

Al final de la práctica deberás producir un programa completo que lea los datos, los procese y genere los resultados solicitados.

## 2. Clase RegistroHorario

Para representar cada entrada de `horarios.csv` definiremos la clase `RegistroHorario`. Esta clase contendrá los atributos `empleado`, `dia`, `entrada` y `salida`, y un método que calcule la duración del turno en horas.

```python
class RegistroHorario:
    def __init__(self, empleado: str, dia: str, entrada: int, salida: int):
        self.empleado = empleado
        self.dia = dia
        self.entrada = entrada
        self.salida = salida

    def duracion(self) -> int:
        """Devuelve la cantidad de horas trabajadas en este registro"""
        return self.salida - self.entrada
```

Cada vez que crees una instancia con `RegistroHorario('Ana','Lunes',9,17)` se almacenarán los valores en los atributos correspondientes. El método `duracion` devuelve la diferencia entre la hora de salida y la de entrada.

## 3. Lectura del CSV y creación de objetos

Python dispone del módulo `csv` para leer archivos en formato Comma Separated Values. La función `csv.reader` devuelve un objeto lector que itera sobre las filas del archivo y entrega cada fila como una lista de cadenas.

- Es importante abrir el archivo con `newline=''` para que el módulo gestione correctamente los saltos de línea
- La conversión de campos a números se realiza manualmente.

El siguiente ejemplo ilustra cómo leer `horarios.csv` y crear una lista de objetos `RegistroHorario`:

```python
import csv

registros = []
with open('horarios.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';', quotechar='"')
    for fila in lector:
        # Cada fila es una lista de cadenas: [nombre, dia, entrada, salida]
        nombre, dia, h_entrada, h_salida = fila
        # Convertimos las horas a enteros
        entrada = int(h_entrada)
        salida = int(h_salida)
        registro = RegistroHorario(nombre, dia, entrada, salida)
        registros.append(registro)

print(f"Se han leído {len(registros)} registros")
```

Tras ejecutar este fragmento, dispondrás de una lista de objetos `RegistroHorario` que puedes recorrer y procesar con normalidad. Si el CSV tuviera encabezados, podrías omitir la primera fila o utilizar `csv.DictReader` para mapear cada fila a un diccionario.

## 4. Conjuntos para agrupar y operar con empleados

Los conjuntos (`set`) son colecciones desordenadas de elementos únicos. Son ideales para eliminar duplicados y para realizar operaciones de unión, intersección y diferencia. Vamos a utilizarlos para crear un conjunto de empleados por cada día y comparar quién ha trabajado en varios días.

Primero, construimos un diccionario que asocie cada día con el conjunto de empleados que han trabajado ese día:

```python
empleados_por_dia = {}
for registro in registros:
    # Creamos el conjunto para el día si no existe
    if registro.dia not in empleados_por_dia:
        empleados_por_dia[registro.dia] = set()
    # Añadimos el empleado al conjunto del día
    empleados_por_dia[registro.dia].add(registro.empleado)

# Mostrar empleados por día
for dia, empleados in empleados_por_dia.items():
    print(f"{dia}: {empleados}")
```

Una vez que tengas estos conjuntos, puedes usar las operaciones de la teoría de conjuntos:

- Unión (|): empleados que trabajaron en al menos alguno de los días. Por ejemplo, `empleados_por_dia['Lunes'] | empleados_por_dia['Martes']` devuelve el conjunto de empleados que trabajaron el lunes o el martes.

- Intersección (&): empleados que trabajaron en ambos días. Por ejemplo, `empleados_por_dia['Lunes'] & empleados_por_dia['Martes']` devuelve quienes trabajaron los dos días.

- Diferencia (-): empleados que trabajaron en un día pero no en otro; `empleados_por_dia['Lunes'] - empleados_por_dia['Martes']` lista quienes trabajaron sólo el lunes.

- Diferencia simétrica (^): empleados que trabajaron en exactamente uno de los días, pero no en ambos.

Los conjuntos también se pueden construir con set comprehensions, una sintaxis compacta que permite aplicar filtros mientras se construye el conjunto. Por ejemplo, para obtener la lista de empleados que han trabajado al menos 8 horas en algún día:

```python
empleados_turno_largo = {r.empleado for r in registros if r.duracion() >= 8}
print(empleados_turno_largo)
```

## 5. Cálculo de estadísticas y escritura del resultado en CSV

Además de usar conjuntos para comparar empleados, es habitual resumir la información en un fichero de salida. Utilizaremos un diccionario para acumular las horas totales trabajadas por cada empleado y luego escribiremos el resultado en un nuevo fichero CSV utilizando `csv.writer`. Al igual que al leer, el fichero debe abrirse con `newline=''` y cualquier dato no textual se convertirá en cadena automáticamente.

```python
import csv

# Calcular horas totales por empleado
horas_totales = {}
for registro in registros:
    horas_totales.setdefault(registro.empleado, 0)
    horas_totales[registro.empleado] += registro.duracion()

# Escribir un resumen en un nuevo CSV
with open('resumen_horarios.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Cabecera
    escritor.writerow(['Empleado', 'Horas totales'])
    # Filas con los datos acumulados
    for empleado, total in horas_totales.items():
        escritor.writerow([empleado, total])

print("Se ha generado el fichero resumen_horarios.csv")
```

El módulo `csv.writer` convierte automáticamente los valores no textuales a cadenas antes de escribir. Con estos pasos conseguimos un informe que resume las horas trabajadas por cada empleado.

## 6. Ejercicios

- Empleados madrugadores. Añade un parámetro `hora_referencia` a tu programa y utiliza un conjunto para obtener los nombres de los empleados que comienzan su turno antes de esa hora. Guarda el resultado en un nuevo archivo `madrugadores.csv` con los campos `empleado` y `hora_entrada`.

- Intersección de días. Calcula el conjunto de empleados que trabajaron tanto el lunes como el viernes. Muestra sus nombres por pantalla y escribe la lista en `en_dos_dias.csv`.

- Empleados exclusivos.Crea un conjunto con los empleados que trabajaron el sábado pero no el domingo. ¿Qué operación de conjuntos has utilizado?

- Resumen semanal. Completa el ejemplo de la sección 5 para calcular, además de las horas totales, el número de días trabajados por cada empleado (puedes usar un `set` dentro del diccionario para evitar contar días repetidos). Escribe el resultado en `resumen_semanal.csv` con los campos `empleado`, `dias_trabajados` y `horas_totales`.

- Filtrado por duración. Usa una set comprehension para obtener el conjunto de empleados que han trabajado al menos 6 horas en todas sus jornadas. Ten en cuenta que necesitarás comprobar cada registro de cada empleado.

- Diseñar clases para empleados y gestión. Define una clase Empleado que almacene el nombre de un trabajador y una lista de sus registros (RegistroHorario). Implementa métodos para añadir registros (agregar_registro), calcular las horas totales trabajadas (horas_totales), obtener el número de días distintos trabajados (dias_trabajados) y devolver una fila para el CSV de resumen (fila_csv). Además, crea una clase GestorHorarios que se encargue de leer el fichero de entrada, agrupar los registros por empleado y escribir el resumen en un archivo. Utiliza estas nuevas clases para generar un fichero resumen_clases.csv con los campos empleado, dias_trabajados y horas_totales.

---
