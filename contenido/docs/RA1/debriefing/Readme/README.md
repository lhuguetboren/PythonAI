# Mini-CRM de Eventos (OBLIGATORIO)

Aplicación de consola en **Python** para la gestión de **clientes**, **eventos** y **ventas**.  

## Funcionalidades principales (OBLIGATORIO)

- Menú de ejecución en bucle con opciones:
  1. Cargar datos desde CSV (`clientes.csv`, `eventos.csv`, `ventas.csv`)
  2. Listar tablas en consola
  3. Dar de alta nuevos clientes
  4. Filtrar ventas por rango de fechas
  5. Calcular estadísticas e indicadores
  6. Exportar informe resumen (`informe_resumen.csv`)
  7. Salir del programa

---

## Estructura del proyecto (OBLIGATORIO)

```
📂 Practica_Final/
 ├── data/
 │   ├── clientes.csv
 │   ├── eventos.csv
 │   ├── ventas.csv
 │   └── informe_resumen.csv
 ├── test_crm.py               # Tests con pytest (opcional)
 ├── README.md
 └── requirements.txt
```

---

## 🧩 Clases utilizadas (OBLIGATORIO)

### `Cliente`
- Atributos: `id_cliente`, `nombre`, `email`, `fecha_alta`
- Métodos:  
  - `antiguedad_dias()` → número de días desde el alta  
  - `__str__()` → representación legible del cliente

### `Evento`
- Atributos: `id_evento`, `titulo`, `fecha_evento`, `categoria`, `aforo`
- Métodos:  
  - `dias_hasta_evento()` → días restantes hasta el evento

### `Venta`
- Atributos: `id_venta`, `id_cliente`, `id_evento`, `precio`, `fecha_compra`  
- Métodos:  
  - `__str__()` → formato de salida legible para consola

---

## 🧮 Funciones y características clave (OBLIGATORIO)

| Función | Descripción |
|----------|--------------|
| `cargar_datos()` | Lee los CSV y genera las listas de clientes, eventos y ventas |
| `listar(tabla)` | Muestra el contenido de `clientes`, `eventos` o `ventas` |
| `alta_cliente()` | Añade un nuevo cliente con validaciones básicas |
| `filtrar_ventas_por_rango()` | Lista ventas entre dos fechas indicadas |
| `estadisticas()` | Calcula ingresos, categorías activas, y métricas de precios |
| `exportar_informe()` | Crea `informe_resumen.csv` con totales por evento |

---

## 📦 Requisitos (OBLIGATORIO)

- **Python ≥ 3.9**
- Librerías estándar (`csv`, `datetime`, `os`, `re`)
- (Opcional) `pytest` para pruebas automatizadas

Instalación recomendada:

```bash
python -m venv venv
source venv/bin/activate   # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt
```

---

## Ejecución

En consola, dentro de la carpeta del proyecto:

```bash
python gestor_CRM.py
```

El menú principal permitirá navegar entre las opciones.

---

## Pruebas (OPTATIVO)

Si se implementan tests con `pytest`, ejecutar:

```bash
pytest -v
```

Incluye ejemplo de validación de email (`test_crm.py`).

---

## Métricas generadas (OPTATIVO)

- **CSV de salida:** `data/informe_resumen.csv`
- **Datos calculados:**  
  - Ingresos totales  
  - Ingresos por evento  
  - Categorías activas  
  - Evento más próximo (días restantes)  
  - Tupla `(mínimo, máximo, media)` de precios de venta

---

## Entregables (OPTATIVO)

- Código fuente (`gestor_sin_dataclass.py`)  
- Carpeta `data/` con CSV de ejemplo  
- Archivo `informe_resumen.csv` generado  
- `README.md` actualizado  

## 📜 Licencia (OPTATIVO)

Proyecto académico desarrollado en Python para uso educativo.
