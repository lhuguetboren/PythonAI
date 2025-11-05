# mini_crm_starter.py
"""
Starter simplificado — Mini-CRM de eventos
Incluye: menú, lectura de CSV, clases vacías, colecciones y uso de datetime.
Rellena los TODO marcados en este archivo y en TODO.md.
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date
from pathlib import Path
import csv

# --- Constantes ---
DATA_DIR = Path("data")
FMT = "%Y-%m-%d"  # formato fecha
HOY: date = date.today()

# --- Colecciones en memoria ---
clientes = []          # list[Cliente]
eventos = []           # list[Evento]
ventas = []            # list[Venta]
clientes_by_id = {}    # dict[str, Cliente]
eventos_by_id = {}     # dict[str, Evento]
categorias = set()     # set[str]

# --- Modelos (POO) ---
@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    email: str
    fecha_alta: date
    # TODO: def antiguedad_dias(self) -> int: ...
    # TODO: __str__/__repr__ para salidas legibles

@dataclass
class Evento:
    id_evento: str
    titulo: str
    fecha_evento: date
    categoria: str
    aforo: int
    # TODO: def dias_hasta_evento(self) -> int: ...

@dataclass
class Venta:
    id_venta: str
    id_cliente: str
    id_evento: str
    precio: float
    fecha_compra: date

# --- Utilidades CSV ---
def leer_csv(path: Path) -> list[dict]:
    """Lee un CSV y devuelve una lista de dict."""
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def guardar_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    """Guarda lista de dict en CSV (sobrescribe)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

# --- Carga de datos ---
def cargar_datos() -> None:
    """Carga clientes, eventos y ventas desde CSV."""
    global clientes, eventos, ventas, clientes_by_id, eventos_by_id, categorias

    try:
        raw = leer_csv(DATA_DIR / "clientes.csv")
        clientes = [
            Cliente(
                id_cliente=r["id_cliente"].strip(),
                nombre=r["nombre"].strip(),
                email=r["email"].strip(),
                fecha_alta=datetime.strptime(r["fecha_alta"], FMT).date(),
            ) for r in raw
        ]
        clientes_by_id = {c.id_cliente: c for c in clientes}
    except FileNotFoundError:
        print("⚠ No se encontró data/clientes.csv")

    try:
        raw = leer_csv(DATA_DIR / "eventos.csv")
        eventos = [
            Evento(
                id_evento=r["id_evento"].strip(),
                titulo=r["titulo"].strip(),
                fecha_evento=datetime.strptime(r["fecha_evento"], FMT).date(),
                categoria=r["categoria"].strip(),
                aforo=int(r["aforo"]),
            ) for r in raw
        ]
        eventos_by_id = {e.id_evento: e for e in eventos}
        categorias = {e.categoria for e in eventos}
    except FileNotFoundError:
        print("⚠ No se encontró data/eventos.csv")

    try:
        raw = leer_csv(DATA_DIR / "ventas.csv")
        ventas = [
            Venta(
                id_venta=r["id_venta"].strip(),
                id_cliente=r["id_cliente"].strip(),
                id_evento=r["id_evento"].strip(),
                precio=float(r["precio"]),
                fecha_compra=datetime.strptime(r["fecha_compra"], FMT).date(),
            ) for r in raw
        ]
    except FileNotFoundError:
        print("⚠ No se encontró data/ventas.csv")

    print(f"✔ Cargados {len(clientes)} clientes, {len(eventos)} eventos, {len(ventas)} ventas.")

# --- Listados (placeholders) ---
def listar(tabla: str) -> None:
    if tabla == "clientes":
        for c in clientes:
            print(c)  # TODO: formatear salida
    elif tabla == "eventos":
        for e in eventos:
            print(e)  # TODO: incluir días hasta el evento
    elif tabla == "ventas":
        for v in ventas:
            print(v)
    else:
        print("Tabla no reconocida.")

# --- Operaciones (placeholders) ---
def alta_cliente() -> None:
    """Alta mínima de cliente (I/O y validaciones)."""
    # TODO: pedir datos, validar email/fecha, actualizar colecciones y guardar incrementalmente
    pass

def filtrar_ventas_por_rango() -> list[Venta]:
    """Filtra ventas entre dos fechas (YYYY-MM-DD)."""
    # TODO: leer dos fechas con input, validar con datetime.strptime, filtrar
    return []

def estadisticas() -> None:
    """Muestra métricas básicas (ingresos totales, por evento, categorías, evento más próximo...)."""
    # TODO: implementar sumatorios, agrupaciones y cálculos de fechas
    pass

def exportar_informe() -> None:
    """Genera informe CSV (resumen por evento)."""
    # TODO: acumular totales por id_evento y escribir data/informe_resumen.csv
    pass

# --- Menú principal ---
def menu() -> None:
    opciones = {
        "1": ("Cargar CSV", cargar_datos),
        "2": ("Listar (clientes/eventos/ventas)", None),
        "3": ("Alta de cliente", alta_cliente),
        "4": ("Filtrar ventas por rango de fechas", filtrar_ventas_por_rango),
        "5": ("Métricas", estadisticas),
        "6": ("Exportar informe CSV", exportar_informe),
        "0": ("Salir", None),
    }
    while True:
        print("\n=== Mini-CRM de eventos (Starter) ===")
        for k, (txt, _) in opciones.items():
            print(f"{k}) {txt}")
        op = input("> Elige opción: ").strip()

        if op == "1":
            cargar_datos()
        elif op == "2":
            cual = input("¿Qué listar? (clientes/eventos/ventas): ").strip().lower()
            listar(cual)
        elif op == "3":
            alta_cliente()
        elif op == "4":
            filtrar_ventas_por_rango()
        elif op == "5":
            estadisticas()
        elif op == "6":
            exportar_informe()
        elif op == "0":
            if input("¿Seguro? (s/n): ").strip().lower() == "s":
                print("¡Hasta pronto!")
                break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
