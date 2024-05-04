import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Importar los datos
df = pd.read_csv("epa-sea-level.csv")

# Crear el diagrama de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# Calcular la línea de mejor ajuste para todos los datos
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Predecir el aumento del nivel del mar en 2050
x_pred = range(1880, 2051)
y_pred = slope * x_pred + intercept

# Trazar la línea de mejor ajuste
plt.plot(x_pred, y_pred, color='red', label='Best Fit Line (All Data)')

# Calcular la línea de mejor ajuste para los datos desde el año 2000 hasta el más reciente
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

# Predecir el aumento del nivel del mar en 2050 utilizando los datos más recientes
x_pred_recent = range(2000, 2051)
y_pred_recent = slope_recent * x_pred_recent + intercept_recent

# Trazar la línea de mejor ajuste utilizando los datos más recientes
plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit Line (Recent Data)')

# Etiquetas y título
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Leyenda
plt.legend()

# Guardar y mostrar el gráfico
plt.savefig('sea_level_rise.png')
plt.show()
