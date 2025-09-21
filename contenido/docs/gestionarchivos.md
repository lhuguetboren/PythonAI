# Gestión de archivos

## Objetivos

- Entender cómo abrir, cerrar, leer y escribir archivos en Python de forma segura.
- Diferenciar entre modos de apertura (lectura, escritura, añadir; texto vs binario) y saber cuándo usar cada uno  
- Utilizar el gestor de contexto with para garantizar el cierre automático de los archivos  
- Eliminar y renombrar archivos y directorios mediante el módulo os  
- Manipular distintos tipos de archivos: texto plano, CSV y JSON, utilizando los módulos csv y json de la biblioteca estándar  

## 1. Manejo básico de archivos

Para trabajar con archivos en Python se utiliza la función incorporada open(), que devuelve un objeto de archivo. Su llamada más común acepta tres argumentos: nombre de archivo, modo de apertura y codificación  

```python
f = open('datos.txt', 'w', encoding='utf-8')
```

- Primer argumento ('datos.txt'): ruta o nombre del archivo.  
- Segundo argumento ('w'): modo de apertura. Los más utilizados son:  
  - 'r' lectura (por defecto). El archivo debe existir.  
  - 'w' escritura. Crea un archivo nuevo o trunca el existente  
  - 'a' añadir. Abre el archivo para append; lo nuevo se añade al final  
  - 'r+' lectura y escritura.  
  - Añadir 'b' lo abre en modo binario (lee y escribe objetos bytes). Sin 'b' se trabaja en modo texto, que lee y escribe cadenas con un determinado encoding  

- Tercer argumento (encoding='utf-8'): codificación del texto. Se recomienda especificarlo para evitar problemas con caracteres especiales  

### Uso del gestor de contexto

Para asegurar que el archivo se cierra correctamente, incluso si ocurre una excepción, se usa el gestor de contexto with:

```python
with open('datos.txt', 'w', encoding='utf-8') as f:
    f.write('Primera línea\n')  # el archivo se cierra automáticamente al salir del bloque
```

Al finalizar el bloque with, el archivo se cierra sin necesidad de llamar a f.close()  

### Lectura de archivos

Una vez abierto un archivo en modo lectura ('r'), existen varias formas de obtener su contenido:

- f.read([size]): lee todo el archivo o size caracteres/bytes  
- f.readline(): lee una línea completa  
- Iterar sobre el archivo: recorrerlo con for line in f  
- f.readlines(): devuelve una lista con todas las líneas del archivo  

### Escritura de archivos

- f.write(cadena): escribe la cadena y devuelve el número de caracteres escritos  
- Importante: convertir otros tipos a cadena antes de escribirlos  

### Posicionamiento

- f.tell() y f.seek(offset, whence) permiten conocer y modificar la posición actual del puntero  

---

## 2. Eliminación y renombrado de archivos

El módulo os proporciona funciones para manipular el sistema de archivos:

```python
import os

# eliminar un archivo
os.remove('datos.txt')  # lanza FileNotFoundError si no existe

# renombrar
os.rename('datos_viejos.txt', 'datos_nuevos.txt')

# borrar un directorio vacío
os.rmdir('carpeta_vacia')
```

Para operaciones de alto nivel el módulo shutil ofrece funciones como shutil.copy(), shutil.move() y shutil.rmtree().

---

## 3. Tipos de archivos y bibliotecas estándar

### 3.1 Texto plano

Los archivos de texto plano (extensiones .txt, .log, etc.) se leen y escriben como cadenas en modo texto. La codificación y la conversión automática de saltos de línea se gestionan al abrir el archivo  Estos archivos son ideales para guardar información sencilla lineal o registros de log.

### 3.2 CSV

El módulo csv simplifica la lectura y escritura de archivos Comma Separated Values. Para leer un CSV se utiliza csv.reader, que devuelve un reader object. Cada fila se devuelve como una lista de cadenas y no se realiza conversión de tipos automáticamente  El archivo debe abrirse con newline='' para evitar que el módulo convierta los saltos de línea de manera incorrecta.

```python
import csv

# Leer un CSV
with open('alumnos.csv', newline='', encoding='utf-8') as csvfile:
    lector = csv.reader(csvfile, delimiter=';', quotechar='"')
    for fila in lector:
        nombre, edad, ciudad = fila
        print(nombre, edad, ciudad)

# Escribir un CSV
with open('salida.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])
    escritor.writerow(['Ana', 30, 'Barcelona'])
```

Para trabajar con diccionarios se utilizan csv.DictReader y csv.DictWriter  

### 3.3 JSON

El formato JSON (JavaScript Object Notation) almacena estructuras de datos como diccionarios y listas. El módulo json permite serializar objetos Python a JSON (json.dump() y json.dumps()) y deserializar JSON a objetos Python (json.load() y json.loads()).

Serializar a archivo: json.dump(objeto, archivo) escribe el objeto en formato JSON en un archivo. El archivo debe estar abierto en modo escritura y aceptar cadenas (str)

Serializar a cadena: json.dumps(objeto) devuelve una cadena JSON.

Leer de archivo: json.load(archivo) lee el JSON del archivo y lo convierte en una estructura de datos Python 

Leer desde cadena: json.loads(cadena) deserializa una cadena JSON a Python.

Las claves en un objeto JSON siempre son cadenas; convertir un diccionario con claves de otro tipo puede alterar la estructura.

```python
import json

datos = {
    'alumnos': [
        {'nombre': 'Ana', 'edad': 25},
        {'nombre': 'Luis', 'edad': 23}
    ]
}

# Escribir JSON en un archivo
with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=4)

# Leer JSON desde un archivo
with open('datos.json', encoding='utf-8') as f:
    datos_cargados = json.load(f)
    print(datos_cargados['alumnos'][0]['nombre'])  # 'Ana'
```

La función indent en json.dump() genera un fichero legible.  

---
