import math
import numpy as np
import scipy.stats as stats

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

def print_scores(model):
    print("R^2: " + str(model.score(X_test, y_test)))
    print("RMSE: " + str(rmse(y_test, model.predict(X_test))) ) # root mean squared error
    print("MAE: " + str(metrics.mean_absolute_error(y_test, model.predict(X_test)))) # mean absolute error
    print("MAPE: " + str(mape(y_test, model.predict(X_test)))) # mean absolute percent error
    print("Error within 20: " + str(error_within(0.2, y_test, model.predict(X_test)))) # error within
    print("Pearson: " + str(stats.pearsonr(y_test, model.predict(X_test)))) # pearson correlation
    
