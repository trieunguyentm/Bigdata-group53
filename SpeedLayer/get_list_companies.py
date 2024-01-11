import pandas as pd


def get_list_companies():
    df = pd.read_csv("./data/list_companies.csv")
    list_companies = df.iloc[:, 0].tolist()
    return list_companies
