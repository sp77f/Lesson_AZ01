import pandas as pd
import numpy as np

# Создание данных для датафрейма
data = {
    'Ученик': ['Иванов Иван', 'Петров Петр', 'Сидоров Сидор', 'Смирнова Елена', 'Николаева Анна', 'Кузнецов Дмитрий', 'Васильева Ольга', 'Козлов Сергей', 'Морозова Мария', 'Новиков Александр'],
    'Математика': np.random.randint(2, 5, 10),
    'Литература': np.random.randint(2, 5, 10),
    'История': np.random.randint(2, 5, 10),
    'Химия': np.random.randint(2, 5, 10),
    'Физика': np.random.randint(2, 5, 10)
}

# Задание 1 Создание датафрейма
df = pd.DataFrame(data)

# Задание 2 Вывод нескольких первых строк датафрейма
print(df.head())

# Задание 3 Расчет средних оценок по каждому предмету
print('\nСредние оценки по предметам:')
print(f"Средняя оценка по математике: {df['Математика'].mean()}")
print(f"Средняя оценка по литературе: {df['Литература'].mean()}")
print(f"Средняя оценка по истории: {df['История'].mean()}")
print(f"Средняя оценка по химии: {df['Химия'].mean()}")
print(f"Средняя оценка по физике: {df['Физика'].mean()}")

# Задание 4 Расчет медианнных оценок по каждому предмету
print('\nМедианные оценки по предметам:')
print(f"Медианные оценки по математике: {df['Математика'].median()}")
print(f"Медианные оценки по литературе: {df['Литература'].median()}")
print(f"Медианные оценки по истории: {df['История'].median()}")
print(f"Медианные оценки по химии: {df['Химия'].median()}")
print(f"Медианные оценки по физике: {df['Физика'].median()}")

# Задание 5 Расчет Q1 и Q3 по математике
q1_math = df['Математика'].quantile(0.25)
q3_math = df['Математика'].quantile(0.75)
IQR_math = q3_math - q1_math
std = df['Математика'].std()

print('\nКвантили по математике:')
print(f"Квантили по математике: Q1: {q1_math}, Q3: {q3_math}")
print(f"Межквартильный размах по математике: {IQR_math}")
print(f"Стандартное отклонение по математике: {std}")