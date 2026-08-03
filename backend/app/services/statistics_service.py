import pandas as pd
import numpy as np


class StatisticsService:

    def analyze(self, df: pd.DataFrame):

        report = {}

        report["dataset"] = {
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
            "duplicate_rows": int(df.duplicated().sum()),
            "missing_cells": int(df.isnull().sum().sum()),
            "memory_usage_mb": round(
                df.memory_usage(deep=True).sum() / 1024 / 1024,
                2,
            ),
        }

        report["columns"] = {}

        for column in df.columns:

            series = df[column]

            column_info = {
                "dtype": str(series.dtype),
                "missing": int(series.isnull().sum()),
                "unique": int(series.nunique()),
            }

            if pd.api.types.is_numeric_dtype(series):

                clean = series.dropna()

                q1 = clean.quantile(0.25)
                q3 = clean.quantile(0.75)
                iqr = q3 - q1

                outliers = clean[
                    (clean < q1 - 1.5 * iqr)
                    | (clean > q3 + 1.5 * iqr)
                ]

                column_info.update(
                    {
                        "mean": float(clean.mean()),
                        "median": float(clean.median()),
                        "mode": clean.mode().tolist(),
                        "min": float(clean.min()),
                        "max": float(clean.max()),
                        "std": float(clean.std()),
                        "variance": float(clean.var()),
                        "skewness": float(clean.skew()),
                        "kurtosis": float(clean.kurt()),
                        "outliers": int(len(outliers)),
                    }
                )

            else:

                column_info.update(
                    {
                        "top": (
                            series.mode().iloc[0]
                            if not series.mode().empty
                            else None
                        ),
                        "value_counts": (
                            series.value_counts()
                            .head(10)
                            .to_dict()
                        ),
                    }
                )

            report["columns"][column] = column_info

        numeric = df.select_dtypes(include=np.number)

        if numeric.shape[1] > 1:

            report["correlation"] = (
                numeric.corr()
                .round(3)
                .fillna(0)
                .to_dict()
            )

        else:

            report["correlation"] = {}

        return report