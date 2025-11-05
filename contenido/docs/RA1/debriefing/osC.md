# osC.md

*Utilidades para trabajar con el sistema de archivos usando `os`: define rutas base y de datos, crea un CSV de ejemplo si no existe y ofrece funciones para copiar archivos y carpetas, mover y eliminar recursivamente. Incluye un bloque `__main__` con ejemplo de uso (backup, copia de carpeta, mover archivo y limpieza).*

```python
import os

# --- Configuración de rutas ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

CLIENTES_CSV = os.path.join(DATA_DIR, "clientes.csv")

# --- Crear un archivo de ejemplo ---
if not os.path.exists(CLIENTES_CSV):
    with open(CLIENTES_CSV, "w", encoding="utf-8") as f:
        f.write("id,nombre,email\n1,Ana,ana@example.com\n")
    print(f"Archivo creado: {CLIENTES_CSV}")


# --- Funciones auxiliares ---
def copiar_archivo(origen: str, destino: str):
    """Copia un archivo binario usando solo os."""
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(origen, "rb") as fsrc, open(destino, "wb") as fdst:
        fdst.write(fsrc.read())
    print(f"Archivo copiado de {origen} → {destino}")


def copiar_carpeta(origen: str, destino: str):
    """Copia recursivamente una carpeta usando os.walk."""
    for raiz, dirs, archivos in os.walk(origen):
        rel_path = os.path.relpath(raiz, origen)
        dest_dir = os.path.join(destino, rel_path)
        os.makedirs(dest_dir, exist_ok=True)
        for archivo in archivos:
            src = os.path.join(raiz, archivo)
            dst = os.path.join(dest_dir, archivo)
            copiar_archivo(src, dst)
    print(f"Carpeta copiada de {origen} → {destino}")


def mover_archivo(origen: str, destino: str):
    """Mueve o renombra un archivo usando os.rename."""
    os.rename(origen, destino)
    print(f"Archivo movido de {origen} → {destino}")


def eliminar_carpeta(carpeta: str):
    """Elimina recursivamente una carpeta"""
    for raiz, dirs, archivos in os.walk(carpeta, topdown=False):
        for archivo in archivos:
            os.remove(os.path.join(raiz, archivo))
        for d in dirs:
            os.rmdir(os.path.join(raiz, d))
    if os.path.exists(carpeta):
        os.rmdir(carpeta)
    print(f"Carpeta eliminada: {carpeta}")


# --- Ejemplo de ejecución ---
if __name__ == "__main__":
    # Copiar archivo
    backup_dir = os.path.join(DATA_DIR, "backup")
    os.makedirs(backup_dir, exist_ok=True)
    destino_archivo = os.path.join(backup_dir, "clientes_backup.csv")
    copiar_archivo(CLIENTES_CSV, destino_archivo)

    # Copiar carpeta completa
    copia_dir = os.path.join(BASE_DIR, "data_copia")
    if os.path.exists(copia_dir):
        eliminar_carpeta(copia_dir)
    copiar_carpeta(DATA_DIR, copia_dir)

    # Mover archivo
    archivo_movido = os.path.join(DATA_DIR, "clientes_moved.csv")
    if os.path.exists(CLIENTES_CSV):
        mover_archivo(CLIENTES_CSV, archivo_movido)

    # Eliminar carpeta completa
    if os.path.exists(copia_dir):
        eliminar_carpeta(copia_dir)
```
