"""
===========================================
   REGULAR EXPRESSIONS (Expresiones regulares)
===========================================

Las expresiones regulares permiten buscar o validar texto 
siguiendo un patrón.

Funciones principales del módulo 're':

1 re.match(patrón, texto)
    - Busca solo al inicio del texto.

2 re.search(patrón, texto)
    - Busca la primera coincidencia en cualquier parte del texto.

3 re.findall(patrón, texto)
    - Devuelve una lista con todas las coincidencias.

4 re.finditer(patrón, texto)
    - Igual que findall, pero devuelve objetos Match (con posición y grupo).

5 re.fullmatch(patrón, texto)
    - Solo hay coincidencia si todo el texto encaja con el patrón.

Símbolos útiles en patrones:
--------------------------------
^  → inicio de línea
$  → final de línea
.  → cualquier carácter
\d → dígito (0–9)
\w → carácter alfanumérico
+  → una o más repeticiones
*  → cero o más repeticiones
?  → opcional
{n,m} → entre n y m repeticiones

Ejemplos prácticos abajo 👇
"""

import re

# =============================
# Ejemplo 1: re.match()
# =============================
print("=== re.match() ===")
texto = "Hola mundo"
print(re.match(r"Hola", texto))   # ✅ Coincide (inicio)
print(re.match(r"mundo", texto))  # ❌ No coincide (no está al inicio)

# =============================
# Ejemplo 2: re.search()
# =============================
print("\n=== re.search() ===")
print(re.search(r"mundo", texto))  # ✅ Encuentra "mundo" en cualquier parte

# =============================
# Ejemplo 3: re.findall()
# =============================
print("\n=== re.findall() ===")
frase = "uno, dos, tres, dos, uno"
print(re.findall(r"dos", frase))   # ['dos', 'dos']

# =============================
# Ejemplo 4: re.finditer()
# =============================
print("\n=== re.finditer() ===")
for m in re.finditer(r"dos", frase):
    print(f"'{m.group()}' en posición {m.start()}–{m.end()}")

# =============================
# Ejemplo 5: re.fullmatch()
# =============================
print("\n=== re.fullmatch() ===")
print(re.fullmatch(r"\d{3}", "123"))   # ✅ Coincide todo el texto
print(re.fullmatch(r"\d{3}", "1234"))  # ❌ No coincide completamente

# =============================
# Ejemplo 6: validación básica de email
# =============================
print("\n=== Validación simple de email ===")
email = "usuario@dominio.com"
patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(patron, email):
    print("✅ Email válido")
else:
    print("❌ Email inválido")
