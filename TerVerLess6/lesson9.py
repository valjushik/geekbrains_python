import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(zp)

b = sum((zp - np.mean(zp)) * (ks - np.mean(ks))) / sum((zp - np.mean(zp))**2)
a = np.mean(ks) - b * np.mean(zp)
print("Коэффициенты линейной регрессии без intercept: b =", b, "a =", a)

X = np.column_stack((np.ones(n), zp))
beta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), ks)
print("Коэффициенты линейной регрессии с intercept: b =", beta[1], "a =", beta[0])

b = 0
a = 0
alpha = 0.0001
n_iter = 1000

for i in range(n_iter):
    y_pred = b * zp
mse = np.mean((ks - y_pred)**2)
b_grad = -2 * np.mean(zp * (ks - y_pred))
b = b - alpha * b_grad

print("Коэффициент линейной регрессии без intercept: b =", b)


b = 0
a = 0
alpha = 0.0001
n_iter = 1000


for i in range(n_iter):
    y_pred = b * zp + a
mse = np.mean((ks - y_pred)**2)
b_grad = -2 * np.mean(zp * (ks - y_pred))
a_grad = -2 * np.mean(ks - y_pred)
b = b - alpha * b_grad
a = a - alpha * a_grad

print("Коэффициенты линейной регрессии с intercept: b =", b, "a =", a)
