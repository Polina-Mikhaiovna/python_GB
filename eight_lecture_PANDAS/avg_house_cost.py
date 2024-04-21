import pandas as pd

file = 'california_housing_train.csv'
df = pd.read_csv(file)

# создаём список в котором содержатся строки где population до 500 и ПРИМЕНЕНЯЕМ К НЕМУ ФУНКЦИЮ .mean()
# в avg сохранится:	median_house_value    206799.951402
#					dtype: float64
avg = df.loc[(df.population < 501), ['median_house_value']].mean()
# avg.iloc[0] - берём только подсчитанное значение, отбрасываем всё лишнее
# DataFrame.iloc[] - доступ к срезу данных DataFrame по позиции
print(avg.iloc[0])


# Задание 2
# Найти максимальное значение переменной "households"
# в зоне минимального значения переменной min_population и
# сохраните это значение в переменную max_households_in_min_population.

min_population = df.population.quantile(0.01)
max_households_in_min_population = df.loc[(df.population <= min_population), ['households']].max()

print(max_households_in_min_population.iloc[0])