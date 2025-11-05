# mini_crm_starter.py
"""
Mini-CRM de eventos
- Lee y guarda CSV
- Gestiona clientes, eventos y ventas
- Hace cálculos de métricas con fechas (datetime.date)
- Usa colecciones (list, dict, set)
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
# mini_crm_starter.py
"""
Mini-CRM de eventos
- Lee y guarda CSV
- Gestiona clientes, eventos y ventas
- Hace cálculos de métricas con fechas (datetime.date)
- Usa colecciones (list, dict, set)
"""

from __future__ import annotations
from datetime import datetime, date
from pathlib import Path
import csv

# --- Constantes ---
DATA_DIR = Path("data")
FMT = "%Y-%m-%d"
HOY: date = date.today()

# --- Colecciones ---
clientes = []
eventos = []
ventas = []
clientes_by_id = {}
eventos_by_id = {}
categorias = set()

# --- Modelos ---
class Cliente:
    def __init__(self, id_cliente: str, nombre: str, email: str, fecha_alta: date):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.fecha_alta = fecha_alta

    def antiguedad_dias(self) -> int:
        diff = HOY - self.fecha_alta
        return diff.days

    def __str__(self) -> str:
        return (
            f"Cliente {self.id_cliente} | {self.nombre} <{self.email}> | alta "
            f"{self.fecha_alta.strftime(FMT)} | {self.antiguedad_dias()} días"
        )

    __repr__ = __str__


class Evento:
    def __init__(self, id_evento: str, titulo: str, fecha_evento: date, categoria: str, aforo: int):
        self.id_evento = id_evento
        self.titulo = titulo
        self.fecha_evento = fecha_evento
        self.categoria = categoria
        self.aforo = aforo

    def dias_hasta_evento(self) -> int:
        diff = self.fecha_evento - HOY
        return diff.days

    def __str__(self) -> str:
        return (
            f"Evento {self.id_evento} | {self.titulo} | {self.fecha_evento.strftime(FMT)} "
            f"({self.categoria}) | aforo {self.aforo} | {self.dias_hasta_evento()} días"
        )

    __repr__ = __str__


class Venta:
    def __init__(self, id_venta: str, id_cliente: str, id_evento: str, precio: float, fecha_compra: date):
        self.id_venta = id_venta
        self.id_cliente = id_cliente
        self.id_evento = id_evento
        self.precio = precio
        self.fecha_compra = fecha_compra

    def __str__(self) -> str:
        return (
            f"Venta {self.id_venta} | cli={self.id_cliente} evt={self.id_evento} | "
            f"{self.precio}€ | {self.fecha_compra.strftime(FMT)}"
        )

    __repr__ = __str__



# --- Utilidades CSV ---
def leer_csv(path: Path) -> list[dict]:
    """Lee un CSV y devuelve una lista de dict."""
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def guardar_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    """Guarda lista de dict en CSV (sobrescribe el archivo)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


# --- Helpers internos de negocio ---

def _generar_nuevo_id_cliente() -> str:
    """
    Genera un id_cliente simple tipo C### que no exista.
    No usamos max(), recorremos manualmente.
    """
    # buscamos el número más alto actual
    mas_alto = 0
    for cid in clientes_by_id.keys():
        # ids esperados "C123"
        if cid.startswith("C"):
            parte_num = cid[1:]
            try:
                n = int(parte_num)
            except ValueError:
                continue
            if n > mas_alto:
                mas_alto = n
    nuevo_num = mas_alto + 1
    return "C" + str(nuevo_num)


def _validar_email(email: str) -> bool:
    """
    Validación MUY simple:
    - que contenga '@'
    - que contenga '.'
    - y que '@' vaya antes que el último '.'
    """
    if "@" not in email:
        return False
    if "." not in email:
        return False
    pos_arroba = -1
    pos_punto = -1
    idx = 0
    for ch in email:
        if ch == "@":
            pos_arroba = idx
        if ch == ".":
            pos_punto = idx
        idx = idx + 1
    if pos_arroba == -1 or pos_punto == -1:
        return False
    # el punto debe venir después de la arroba
    return pos_arroba < pos_punto


def _pedir_fecha(mensaje: str) -> date | None:
    """
    Pide una fecha YYYY-MM-DD por input() y la convierte a date.
    Devuelve None si el formato no es válido.
    """
    txt = input(mensaje).strip()
    try:
        return datetime.strptime(txt, FMT).date()
    except ValueError:
        print("⚠ Formato de fecha inválido, usa YYYY-MM-DD")
        return None


# --- Carga de datos ---
def cargar_datos() -> None:
    """Carga clientes, eventos y ventas desde CSV a memoria."""
    global clientes, eventos, ventas, clientes_by_id, eventos_by_id, categorias

    try:
        raw = leer_csv(DATA_DIR / "clientes.csv")
        clientes_local = []
        for r in raw:
            c = Cliente(
                id_cliente=r["id_cliente"].strip(),
                nombre=r["nombre"].strip(),
                email=r["email"].strip(),
                fecha_alta=datetime.strptime(r["fecha_alta"], FMT).date(),
            )
            clientes_local.append(c)
        clientes = clientes_local
        # índice auxiliar
        clientes_by_id = {}
        for c in clientes:
            clientes_by_id[c.id_cliente] = c
    except FileNotFoundError:
        print("⚠ No se encontró data/clientes.csv")

    try:
        raw = leer_csv(DATA_DIR / "eventos.csv")
        eventos_local = []
        for r in raw:
            e = Evento(
                id_evento=r["id_evento"].strip(),
                titulo=r["titulo"].strip(),
                fecha_evento=datetime.strptime(r["fecha_evento"], FMT).date(),
                categoria=r["categoria"].strip(),
                aforo=int(r["aforo"]),
            )
            eventos_local.append(e)
        eventos = eventos_local

        eventos_by_id = {}
        for e in eventos:
            eventos_by_id[e.id_evento] = e

        # set de categorías únicas
        cat_local = set()
        for e in eventos:
            cat_local.add(e.categoria)
        categorias = cat_local
    except FileNotFoundError:
        print("⚠ No se encontró data/eventos.csv")

    try:
        raw = leer_csv(DATA_DIR / "ventas.csv")
        ventas_local = []
        for r in raw:
            v = Venta(
                id_venta=r["id_venta"].strip(),
                id_cliente=r["id_cliente"].strip(),
                id_evento=r["id_evento"].strip(),
                precio=float(r["precio"]),
                fecha_compra=datetime.strptime(r["fecha_compra"], FMT).date(),
            )
            ventas_local.append(v)
        ventas = ventas_local
    except FileNotFoundError:
        print("⚠ No se encontró data/ventas.csv")

    # Este print ya estaba en el starter (usa len(), lo dejamos)
    print(
        "✔ Cargados "
        + str(len(clientes))
        + " clientes, "
        + str(len(eventos))
        + " eventos, "
        + str(len(ventas))
        + " ventas."
    )


# --- Listados ---
def listar(tabla: str) -> None:
    """Muestra en consola clientes, eventos o ventas formateados."""
    if tabla == "clientes":
        for c in clientes:
            print(c)

    elif tabla == "eventos":
        for e in eventos:
            print(e)

    elif tabla == "ventas":
        for v in ventas:
            # enriquecer un poco con nombre cliente / titulo evento si existen
            cli = clientes_by_id.get(v.id_cliente, None)
            evt = eventos_by_id.get(v.id_evento, None)

            nombre_cli = cli.nombre if cli is not None else "?"
            titulo_evt = evt.titulo if evt is not None else "?"

            print(
                v.id_venta
                + " | "
                + v.fecha_compra.strftime(FMT)
                + " | "
                + nombre_cli
                + " -> "
                + titulo_evt
                + " | "
                + str(v.precio)
                + "€"
            )
    else:
        print("Tabla no reconocida.")


# --- Operaciones de negocio ---
def alta_cliente() -> None:
    """
    Alta mínima de cliente:
    - pedir nombre, email, fecha_alta
    - validar email
    - validar fecha
    - generar id único
    - guardar en memoria y re-escribir clientes.csv
    """
    print("\n=== Alta de cliente ===")

    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()

    if not _validar_email(email):
        print("⚠ Email no válido.")
        return

    # pedir fecha hasta que sea válida
    fecha_ok = None
    while fecha_ok is None:
        fecha_ok = _pedir_fecha("Fecha de alta (YYYY-MM-DD): ")
        if fecha_ok is None:
            # si no es válida, repetimos
            pass

    # generar id que no choque
    nuevo_id = _generar_nuevo_id_cliente()
    if nuevo_id in clientes_by_id:
        # extremadamente raro, pero por seguridad generamos otro
        # (sin raise, usamos bucle)
        while nuevo_id in clientes_by_id:
            nuevo_id = _generar_nuevo_id_cliente()

    # crear objeto e incorporarlo a las colecciones
    nuevo_cliente = Cliente(
        id_cliente=nuevo_id,
        nombre=nombre,
        email=email,
        fecha_alta=fecha_ok,
    )
    clientes.append(nuevo_cliente)
    clientes_by_id[nuevo_cliente.id_cliente] = nuevo_cliente

    # persistir CSV completo sobrescribiendo
    rows = []
    for c in clientes:
        rows.append(
            {
                "id_cliente": c.id_cliente,
                "nombre": c.nombre,
                "email": c.email,
                "fecha_alta": c.fecha_alta.strftime(FMT),
            }
        )

    guardar_csv(
        DATA_DIR / "clientes.csv",
        rows,
        fieldnames=["id_cliente", "nombre", "email", "fecha_alta"],
    )

    print("✔ Cliente dado de alta con id " + nuevo_cliente.id_cliente)


def filtrar_ventas_por_rango() -> list[Venta]:
    """
    Pide dos fechas YYYY-MM-DD (inicio y fin), ambas incluidas.
    Muestra en pantalla las ventas dentro del rango y devuelve la lista.
    """
    print("\n=== Filtro de ventas por rango de fechas ===")

    fecha_inicio = None
    while fecha_inicio is None:
        fecha_inicio = _pedir_fecha("Fecha inicio (YYYY-MM-DD): ")
        if fecha_inicio is None:
            pass

    fecha_fin = None
    while fecha_fin is None:
        fecha_fin = _pedir_fecha("Fecha fin (YYYY-MM-DD): ")
        if fecha_fin is None:
            pass

    # asegurarnos de que inicio <= fin
    if fecha_inicio > fecha_fin:
        print("⚠ Rango inconsistente, inicio es posterior al fin.")
        return []

    encontradas = []

    # recorremos ventas y filtramos manualmente
    for v in ventas:
        if v.fecha_compra >= fecha_inicio and v.fecha_compra <= fecha_fin:
            encontradas.append(v)

    # Mostrar resultado
    print(
        "Ventas entre "
        + fecha_inicio.strftime(FMT)
        + " y "
        + fecha_fin.strftime(FMT)
        + ":"
    )
    for v in encontradas:
        cli = clientes_by_id.get(v.id_cliente, None)
        evt = eventos_by_id.get(v.id_evento, None)

        nombre_cli = cli.nombre if cli is not None else "?"
        titulo_evt = evt.titulo if evt is not None else "?"

        print(
            v.id_venta
            + " | "
            + v.fecha_compra.strftime(FMT)
            + " | "
            + nombre_cli
            + " -> "
            + titulo_evt
            + " | "
            + str(v.precio)
            + "€"
        )

    print("Total coincidencias: " + str(len(encontradas)))
    return encontradas


def estadisticas() -> None:
    """
    Muestra métricas básicas:
    - ingresos totales
    - ingresos por evento
    - set de categorías
    - días hasta el evento más próximo (>= HOY)
    - tupla (min, max, media) de precios de venta
    """
    print("\n=== Métricas ===")

    # ingresos totales y por evento (sin sum() automático)
    total_ingresos = 0.0
    ingresos_por_evento = {}  # id_evento -> total float
    contador_ventas = 0

    # también recopilamos lista de precios para min/max/media
    precio_min = None
    precio_max = None

    for v in ventas:
        total_ingresos = total_ingresos + v.precio
        contador_ventas = contador_ventas + 1

        # min / max manuales
        if precio_min is None or v.precio < precio_min:
            precio_min = v.precio
        if precio_max is None or v.precio > precio_max:
            precio_max = v.precio

        # agrupar por evento
        actual = ingresos_por_evento.get(v.id_evento, 0.0)
        ingresos_por_evento[v.id_evento] = actual + v.precio

    # media manual (evitamos usar sum() / len() si quisiéramos ser estrictos,
    # pero aquí ya hemos recorrido y tenemos total_ingresos y contador_ventas)
    if contador_ventas > 0:
        media_precios = total_ingresos / contador_ventas
    else:
        media_precios = 0.0

    # categorías existentes ya las tenemos en el set global `categorias`
    # Mostramos categorías como una lista formateada
    txt_categorias = ""
    primera = True
    for cat in categorias:
        if primera:
            txt_categorias = cat
            primera = False
        else:
            txt_categorias = txt_categorias + ", " + cat

    # evento más próximo (días >= 0 más pequeño)
    dias_evento_mas_proximo = None
    evento_cercano = None
    for e in eventos:
        diff = e.dias_hasta_evento()
        if diff >= 0:
            if dias_evento_mas_proximo is None or diff < dias_evento_mas_proximo:
                dias_evento_mas_proximo = diff
                evento_cercano = e

    # salida
    print("Ingresos totales: " + str(total_ingresos) + " €")

    print("Ingresos por evento:")
    for idevt, total_evt in ingresos_por_evento.items():
        evt = eventos_by_id.get(idevt, None)
        titulo_evt = evt.titulo if evt is not None else "?"
        print("  - " + idevt + " (" + titulo_evt + "): " + str(total_evt) + " €")

    print("Categorías activas: " + txt_categorias)

    if evento_cercano is not None and dias_evento_mas_proximo is not None:
        print(
            "Próximo evento: "
            + evento_cercano.titulo
            + " en "
            + str(dias_evento_mas_proximo)
            + " días"
        )
    else:
        print("No hay eventos futuros registrados.")

    # tupla (min, max, media)
    print(
        "Precios venta (min, max, media): ("
        + str(precio_min)
        + ", "
        + str(precio_max)
        + ", "
        + str(media_precios)
        + ")"
    )


def exportar_informe() -> None:
    """
    Genera data/informe_resumen.csv con totales por evento.
    Columnas:
    id_evento, titulo, num_ventas, total_ingresos
    """
    print("\n=== Exportar informe ===")

    # acumulamos info por evento
    resumen = {}  # id_evento -> dict con contador y suma
    for v in ventas:
        if v.id_evento not in resumen:
            resumen[v.id_evento] = {
                "num_ventas": 0,
                "total_ingresos": 0.0,
            }
        datos_evt = resumen[v.id_evento]
        datos_evt["num_ventas"] = datos_evt["num_ventas"] + 1
        datos_evt["total_ingresos"] = datos_evt["total_ingresos"] + v.precio

    # convertir a filas para CSV final
    rows_out = []

    for idevt, info_evt in resumen.items():
        evt = eventos_by_id.get(idevt, None)
        titulo_evt = evt.titulo if evt is not None else "?"
        rows_out.append(
            {
                "id_evento": idevt,
                "titulo": titulo_evt,
                "num_ventas": str(info_evt["num_ventas"]),
                "total_ingresos": str(info_evt["total_ingresos"]),
            }
        )

    out_path = DATA_DIR / "informe_resumen.csv"
    guardar_csv(
        out_path,
        rows_out,
        fieldnames=["id_evento", "titulo", "num_ventas", "total_ingresos"],
    )

    print("✔ Informe generado en " + str(out_path))


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
        print("\n=== Mini-CRM de eventos ===")
        for k, (txt, _) in opciones.items():
            print(k + ") " + txt)
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
            seguro = input("¿Seguro? (s/n): ").strip().lower()
            if seguro == "s":
                print("¡Hasta pronto!")
                break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
