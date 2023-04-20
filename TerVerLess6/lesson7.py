
from scipy.stats import mannwhitneyu
print('Задание №1:')
x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]

stat, p = mannwhitneyu(x1, y1)
print('Statistics=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
if p > alpha:
    print('Выборки не различаются\n')
else:
    print('Выборки различаются\n')

from scipy import stats
import numpy as np


print('Задание №2:')
before = [150, 160, 165, 145, 155]
after_10 = [140, 155, 150, 130, 135]
after_30 = [130, 130, 120, 130, 125]

chi2_statistic, p_value = stats.friedmanchisquare(before, after_10, after_30)
print(chi2_statistic, p_value)
if p_value > alpha:
    print('Нет статистически значимых различий\n')
else:
    print('Есть статистически значимые различия\n')



print('Задание №3:')

t_statistic1, p_value1 = stats.ttest_rel(before, after_10)
t_statistic2, p_value2 = stats.ttest_rel(before, after_30)
t_statistic3, p_value3 = stats.ttest_rel(after_10, after_30)

print(t_statistic1, p_value1)
if p_value1 > alpha:
    print('Выборки до приема и после 10 мин не различаются\n')
else:
    print('Выборки до приема и после 10 мин различаются\n')

print(t_statistic2, p_value2)
if p_value2 > alpha:
    print('Выборки до приема и после 30 мин не различаются\n')
else:
    print('Выборки до приема и после 30 мин различаются\n')

print(t_statistic3, p_value3)
if p_value3 > alpha:
    print('Выборки после 10 мин и после 30 мин не различаются\n')
else:
    print('Выборки после 10 мин и после 30 мин различаются\n')


print('Задание №4:')
group1 = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
group2 = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
group3 = [57, 67, 49, 48, 47, 55, 66, 51, 54]

h_statistic, p_value = stats.kruskal(group1, group2, group3)
print(h_statistic, p_value)
if p_value > alpha:
    print('Выборки не различаются\n')
else:
    print('Выборки различаются\n')


print('Задание №5:')
import statistics
data = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
t_statistic, p_value = stats.ttest_1samp(data, 2.5)
print(t_statistic, p_value)

x = statistics.mean(data)
m = 2.5
n = 10
s = np.std(data)
t = (x - m) / (s / (n**0.5))
print(t)

if t > alpha:
    print('Нет статистически значимых различий\n')
else:
    print('Есть статистически значимые различия\n')