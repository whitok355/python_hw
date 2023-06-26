# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

# df[df['population']<501]['median_house_value'].agg(['mean'])
# # mean    206799.951402
# # Name: median_house_value, dtype: float64


# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

# df[df['population']==df['population'].min()]['households'].max()
# # 4.0