def create_features(df):

    df["SHOT_DISTANCE_BIN"] = pd.cut(df["SHOT_DISTANCE"], bins=[0,5,15,25,50])

    return df
