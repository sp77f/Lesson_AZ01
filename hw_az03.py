import numpy as np
import matplotlib.pyplot as plt

# Задание 1 гистограмму для случайных данных
mean = 0
std_dev = 1
num_samples = 1000
data = np.random.normal(mean, std_dev, num_samples)
plt.hist(data, bins=20)
plt.title('Гистограмма случайных данных')
plt.xlabel('Значения')
plt.ylabel('Количество')
plt.show()
# Задание 2 диаграмму рассеяния для двух наборов случайных данных
data1 = np.random.rand(10)
data2 = np.random.rand(10)
plt.scatter(data1, data2)
plt.title('Диаграмма рассеяния')
plt.xlabel('Первый набор данных')
plt.ylabel('Второй набор данных')
plt.show()
# Задание 3 ПАРСИНГ ДИВАН РУ

