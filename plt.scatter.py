import numpy as np
import matplotlib.pyplot as plt

num_samples = 5  # Количество образцов
data_x = np.random.rand(num_samples)  # Первый набор случайных данных
data_y = np.random.rand(num_samples)  # Второй набор случайных данных

plt.scatter(data_x, data_y, c='blue', alpha=0.5, edgecolors='w', s=50)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X значения')
plt.ylabel('Y значения')

plt.show()