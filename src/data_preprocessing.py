import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess(df):

    df = df.dropna(subset=["SHOT_RESULT"])

    return df


def encode_scale(X):

    X = pd.get_dummies(X, drop_first=True)

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X
