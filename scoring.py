def mse(classifier, X_train, X_test, y_train, y_test):
    pred = classifier.fit(X_train, y_train).predict(X_test)
    return ((pred - y_test) ** 2).mean()
