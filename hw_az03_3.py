from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def clean_price(price):
   # Удаляем "руб." и преобразуем в число
   return int(price.replace('руб.', '').replace(' ', ''))


# Запускаем веб-драйвер (Chrome)
driver = webdriver.Chrome()

# Переходим на страницу с диванами на сайте divan.ru
driver.get("https://www.divan.ru/category/divany-i-kresla")

# Находим все элементы с ценами
prices = driver.find_elements(By.CSS_SELECTOR,"span.ui-LD-ZU.KIkOH[data-testid='price']")
for price in prices:
    print(price.text)


with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])
# Закрываем веб-драйвер
driver.quit()
input_file = 'prices.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")
data = pd.read_csv('cleaned_prices.csv')
print(f"\nCредняя цена диванов {round(data['Price'].mean(),2)} руб.")
plt.hist(data, bins=10)
plt.show()
