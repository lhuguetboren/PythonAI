# Practica 2

## Objetivos

- Primer contacto con las funciones en Python y por qué se utilizan para estructurar programas.  
- Aprender a definir funciones con la palabra reservada `def`.  
- Aplicar estructuras básicas como diccionarios, bucles `for` y condicionales para resolver un problema sencillo de control de horarios.  
- Practicar técnicas de depuración con el depurador incorporado de Python y conocer los pasos para depurar en Visual Studio Code.  

---

## 1. ¿Por qué utilizar funciones con `def`?

En Python, una función es un bloque de código reutilizable que se define mediante la palabra clave `def`, seguida del nombre de la función, una lista de parámetros opcionales entre paréntesis y dos puntos. Todo el cuerpo de la función debe ir indentado.  

Al invocar una función, Python crea una tabla de símbolos local donde se guardan los parámetros y las variables definidas en el cuerpo. Esto significa que las variables asignadas dentro de una función no afectan a las variables fuera de ella.

Si una función no incluye la sentencia `return`, devolverá automáticamente el objeto especial `None` al terminar.  

---

## 2. Descripción del programa

El programa **`horario_minimo.py`** es un ejercicio introductorio en el que se gestiona un conjunto de horarios de empleados: los datos están codificados directamente en el propio script mediante un diccionario.  

Cada entrada del diccionario asocia el nombre de una persona con una tupla de dos cadenas, la primera indicando la hora de entrada y la segunda la hora de salida.  

Ejemplo:  
`'María': ('08', '16')` indica que María entra a las 8 h y sale a las 16 h.  

El programa define tres funciones principales:

- **`mostrar_registros()`** – Recorre el diccionario y muestra todos los empleados con sus horas. Utiliza `enumerate(horarios.items(), start=1)` para numerar la salida comenzando en uno.  
- **`contar_entradas()`** – Solicita al usuario una hora (0–23), valida la entrada y cuenta cuántas personas han llegado antes o a esa hora.  
- **`menu()`** – Presenta un menú repetitivo mediante un bucle `while` para que el usuario elija entre mostrar registros, contar entradas o salir.  

Mediante estas funciones, el programa demuestra cómo dividir el código en bloques lógicos e interactuar con el usuario de forma sencilla.  

---

## 3. Cómo crear el programa

### Definir los datos

```python
horarios = {
    'María': ('08', '16'),
    'Juan':  ('09', '17'),
    # ... más entradas
}
```

### Mostrar registros

Define una función `mostrar_registros()` que recorra el diccionario.  
Para numerar los elementos a partir de 1, usa:

```python
enumerate(horarios.items(), start=1)
```

### Contar entradas

Crea una función `contar_entradas()` que solicite al usuario una hora en formato entero (0–23).  

- Valida la entrada con `try/except`.  
- Inicializa un contador en cero.  
- Convierte la hora de entrada a entero y compárala con la hora introducida.  
- Incrementa el contador si corresponde.  

### Menú principal

Implementa una función `menu()` que muestre un menú textual con tres opciones:  

1. Mostrar registros  
2. Contar entradas  
3. Salir  

El menú debe ejecutarse hasta que el usuario introduzca la opción de salida.  

### Punto de entrada

```python
if __name__ == '__main__':
    menu()
```

---

## 5. Depuración en Visual Studio Code

Pasos:

1. Abrir la carpeta que contiene `horario_minimo.py`.  
2. Ir a **Run and Debug** (Ctrl+Shift+D) y seleccionar *Python File*.  

VS Code generará un `launch.json` para configurar la depuración.  

Ahora puedes:  

- Colocar puntos de ruptura con clic en el margen.  
- Ejecutar con **F5**.  
- Observar variables, pila de llamadas y usar la consola interactiva.  

Si necesitas pausar la ejecución desde el propio código:

```python
import debugpy
debugpy.breakpoint()
```

---

## 6. Actividades sugeridas

- **Ampliar los horarios** – Añade un par de empleados más al diccionario `horarios`. ¿Cambia algo en el resto del programa?  
- **Validar la entrada** – Mejora `contar_entradas()` para aceptar horas con minutos (`'08:30'`).  
- **Refactorizar el código** – Crea una función para la validación de la hora y reutilízala.  
- **Practicar con `enumerate`** – Cambia la numeración inicial a 0 en `mostrar_registros()`.  
- **Depuración visual** – Usa VS Code para depurar `contar_entradas()`.  

---
