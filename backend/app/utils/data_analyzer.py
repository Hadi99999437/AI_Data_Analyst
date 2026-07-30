import pandas as pd


def load_dataset(path: str):
    extension = path.split(".")[-1].lower()

    if extension == "csv":
        return pd.read_csv(path)

    if extension in ["xlsx", "xls"]:
        return pd.read_excel(path)

    raise Exception("Unsupported file")