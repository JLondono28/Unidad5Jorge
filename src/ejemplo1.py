import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y = np.tan(x)

# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Tangente')
plt.xlabel('X')
plt.ylabel('tan(X)')

# Mostrar la gráfica
plt.show()