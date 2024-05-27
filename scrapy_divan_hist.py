import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('divan_prices.csv')

# Найдем среднюю цену
average_price = df['price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} руб.')
