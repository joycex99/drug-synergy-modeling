import math
import numpy as np

# Mean squared error
def mse(classifier, X_train, X_test, y_train, y_test):
    pred = classifier.fit(X_train, y_train).predict(X_test)
    return ((pred - y_test) ** 2).mean()

# Root mean squared error
def rmse(y_pred, y_true):
    return math.sqrt(((y_true-y_pred)**2).mean())

# Mean absolute error
def mape(y_pred, y_true):
    return np.mean(np.abs((y_true - y_pred) / y_true))

# Percent of predictions within a certain value to true value
def error_within(epsilon, y_pred, y_true):
    #within = np.absolute(y_true-y_pred) < epsilon
    #return np.sum(within)/within.size
    within = np.absolute((y_true-y_pred)/y_true) < epsilon * y_true
    return np.sum(within)/within.size
    
