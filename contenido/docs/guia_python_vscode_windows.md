# Guía rápida: Python + VS Code en Windows

## 1. Instalar Python en Windows

1. Descarga el instalador desde [python.org > Downloads > Windows](https://www.python.org/downloads/windows/).
2. Ejecuta el instalador y marca **“Add python.exe to PATH”**, luego pulsa **Install Now**.
3. Verifica en una terminal (PowerShell o CMD):

   ```powershell
   python --version
   py --version
   ```

> Si PowerShell bloquea la activación de entornos virtuales:

> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

---

## 2. Visual Studio Code + extensiones necesarias + modulos

Instala VS Code y añade estas extensiones:

- **Python** – *ms-python.python*
- **Pylance** – *ms-python.vscode-pylance*
- **Jupyter** – *ms-toolsai.jupyter* (si usarás notebooks)

Para utilizar Jupyter es necesario instalar también

```bash
pip install ipykernel
```


## 3. Crear y usar un entorno virtual (venv)

En la carpeta del proyecto:

**Crear**

```powershell
py -m venv .venv
```

*py o python dependiendo como hayas instalado el ejecutable

**Activar**

```powershell
# PowerShell
. .\.venv\Scripts\Activate.ps1
```

```bat
:: CMD clásico
.\.venv\Scripts\activate.bat
```

> Verás `(.venv)` al inicio de la línea en la terminal cuando esté activo.

**Usar en VS Code**

Habitualmente VS Code detecta el env, sino es así proceder de la siguiente forma:

- Abre tu carpeta de proyecto.
- `Ctrl+Shift+P` → **Python: Select Interpreter** → (elige el de tu venv cuando lo tengas).

Si quieres que este entorno se inicie siempre al abrir el proyecto edita o crea en el directorio .vscode/settgins.json con lo siguiente

```json
{
    "python-envs.pythonProjects": [],
    "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"
}```


### Instalar paquetes y guardar dependencias

```powershell
pip install requests
pip freeze > requirements.txt
```

Para restaurar en otra máquina:

```powershell
pip install -r requirements.txt
```

---

## 4. Ajustes básicos recomendados en VS Code

En `settings.json`:

```json
{
  "python.testing.pytestEnabled": true,
  "python.analysis.typeCheckingMode": "basic",
  "python.defaultInterpreterPath": ".venv/Scripts/python.exe",
  "editor.formatOnSave": true
}
```

---

## 5. Consejos rápidos

- Añade `.venv/` a tu **.gitignore**.
- Usa un venv **por proyecto** para evitar choques de versiones.
- En notebooks, selecciona el **kernel** correspondiente al venv (barra superior del `.ipynb`).
