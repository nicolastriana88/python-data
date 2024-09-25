import numpy as np
import matplotlib.pyplot as plt

# Serie estacionaria
n = 100
np.random.seed(0)

stationary_series = np.random.normal(0, 1, n)
plt.plot(stationary_series)
plt.title('Serie Estacionaria')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.show()

# Serie no estacionaria
trend = np.linspace(0, 10, n)
non_stationary_series = trend + np.random.normal(0, 1, n)
plt.plot(non_stationary_series)
plt.title('Serie No Estacionaria')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.show()

# Serie con estacionalidad
seasonal = 10 + np.sin(np.linspace(0, 20, n))
seasonal_series = seasonal + np.random.normal(0, 1, n)
plt.plot(seasonal_series)
plt.title('Serie con Estacionalidad')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.show()
