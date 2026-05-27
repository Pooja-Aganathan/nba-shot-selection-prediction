from sklearn.metrics import accuracy_score, f1_score

def evaluate(model, X_test, y_test):

    y_pred = model.predict(X_test)

    return {
        "Accuracy": accuracy_score(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred)
    }
