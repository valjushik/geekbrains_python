from scipy import stats
import numpy as np
import pandas as pd
from scipy.stats import t

print('Задание №1:')
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

mean_zp = sum(zp) / len(zp)
mean_ks = sum(ks) / len(ks)
cov = sum((zp[i] - mean_zp) * (ks[i] - mean_ks) for i in range(len(zp))) / (len(zp) - 1)
print("Ковариация (ручная):", cov)

cov_np = np.cov(zp, ks, ddof=1)[0][1]
print("Ковариация (numpy):", cov_np)

std_zp = np.std(zp, ddof=1)
std_ks = np.std(ks, ddof=1)
corr = cov / (std_zp * std_ks)
print("Коэффициент корреляции Пирсона (ручной):", corr)


corr_np = np.corrcoef(zp, ks)[0][1]
print("Коэффициент корреляции Пирсона (numpy):", corr_np)

df = pd.DataFrame({'zp': zp, 'ks': ks})
corr_pd = df['zp'].corr(df['ks'])
print("Коэффициент корреляции Пирсона (pandas):", corr_pd)

print('Задание №2:')
data = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
alpha = 0.05
n = len(data)

mean = np.mean(data)
std = np.std(data, ddof=1)

t_value = t.ppf(1 - alpha/2, df=n-1)

CI = (mean - t_value * std / np.sqrt(n), mean + t_value * std / np.sqrt(n))
print("Доверительный интервал для математического ожидания:", CI)


print('Задание №3:')
sigma = np.sqrt(25)
alpha = 0.05
n = 27
mean = 174.2

SE = sigma / np.sqrt(n)

z_value = t.ppf(1 - alpha/2, df=n-1)

CI = (mean - z_value * SE, mean + z_value * SE)
print("Доверительный интервал для математического ожидания:", CI)
