import os
import subprocess
import shutil
import csv
import stat
from datetime import datetime

# 📂 Carpeta principal donde se guardarán los repositorios.
# Recomendación: usa una carpeta FUERA de OneDrive para evitar bloqueos.
DESTINO = r"C:\repos_alumnos"
os.makedirs(DESTINO, exist_ok=True)

# 🧑‍💻 Lista de repositorios (Nombre carpeta alumno -> URL repo)
repos = {
    "Pol_Carbajal": "https://github.com/Peke2005/DAM-OPT-Python-AI-",
    "Abril_Palau": "https://github.com/AbrilPalauPardillos/MOPT2",
    "Angelo_Pozo": "https://github.com/angelopozo/python-projects",
    "Biel_Laguna": "https://github.com/Bielclon/Actividades-Pyton",
    "Cassius_Tedesco": "https://github.com/cassiuste/Python-RA1",
    "Diana_Canas": "https://github.com/Dianathecoder/Python_RA01",
    "Eric_Rodriguez": "https://github.com/EricRodriguezRojo/Practica-final.git",
    "Jean_Patrick_Esquivel": "https://github.com/Eskibal/MOPT2RA1_Practica_Python.git",
    "Jiahio_Liu": "https://github.com/LiuUexe/DAM2_RA1_Python",
    "Joan_Marc_Martinez_Motis_312572": "https://github.com/JoanMarcMM/RA1-IntroduccioPython-JoanMarc",
    "Joan_Ye": "https://github.com/Joan735/PythonRA1",
    "John_Henard_Salango_Fernande": "https://github.com/JohnHeSaFe/python-introduction.git",
    "Junxi_Xen": "https://github.com/Junxi-HM/Python_RA1",
    "Marc_Fernandez": "https://github.com/marcfg2002/MPOPTPLDAM2NLL2025_RA1",
    "Marc_Lopez": "https://github.com/MarcLopezMolina/DAM2_RA1-Practicas_python",
    "Marc_Muntane": "https://github.com/MarcMunta/Practicas",
    "Mario_Perez": "https://github.com/mario-perez30/MPOPT.Actividades",
    "Rodrigo_Mullisaca": "https://github.com/MoonRodri/PythonRA1",
    "Yixin_Huang": "https://github.com/kim-1111/python",
    "Ziril_Justin_Suarez": "https://github.com/zjsuarez/Pythonai-"
}

# 🧼 Eliminación robusta de carpetas con ficheros protegidos/bloqueados en Windows
def eliminar_carpeta_segura(path):
    """
    Intenta eliminar una carpeta completa, incluso si hay archivos
    marcados como solo lectura, bloqueados, etc.
    """
    def onerror(func, p, exc_info):
        # Quitar solo-lectura y reintentar
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except Exception:
            # si aun así falla, seguimos y ya avisaremos
            pass

    if os.path.exists(path):
        shutil.rmtree(path, onerror=onerror)


# 📝 Aquí guardaremos el resultado de cada repo para luego sacar el CSV
resultados = []

for alumno, repo_url in repos.items():
    print(f"\n=== Procesando {alumno} ===")

    carpeta_destino = os.path.join(DESTINO, alumno)

    # 1. Si la carpeta ya existe de ejecuciones anteriores, la borramos entera
    if os.path.exists(carpeta_destino):
        print(f"🗑️ Eliminando carpeta anterior: {carpeta_destino}")
        eliminar_carpeta_segura(carpeta_destino)

    # 2. Clonar el repo con profundidad 1 (solo último commit)
    try:
        print(f"⬇️ Clonando {repo_url} ...")
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, carpeta_destino],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"✅ Clonado en {carpeta_destino}")
        estado = "OK"
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al clonar {repo_url}: {e}")
        resultados.append({
            "Alumno": alumno,
            "URL": repo_url,
            "Estado": "ERROR"
        })
        # Pasamos al siguiente alumno
        continue

    # 3. Borrar la carpeta .git para que solo queden los ficheros del alumno
    git_dir = os.path.join(carpeta_destino, ".git")
    if os.path.exists(git_dir):
        print("🧹 Eliminando carpeta .git ...")
        try:
            eliminar_carpeta_segura(git_dir)
            print("   ✔ .git eliminada.")
        except Exception as e:
            print(f"   ⚠ No se pudo eliminar .git completamente: {e}")

    # 4. Guardar resultado OK
    resultados.append({
        "Alumno": alumno,
        "URL": repo_url,
        "Estado": estado
    })

# 5. Generar el CSV resumen
csv_filename = os.path.join(DESTINO, "informe_descargas.csv")

print(f"\n📝 Creando informe CSV: {csv_filename}")
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Alumno", "URL", "Estado", "Fecha"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for r in resultados:
        writer.writerow({
            "Alumno": r["Alumno"],
            "URL": r["URL"],
            "Estado": r["Estado"],
            "Fecha": fecha_actual
        })

print("\n🎉 Hecho.")
print(f"📂 Repos descargados en: {DESTINO}")
print(f"📄 Informe: {csv_filename}")
