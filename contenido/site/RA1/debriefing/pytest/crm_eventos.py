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

