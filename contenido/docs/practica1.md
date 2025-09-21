# Practica 1

## Objetivos

* Consolidar el uso de **variables simples**, entrada de datos con `input()` y salida con `print()`.  
* Practicar **condicionales** (`if`/`else`) y **bucles** `while` para repetir acciones según un contador.  
* Trabajar con datos numéricos y realizar comparaciones para contar y encontrar valores mínimos.  
* Crear un programa completo **sin emplear funciones, diccionarios ni listas**, de modo que el alumno se concentre en el flujo de control básico.

---

## 1. Enunciado del ejercicio

Se pide desarrollar un pequeño programa que lea información sobre varios empleados y sus horarios de entrada y salida.

1. Preguntar al usuario cuántos empleados va a introducir y pedir una hora de referencia (0–23) para comparar las entradas.  
2. Iterar tantas veces como empleados haya indicado el usuario. En cada iteración se solicitará el nombre del empleado y sus horas de entrada y salida (enteros entre 0 y 23). Se debe validar que la hora de salida sea mayor que la de entrada.  
3. Contar cuántos empleados han entrado antes o a la hora de referencia.  
4. Determinar qué empleado tiene la salida más temprana.  
5. Mostrar al final del programa el número de empleados que cumplen la condición y el nombre de quien salió primero.

---

## 2. Claves de implementación

1. **Variables iniciales**. Declara variables para llevar el recuento de entradas (`contador_entradas`) y para almacenar la salida más temprana (`salida_mas_temprana`) y el nombre del empleado correspondiente. 

2. **Entrada de datos**. Utiliza la función `input()` para pedir al usuario el número de empleados y la hora de referencia, y conviértelos a enteros. Valida que sean números positivos y que la hora esté en el rango 0–23. Si la validación falla, muestra un mensaje y termina la ejecución o solicita de nuevo los datos.

3. **Bucle de iteración**. Emplea un bucle `while` con un contador para pedir los datos de cada empleado. Este tipo de bucle repite sus instrucciones mientras la condición sea verdadera.

   - Solicita el nombre y las horas de entrada y salida.  
   - Convierte las horas a enteros y comprueba que estén en el intervalo permitido. Si no lo están o la salida no supera a la entrada, muestra un mensaje y repite la iteración sin avanzar el contador.  
   - Compara la hora de entrada con la hora de referencia; si es menor o igual, incrementa `contador_entradas`.  
   - Compara la hora de salida con `salida_mas_temprana`; si es menor, actualiza ambas variables con la nueva salida y el nombre del empleado.  
   - Incrementa el contador del bucle para pasar al siguiente empleado.

4. **Salida de resultados**. Después de salir del bucle, utiliza `print()` para mostrar el número de empleados que entraron antes o a la hora de referencia y, si se determinó alguno, el nombre y la hora de la salida más temprana.

---

## 3. Sugerencias de depuración

En Visual Studio Code, abre el archivo `.py` y utiliza el panel **Run and Debug** para depurar el script. Selecciona **Python File** como configuración, establece un punto de ruptura en la línea de actualización de `salida_mas_temprana` y ejecuta la depuración. Podrás observar la evolución de las variables en los paneles de variables y la pila de llamadas.
