import scipy
import numpy as np
import scipy.stats as st


mean = 80
std = 16
n = 256
se = std / (n**0.5)

left = mean - st.norm.ppf(0.975)*se
right = mean + st.norm.ppf(0.975)*se
print("Задача №1 \n", left, right)


#2) В результате 10 независимых измерений некоторой величины X,
# выполненных с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала,
# покрывающего это значение с доверительной вероятностью 0,95.

#define sample data
data = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
#create 95% confidence interval for population mean weight
print("Задача №2 \n", st.t.interval(confidence=0.95, df=len(data)-1, loc=np.mean(data), scale=st.sem(data)))


#Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
#Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
#Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

children_heights = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers_heights = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

mean_diff = np.mean(children_heights) - np.mean(mothers_heights)
std_error = np.sqrt(np.var(children_heights)/len(children_heights) + np.var(mothers_heights)/len(mothers_heights))
t_value = scipy.stats.t.ppf(0.975, df=len(children_heights)+len(mothers_heights)-2)

lower_bound = mean_diff - t_value*std_error
upper_bound = mean_diff + t_value*std_error

print("Задача №3 \n", lower_bound, upper_bound)

