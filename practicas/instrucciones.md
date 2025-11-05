# Práctica final: Mini-CRM de eventos (con CSV, clases y datetime)

## Objetivo

Desarrollar una aplicación de consola en Python que gestione **clientes**, **eventos** y **ventas** a partir de ficheros CSV. La app debe:

- Incluir un **menú de ejecución** en bucle.
- Leer y escribir **CSV** (módulo `csv`).
- Usar **tipos de datos** básicos (str, int, float, bool) y **colecciones** (list, dict, set, tuple).
- Definir **al menos una clase** propia (recomendadas: `Cliente`, `Evento`, `Venta`).
- Utilizar **`datetime`** para parsear fechas y calcular rangos/diferencias.

## Requisitos funcionales mínimos

1. **Menú** con opciones: cargar CSV, listar tablas, alta de cliente, filtro de ventas por rango de fechas, métricas, exportar informe, salir.
2. **CSV**: `clientes.csv`, `eventos.csv`, `ventas.csv` (ver formato en starter).
3. **POO**: implementar clases y métodos de utilidad (p. ej., `dias_hasta_evento()`).
4. **Fechas**: parsear fechas con `datetime.strptime`, calcular diferencias con `date.today()`.
5. **Colecciones**: listas para tablas, diccionarios índice por id, set de categorías, tuplas para devolver resúmenes.
6. **Gestión de archivos**: lectura robusta, guardado incremental y exportación de informe CSV.

## TODO

### Mínimos (obligatorios)

- [ ] Implementar `cargar_datos()` para leer `clientes.csv`, `eventos.csv`, `ventas.csv`.
- [ ] Completar `listar(tabla)` con salidas formateadas.
- [ ] `alta_cliente()`: pedir datos por `input`, validar fecha (YYYY-MM-DD), actualizar colecciones y guardar incrementalmente `data/clientes.csv`.
- [ ] `filtrar_ventas_por_rango()`: leer dos fechas, validar, devolver/imprimir ventas entre el rango.
- [ ] `estadisticas()`: 
  - [ ] ingresos totales
  - [ ] ingresos por evento (dict)
  - [ ] set de categorías existentes
  - [ ] días hasta el evento más próximo
  - [ ] tupla (min, max, media) de precios
- [ ] `exportar_informe()`: crear `data/informe_resumen.csv` con totales por evento.