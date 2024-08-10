import matplotlib.pyplot as plt

# Datos de la tabla
distancias = [10, 20, 30, 40, 50, 60, 70]
subida_1 = [2.58, 2.36, 1.88, 1.48, 1.22, 1.04, 0.9]
bajada_1 = [2.63, 2.33, 1.87, 1.47, 1.21, 1.03, 0.9]
subida_2 = [2.65, 2.33, 1.86, 1.48, 1.21, 1.04, 0.9]
bajada_2 = [2.6, 2.33, 1.86, 1.47, 1.21, 1.04, 0.9]
subida_3 = [2.63, 2.33, 1.87, 1.48, 1.22, 1.05, 0.91]
bajada_3 = [2.6, 2.33, 1.86, 1.48, 1.23, 1.05, 0.9]

# Crear las gráficas de histéresis
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Gráfica 1
axs[0].plot(distancias, subida_1, 'b-', marker='o', label='Subida 1')
axs[0].plot(distancias, bajada_1, 'r-', marker='o', label='Bajada 1')
axs[0].set_title('Histeresis Medición 1')
axs[0].set_xlabel('Distancia (cm)')
axs[0].set_ylabel('Voltaje (V)')
axs[0].legend()

# Gráfica 2
axs[1].plot(distancias, subida_2, 'b-', marker='o', label='Subida 2')
axs[1].plot(distancias, bajada_2, 'r-', marker='o', label='Bajada 2')
axs[1].set_title('Histeresis Medición 2')
axs[1].set_xlabel('Distancia (cm)')
axs[1].set_ylabel('Voltaje (V)')
axs[1].legend()

# Gráfica 3
axs[2].plot(distancias, subida_3, 'b-', marker='o', label='Subida 3')
axs[2].plot(distancias, bajada_3, 'r-', marker='o', label='Bajada 3')
axs[2].set_title('Histeresis Medición 3')
axs[2].set_xlabel('Distancia (cm)')
axs[2].set_ylabel('Voltaje (V)')
axs[2].legend()

plt.tight_layout()
plt.show()
