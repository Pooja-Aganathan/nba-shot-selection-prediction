from sklearn.model_selection import train_test_split

def split_data(df):

    X = df.drop("SHOT_RESULT", axis=1)
    y = df["SHOT_RESULT"]

    return X, y


def split_train_test(X, y):

    return train_test_split(X, y, test_size=0.2, random_state=42)
