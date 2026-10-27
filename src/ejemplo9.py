import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Gráfica de seno
axs[0].plot(x, y_sin)
axs[0].set_title('Seno')

# Gráfica de coseno
axs[1].plot(x, y_cos, 'r')
axs[1].set_title('Coseno')

# Ajustar el espacio entre subplots
plt.tight_layout()

# Mostrar la gráfica
plt.show()