from pathlib import Path
import shutil

# --- Configuración de rutas con Path ---
BASE_DIR: Path = Path(__file__).resolve().parent          # carpeta actual (src)
DATA_DIR: Path = (BASE_DIR / ".." / "data").resolve()     # sube una carpeta y entra en "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)               # crea la carpeta si no existe

# Rutas a los archivos CSV
CLIENTES_CSV: Path = DATA_DIR / "clientes.csv"
EVENTOS_CSV: Path  = DATA_DIR / "eventos.csv"
VENTAS_CSV: Path   = DATA_DIR / "ventas.csv"
INFORME_CSV: Path  = DATA_DIR / "informe_resumen.csv"


"""
Ejemplos básicos con la librería shutil y pathlib.Path.
"""
backup_dir = DATA_DIR / "backup"
backup_dir.mkdir(exist_ok=True)

# Copiar un archivo
if CLIENTES_CSV.exists():
    destino = backup_dir / CLIENTES_CSV.name
    shutil.copy(CLIENTES_CSV, destino)
    print(f"Archivo copiado a: {destino}")

# Copiar una carpeta completa (recursiva)
carpeta_origen = DATA_DIR
carpeta_destino = BASE_DIR / "data_copia"
if carpeta_destino.exists():
    shutil.rmtree(carpeta_destino)  # elimina si ya existe

shutil.copytree(carpeta_origen, carpeta_destino)
print(f"Carpeta copiada a: {carpeta_destino}")
