import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ГРАФИКОВ ПАР (SEABORN)
#Загрузка набора данных Iris
iris = sns.load_dataset('iris')
# График пар (Pair Plot)
sns.pairplot(iris, hue='species', markers=['o', 's', 'D'])
plt.title('Графики пар в наборе данных Iris')
plt.show()



#ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ МНОГОУРОВНЕВЫХ ГРАФИКОВ (SEABORN)
#Загрузка набора данных о ценах на алмазы
tips = sns.load_dataset('diamonds')
# FacetGrid: многоуровневый график цикла по категориям
g = sns.FacetGrid(tips, col='cut', hue='color', margin_titles=True)
g.map(sns.scatterplot, 'carat', 'price', alpha=0.7)
g.add_legend()
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Цены на алмазы по категории и цвету')
plt.show()



#ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ГРАФИКОВ С НЕСКОЛЬКИМИ ОСЯМИ (SEABORN)
#Dummy data: расходы и доходы
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'expenses': [500, 600, 700, 800, 900, 700, 950, 800, 1100, 900, 1000, 1200],
    'income': [800, 950, 1000, 1100, 1200, 1150, 1300, 1400, 1350, 1600, 1500, 1800]
}
df = pd.DataFrame(data)
# Создание графиков с несколькими осями
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
sns.lineplot(data=df, x='month', y='expenses', ax=ax1, color='r', marker='o', label='Расходы')
sns.lineplot(data=df, x='month', y='income', ax=ax2, color='g', marker='s', label='Доходы')
# Настройка осей и легенд
ax1.set_ylabel('Расходы', color='r')
ax2.set_ylabel('Доходы', color='g')
ax1.set_title('Сравнение расходов и доходов по месяцам')
ax1.set_xticks(range(len(df['month'])))
ax1.set_xticklabels(df['month'])
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()