import pandas as pd

def load_data():

    df = pd.read_csv("data/raw/nba_shot_data.csv")

    return df
