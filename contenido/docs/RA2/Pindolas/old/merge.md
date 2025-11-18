import pandas as pd
import numpy as np

# 1. Cargar datos primarios
df_matches = pd.read_csv('international_matches.csv', parse_dates=['Date'])

# 2. Crear columnas numéricas
df_matches['Home Goals'] = pd.to_numeric(df_matches['Home Goals'], errors='coerce')
df_matches['Away Goals'] = pd.to_numeric(df_matches['Away Goals'], errors='coerce')

# 3. Crear goal_diff y total_goals
df_matches['goal_diff']   = df_matches['Home Goals'] - df_matches['Away Goals']
df_matches['total_goals'] = df_matches['Home Goals'] + df_matches['Away Goals']

# 4. Cargar CSV adicional, por ejemplo equipos
df_teams = pd.read_csv('teams.csv')  # supuestos campos: Team, Continent, FIFA_Rank

# 5. Hacer merge para añadir información del equipo local
df = df_matches.merge(df_teams, how='left', left_on='Home Team', right_on='Team', suffixes=('','_home'))

# 6. Ahora tienes en `df` información del equipo local: Continent_home, FIFA_Rank_home etc.

# 7. Análisis exploratorio cruzado
#   a) Promedio de goal_diff por continente
continent_stats = df.groupby('Continent')[['goal_diff']].agg(['mean','std','count']).reset_index()
print(continent_stats)

#   b) Correlación entre ranking (FIFA_Rank_home) y goal_diff
corr = df[['FIFA_Rank_home','goal_diff']].corr()
print("Correlación entre ranking y diferencia de goles:", corr)

# 8. Visualización
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='FIFA_Rank_home', y='goal_diff')
plt.xlabel('Ranking FIFA del equipo local')
plt.ylabel('Diferencia de goles (local - visitante)')
plt.title('Ranking vs ventaja de goles local')
plt.show()
