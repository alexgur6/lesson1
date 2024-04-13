import matplotlib.pyplot as plt

counts = [17, 3]
plt.figure(figsize=(5, 5))
plt.pie(counts,
        colors=['royalblue', 'gold'],  # Цвета долей
        labels=['Dogs', 'Cats'],       # Подписи
        startangle=120,                # Начальный угол
        autopct='%.3f%%'               # Формат вывода значений долей
        )
plt.show()
