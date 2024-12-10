import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ИНТЕРАКТИВНОГО ГРАФИКА РАССЕЯНИЯ (PLOTLY)
# Загрузка данных о цветах Iris
iris = px.data.iris()
# Создание графика рассеяния
fig = px.scatter(iris, x='sepal_width', y='sepal_length', color='species',
                 title='График рассеяния для цветов Iris')
fig.show()


# ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ КРУГОВОЙ ДИАГРАММЫ (PLOTLY)
# Данные о расходах по категориям
categories = ['Продукты', 'Транспорт', 'Жилище', 'Развлечения', 'Здоровье']
values = [400, 150, 600, 200, 100]
df = pd.DataFrame({
    'categories': categories,
    'values': values
})

# Создание круговой диаграммы
fig = px.pie(df, values='values', names='categories', title='Распределение расходов')
fig.show()
# Создание данных
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
expenses = [500, 600, 700, 800, 900, 700, 950, 800, 1100, 900, 1000, 1200]
income = [800, 950, 1000, 1100, 1200, 1150, 1300, 1400, 1350, 1600, 1500, 1800]
df = pd.DataFrame({
    'months': months,
    'expenses': expenses,
    'income': income
})



# ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ГРАФИКА С НЕСКОЛЬКИМИ ОСЯМИ (PLOTLY)
# Создание графика с несколькими осями
fig = go.Figure()
# Добавление графика расходов
fig.add_trace(go.Scatter(x=df['months'], y=df['expenses'], mode='lines+markers', name='Расходы', line=dict(color='red')))
# Добавление графика доходов
fig.add_trace(go.Scatter(x=df['months'], y=df['income'], mode='lines+markers', name='Доходы', line=dict(color='green')))
# Настройка меток осей и заголовка
fig.update_layout(title='Сравнение расходов и доходов по месяцам', yaxis_title='Сумма (в $)')
fig.show()