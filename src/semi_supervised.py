from sklearn.ensemble import RandomForestClassifier

def pseudo_labeling(X_labeled, y_labeled, X_unlabeled):

    model = RandomForestClassifier()

    # Train on labeled data
    model.fit(X_labeled, y_labeled)

    # Predict pseudo labels
    pseudo_labels = model.predict(X_unlabeled)

    return pseudo_labels
