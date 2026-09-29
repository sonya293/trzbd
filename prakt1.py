import numpy as np

data_steps = np.array([
    8200, 11500, 9400, 7100, 10800, 8600, 12900, 45000, 9900, 9100,
    7600, 11300, 8300, 9700, 10400, 8900, 12100, 6800, 10200, 9200,
    200, 450, 8100, 11600, 7900, 9600, 10700, 8700, 12200, 6900
])

avr = np.mean(data_steps)
print(f"Среднее значение: {avr}")

median = np.median(data_steps)
print(f"Медиана: {median}")

dispersia = np.var(data_steps)
print(f"Дисперсия: {dispersia}")

standart_otkl = np.std(data_steps)
print(f"Стандартное отклонение: {standart_otkl}")

maximum = np.max(data_steps)
print(f"Максимальное значение: {maximum}")

minimum = np.min(data_steps)
print(f"Минимальное значение: {minimum}")

peaktopeak = np.ptp(data_steps)
print(f"Размах данных: {peaktopeak}")

percentiles = np.percentile(data_steps, [25, 50, 75, 90, 99])
print(f"Перцентили 25, 50, 75, 90, 99: {percentiles}")

q1 = np.percentile(data_steps, 25)
q2 = np.percentile(data_steps, 50)
q3 = np.percentile(data_steps, 75)

print(f"Первый квартиль: {q1}")
print(f"Второй квартиль: {q2}")
print(f"Третий квартиль: {q3}")

iqr = q3 - q1
print(f"Межквартильный размах: {iqr}")

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = data_steps[(data_steps < lower) | (data_steps > upper)]

print(f"Нижняя граница: {lower}")
print(f"Верхняя граница: {upper}")
print(f"Выбросы: {outliers}")

A = np.array([
    8000, 12000, 9500, 7000, 11000,
    8500, 13000, 6000, 10000, 9000,
    7500, 11500, 8200, 9800, 10500
])
matrix = A.reshape(3, 5)
print("Матрица 3х5:")
print(matrix)

print(f"Размерность: {matrix.shape}")

print(f"Количество элементов: {matrix.size}")

print(f"Сумма по строкам: {matrix.sum(axis=1)}")

print(f"Сумма по столбцам: {matrix.sum(axis=0)}")

print("Транспонированная матрица:")
print(matrix.T)

print(f"Среднее значение матрицы: {np.mean(matrix)}")
print(f"Стандартное отклонение матрицы: {np.std(matrix)}")
print(f"Дисперсия матрицы: {np.var(matrix)}")

quatr = np.percentile(matrix, [25, 50, 75])
print(f"Квартили матрицы: {quatr}")

days_less_8000 = np.sum(data_steps < 8000)
print(f"Количество дней с количеством шагов меньше 8000: {days_less_8000}")