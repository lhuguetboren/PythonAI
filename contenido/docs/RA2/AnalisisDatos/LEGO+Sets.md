# Análisis de datos con pandas y NumPy

**Dataset**: catàleg de sets de LEGO  
> Variables: `set_id`, `name`, `year`, `theme`, `subtheme`, `themeGroup`, `category`, `pieces`, `minifigs`, `agerange_min`, `US_retailPrice`, `bricksetURL`, `thumbnailURL`, `imageURL`

---

## 1. Imports & configuració

Importacion de librerias

---

## 2. Càrrega de dades

- Carrega el fitxer CSV.  
- Mostra les primeres files, utilitza `df.info()`, `df.describe()` per entendre variables numèriques/com a text.  
- Observa la distribució temporal (anys), els valors que falten (per exemple `US_retailPrice`, `minifigs`).

---

## 3. Neteja i preparació de dades

- Assegura’t que `year`, `pieces`, `minifigs`, `agerange_min`, `US_retailPrice` estan en tipus numèric correcte.  
- Tracta possibles valors nuls o buits (per exemple `US_retailPrice` buit, `minifigs` buit). Decideix eliminar-o imputar-los.  
- Comprova duplicates pel `set_id`.  
- Potser crea columna nova: per exemple ‘densitat de peces’ = `pieces / agerange_min` (o alguna altra relació entre propietats).  
- Converteix variables categòriques (`theme`, `category`, `themeGroup`) en tipus «category» per a analitzar agrupacions.

---

## 4. Anàlisi exploratori

### 4.1 Estadístiques globals

- Nombre total de sets.  
- Estadístiques de `pieces`, `minifigs`, `US_retailPrice`: mitjana, mediana, mínim, màxim.  
- Quants sets tenen preu (US_retailPrice) informats vs quants no.  
- Quants anys estan coberts (minim any, maxim any, quants per any).

### 4.2 Distribució per tema/categoria

- Agrupa per `theme` i calcula:  
  - nombre de sets  
  - nombre mitjà de peces  
  - preu mitjà (quan està disponible)  
- Ordena de més a menys per nombre de sets o per preu mitjà.  
- Observa si certs temes tendeixen a tenir més peces o més preu.

### 4.3 Relació entre peces, minifigs, preu

- Examina la relació entre nombre de peces (`pieces`) i preu (`US_retailPrice`) (per ex: scatter plot si vols).  
- Agrupa per rangs de peces (per exemple <100, 100-300, >300) i calcula preu mitjà en cada rang.  
- Utilitza NumPy per calcular percentils de `pieces` i `preu`.

### 4.4 Anàlisi temporal

- Analitza l’evolució dels sets segons l’any `year`: nombre de sets per any, preu mitjà per any, peces mitjanes per any.  
- Observa si cal detectar tendències: els sets dels anys més recents tenen més peces / preu més alt?

---

## 5. Ús de NumPy per anàlisi auxiliar

- Calcula percentils (25th, 50th, 75th, 95th) per `pieces`, `US_retailPrice` utilitzant `np.percentile`.  
- Crea arrays amb NumPy per fer operacions vectoritzades sobre `pieces` o `preu`, per exemple calcular log(preu) o relacions.  
- Potser utilitza `np.histogram` per veure distribució de `pieces` o `preu`.

---

## 6. Preguntes

1. Quin tema (`theme`) té el major nombre de sets? I quin té menys?  
2. Quin és el percentil 95 del nombre de peces (`pieces`)? Quants sets superen aquest valor?  
3. Quin és el preu mitjà dels sets per rang de peces (per exemple <100 peces, 100-300, >300)?  
4. Com ha evolucionat el preu mitjà i el nombre mitjà de peces dels sets des de l’any més antic fins al més recent? Hi ha una tendència clara?  
