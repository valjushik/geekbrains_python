from scipy import stats
import numpy as np

# данные
football = [173, 175, 180, 178, 177, 185, 183, 182]
hockey = [177, 179, 180, 188, 177, 172, 171, 184, 180]
weightlifting = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]

# количество элементов в каждой выборке
n_football = len(football)
n_hockey = len(hockey)
n_weightlifting = len(weightlifting)

# среднее значение для каждой выборки
mean_football = np.mean(football)
mean_hockey = np.mean(hockey)
mean_weightlifting = np.mean(weightlifting)

# среднее квадратичное отклонение для каждой выборки
std_football = np.std(football, ddof=1)
std_hockey = np.std(hockey, ddof=1)
std_weightlifting = np.std(weightlifting, ddof=1)

# проверка нормальности распределения
print("Нормальность распределения:")
print("Футболисты:", stats.shapiro(football))
print("Хоккеисты:", stats.shapiro(hockey))
print("Штангисты:", stats.shapiro(weightlifting))

# проверка однородности дисперсии
print("Однородность дисперсии:")
print(stats.levene(football, hockey, weightlifting))

# Однофакторный дисперсионный анализ
print("Однофакторный дисперсионный анализ:")
f_value, p_value = stats.f_oneway(football, hockey, weightlifting)
print("F-value:", f_value)
print("P-value:", p_value)


import pandas as pd
from scipy.stats import f_oneway, shapiro, levene, f
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# множественное сравнение
df = pd.DataFrame({'vals': football + hockey + weightlifting,
                   'group': ['football']*len(football) + ['hockey']*len(hockey) + ['weightlifting']*len(weightlifting)})
tukey = pairwise_tukeyhsd(df.vals, df.group)
print(tukey)

# распределение Фишера
f_dist = f(len(df['group'].unique())-1, len(df)-len(df['group'].unique()))
print("Критическое значение распределения Фишера:", f_dist.ppf(1-0.05))


# добавление значений
football = np.append(football, [np.mean(football)]*3)
hockey = np.append(hockey, [np.mean(hockey)]*2)

# однофакторный дисперсионный анализ
f_value, p_value = f_oneway(football, hockey, weightlifting)
print("F-статистика: ", f_value)
print("p-value: ", p_value)

# post hoc тест Тьюки
data = np.concatenate([football, hockey, weightlifting])
labels = ['football']*len(football) + ['hockey']*len(hockey) + ['weightlifting']*len(weightlifting)
tukey_results = pairwise_tukeyhsd(data, labels, 0.05)
print(tukey_results)
