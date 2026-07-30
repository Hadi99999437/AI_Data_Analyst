import pandas as pd


def load_dataset(path: str):
    extension = path.split(".")[-1].lower()

    if extension == "csv":
        return pd.read_csv(path)

    if extension in ["xlsx", "xls"]:
        return pd.read_excel(path)

    raise Exception("Unsupported file")

def dataset_summary(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.astype(str).to_dict(),
    }    