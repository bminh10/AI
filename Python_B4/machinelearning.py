import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

#du lieu
x = np.array([1,2,4,4,5])
y = np.array([2,4,5,4,6])
X = x.reshape(-1,1)

model = LinearRegression().fit(X,y)
w1 = model.coef_
w0 = model.intercept_


print(f"y_hat = {w0:.4f} + {w1:.4f} * x")