import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import json

# =========================================
# CONFIGURACIÓN
# =========================================
BASE_DIR = Path(__file__).resolve().parent

# Ruta al archivo resumen del curso
RUTA_RESUMEN = BASE_DIR /"resumen.md"

RUTA_INSTRUCCIONES = BASE_DIR /"instrucciones.md"
# Ruta al código oficial correcto que sirve como referencia
RUTA_SOLUCION = BASE_DIR /"gestor.py"

# Carpeta donde están TODOS los .py del alumno
CARPETA_ALUMNO = ""

# Modelo de OpenAI a usar
MODELO = "gpt-4.1-mini"  # razonamiento/análisis de código

# La clave debe estar en la variable de entorno OPENAI_API_KEY
#   export OPENAI_API_KEY="tu_clave"
# Cargar el archivo .env
load_dotenv()

# Crear el cliente usando la variable cargada
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# =========================================
# PROMPTS BASE
# =========================================

SYSTEM_PROMPT = """
Eres un revisor técnico del módulo de Python+IA del ciclo DAM/DAW.
Tu trabajo es detectar TODO el código que viola las restricciones del curso.

Reglas del curso:
- El único Python permitido es el descrito en 'resumen.md'.
- También está permitido exactamente el estilo y las funciones usadas en la SOLUCIÓN OFICIAL.
- Cualquier cosa en el código del alumno que no aparezca en resumen.md NI en la solución oficial es una violación.

Ejemplos de violaciones:
- imports no permitidos (os, re, typing...)
- uso de regex
- uso de lambda / sorted / sum / max / min / setdefault
- comprensiones de listas/dicts/sets
- generadores de id con max()
- clases que encapsula toda la lógica en vez de usar variables globales + funciones
- csv.writer con ';' en lugar de DictWriter con cabeceras
- rutas con os.path o path en lugar de lectura directa de ficheros
- etc.

INSTRUCCIONES DE SALIDA:
- Devuelve SOLO la lista numerada de violaciones (1., 2., 3., ...).
- Cada punto debe ser corto y directo.
- No añadas explicación previa ni resumen final.
- No añadas texto fuera de los puntos numerados.
"""


USER_PROMPT_TEMPLATE = """
[resumen.md]
{resumen}

[CODIGO_SOLUCION_OFICIAL]
{solucion}

[CODIGO_ALUMNO]
{codigo_alumno}

Analiza el CODIGO_ALUMNO.
Genera la lista numerada de violaciones respecto a RESUMEN.md y CODIGO_SOLUCION_OFICIAL.
No repitas bloques de código completos, solo describe la violación.
"""

SYSTEM_PROMPT2 = """
Eres un revisor técnico del módulo de Python+IA del ciclo DAM/DAW.
Tu trabajo es validar que las practicas funcionan correctamente, para ello simula la ejecucion e indica si cumple todos los requisitos.
"""

USER_PROMPT_TEMPLATE2 = """
[instrucciones.md]
{instrucciones}


[CODIGO_ALUMNO]
{codigo_alumno}

Analiza el CODIGO_ALUMNO y elabora un checklist de validación respecto a las INSTRUCCIONES.
"""


# =========================================
# FUNCIONES DE UTILIDAD
# =========================================

def leer_archivo_texto(ruta: str) -> str:
    """Lee un archivo de texto en UTF-8 y devuelve su contenido como string."""
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


from pathlib import Path

def obtener_carpetas_final(base_salidas: Path) -> dict[str, Path]:
    """
    Recorre todas las carpetas de alumnos dentro de 'base_salidas' y busca,
    dentro de cada una, la subcarpeta cuyo nombre contenga 'final'
    (sin importar mayúsculas o minúsculas).

    Devuelve un diccionario {nombre_alumno: ruta_carpeta_final}
    """
    carpetas_final = {}

    for alumno_dir in base_salidas.iterdir():
        if alumno_dir.is_dir():
            # Buscar recursivamente dentro del directorio del alumno
            for subcarpeta in alumno_dir.rglob("*"):
                if subcarpeta.is_dir() and "final" in subcarpeta.name.lower():
                    carpetas_final[alumno_dir.name] = subcarpeta.resolve()
                    break  # dejamos de buscar dentro de este alumno una vez encontrada
    return carpetas_final



def cargar_codigo_alumno(carpeta: str) -> str:
    """
    Lee todos los archivos .py del alumno dentro de `carpeta`
    y los concatena en un único string con separadores claros.

    Ejemplo de salida:
    ----- FICHERO: alumno/exercice_final.py -----
    <código...>

    ----- FICHERO: alumno/helpers.py -----
    <código...>
    """
    bloques = []

    # Recorremos todos los .py de la carpeta del alumno (orden alfabético para estabilidad)
    for nombre in sorted(os.listdir(carpeta)):
        if nombre.endswith(".py"):
            ruta = os.path.join(carpeta, nombre)
            with open(ruta, "r", encoding="utf-8") as f:
                codigo = f.read()
            bloque = (
                "----- FICHERO: " + ruta + " -----\n" +
                codigo +
                "\n"
            )
            bloques.append(bloque)

    if not bloques:
        raise RuntimeError(
            f"No se encontraron archivos .py en la carpeta '{carpeta}'. "
            "Asegúrate de poner ahí el código del alumno."
        )

    return "\n".join(bloques)


def construir_prompt_usuario(resumen: str, solucion: str, codigo_alumno: str) -> str:
    """Rellena la plantilla USER_PROMPT_TEMPLATE con los textos dados."""
    return USER_PROMPT_TEMPLATE.format(
        resumen=resumen,
        solucion=solucion,
        codigo_alumno=codigo_alumno
    )


def evaluar(resumen: str, solucion: str, codigo_alumno: str, modelo: str, prompt: str) -> str:
    """
    Envía todo al modelo de OpenAI y devuelve el texto resultado
    """
    prompt_usuario = construir_prompt_usuario(resumen, solucion, codigo_alumno)

    completion = client.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "system", "content": prompt.strip()},
            {"role": "user", "content": prompt_usuario.strip()},
        ]
    )

    respuesta = completion.choices[0].message.content.strip()
    return respuesta


# =========================================
# MAIN
# =========================================

def main():
    # 1. Cargar fuentes oficiales
    resumen_texto = leer_archivo_texto(RUTA_RESUMEN)
    solucion_texto = leer_archivo_texto(RUTA_SOLUCION)
    instrucciones_texto = leer_archivo_texto(RUTA_INSTRUCCIONES)




    # Ejemplo de uso:
    BASE_DIR = Path("./practicas").resolve()
    base_salidas = BASE_DIR / "RA1" / "salidas"
    resultado = {}
    carpetas = obtener_carpetas_final(base_salidas)

    for alumno, ruta in carpetas.items():
        #print(f"{alumno}: {ruta}")
        # 2. Unir todos los .py del alumno
        alumno_texto = cargar_codigo_alumno(ruta)

        # 3. Pasar todo al modelo
        hallazgos = evaluar(
            resumen=resumen_texto,
            solucion=solucion_texto,
            codigo_alumno=alumno_texto,
            modelo=MODELO, prompt=SYSTEM_PROMPT)
        
        validaciones = evaluar(
            resumen=instrucciones_texto,
            solucion=solucion_texto,
            codigo_alumno=alumno_texto,
            modelo=MODELO, prompt=SYSTEM_PROMPT2)
        
       
        resultado[alumno] = {
            'hallazgos': hallazgos,
            'validaciones': validaciones
            }
        
        
    with open("practicas/RA1/PF_alumno.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    main()
