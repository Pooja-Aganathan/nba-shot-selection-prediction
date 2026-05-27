from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def train_models(X_train, y_train):

    models = {}

    models["RandomForest"] = RandomForestClassifier().fit(X_train, y_train)

    models["XGBoost"] = XGBClassifier(use_label_encoder=False, eval_metric='logloss').fit(X_train, y_train)

    return models
