import os
import uuid

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class VisualizationService:

    def __init__(self):
        self.output_dir = "uploads/charts"
        os.makedirs(self.output_dir, exist_ok=True)

    def _save_plot(self):

        filename = f"{uuid.uuid4()}.png"

        path = os.path.join(
            self.output_dir,
            filename
        )

        plt.tight_layout()
        plt.savefig(path)
        plt.close()

        return path

    # -----------------------------------
    # Histograms
    # -----------------------------------

    def create_histogram(self, df):

        charts = []

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            plt.figure(figsize=(8, 5))

            df[column].dropna().hist(
                bins=20,
                edgecolor="black"
            )

            plt.title(f"Histogram - {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")

            charts.append(
                self._save_plot()
            )

        return charts