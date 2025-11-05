# pytest_crm.md

## Instrucciones: Cómo usar Pytest en Visual Studio Code

1. **Instalar pytest**
   Abre la terminal en tu entorno de trabajo (por ejemplo, dentro de tu entorno virtual) y ejecuta:
   ```bash
   pip install pytest tabulate
   ```

2. **Estructura recomendada de carpetas**
   ```
   proyecto/
   ├── crm_eventos.py
   ├── test_crm.py
   └── ...
   ```

3. **Configurar Visual Studio Code**
   - Asegúrate de tener instalada la extensión **Python** de Microsoft.  
   - Abre la carpeta del proyecto (`proyecto/`) en VS Code.  
   - Presiona **Ctrl+Shift+P** (o **Cmd+Shift+P** en macOS) → busca `Python: Configure Tests`.  
   - Elige:
     - Framework: **pytest**
     - Carpeta raíz: la del proyecto  
   - VS Code detectará automáticamente los archivos de test (`test_*.py`).

4. **Ejecutar las pruebas**
   - Desde la terminal integrada:
     ```bash
     pytest -v
     ```
   - O directamente desde el panel de pruebas de VS Code (icono de tubo de ensayo en la barra lateral).  
   - Si quieres ver la tabla generada en la salida:
     ```bash
     pytest -s
     ```

---

## crm_eventos.py

*Contiene la función `validar_email`, que comprueba la validez de direcciones de correo electrónico mediante expresiones regulares. Rechaza direcciones con doble punto (`..`) y requiere un dominio con al menos un punto y un TLD de dos letras o más.*

```python
import csv
# Importar módulos necesarios para manejo de fechas y validaciones
from datetime import datetime, date
from typing import List, Dict, Set, Tuple
import os
import re

# ============================================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================================

def validar_email(email: str) -> bool:
    """
    Valida formato básico de email:
    - No permite '..' en ninguna parte
    - Requiere al menos un punto en el dominio
    - TLD de 2+ letras
    """
    patron = r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
    return re.match(patron, email) is not None
```

---

## test_crm.py

*Archivo de pruebas unitarias que valida la función `validar_email` usando `pytest`. Incluye una tabla de resultados generada con `tabulate` para visualizar qué correos pasan o fallan las pruebas.*

```python
import pytest
from crm_eventos import validar_email
from tabulate import tabulate

# Lista de casos (email, resultado esperado)
casos = [
    # Válidos
    ("usuario@example.com", True),
    ("nombre.apellido@dominio.es", True),
    ("user123@sub.dominio.org", True),
    ("a+b@dominio.co", True),

    # Inválidos
    ("usuarioexample.com", False),
    ("usuario@.com", False),
    ("usuario@dominio", False),
    ("usuario@@dominio.com", False),
    ("usuario@dominio..com", False),
    ("@dominio.com", False),
]

def test_email_valido():
    """Prueba directa de casos válidos."""
    assert validar_email("usuario@example.com") is True
    assert validar_email("nombre.apellido@dominio.es") is True
    assert validar_email("user123@sub.dominio.org") is True

@pytest.mark.parametrize("email, esperado", casos)
def test_validar_email(email, esperado):
    """Verifica la validación de emails mostrando resultados en tabla."""
    resultado = validar_email(email)
    assert resultado == esperado, f"Error en '{email}' (esperado {esperado}, obtenido {resultado})"

def test_mostrar_tabla():
    """Imprime una tabla con todos los casos y resultados."""
    filas = []
    for email, esperado in casos:
        resultado = validar_email(email)
        estado = "✅ OK" if resultado == esperado else "❌ ERROR"
        filas.append([email, esperado, resultado, estado])

    print("\n")
    print(tabulate(
        filas,
        headers=["Email", "Esperado", "Obtenido", "Estado"],
        tablefmt="grid"
    ))
```
