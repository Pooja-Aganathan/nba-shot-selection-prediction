from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier


def train_models(
    X_train,
    y_train
):

    models = {}

    models[
        'Logistic Regression'
    ] = LogisticRegression(
        max_iter=1000
    )

    models[
        'Random Forest'
    ] = RandomForestClassifier(
        random_state=42
    )

    models[
        'XGBoost'
    ] = XGBClassifier(
        random_state=42
    )

    for name, model in models.items():

        model.fit(
            X_train,
            y_train
        )

    return models
