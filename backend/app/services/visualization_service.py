import os
import uuid
import matplotlib.pyplot as plt


class VisualizationService:

    def __init__(self):
        self.output_dir = "uploads/charts"
        os.makedirs(self.output_dir, exist_ok=True)

    def create_histogram(self, df):

        numeric_columns = df.select_dtypes(include="number").columns

        if len(numeric_columns) == 0:
            return []

        charts = []

        for column in numeric_columns:

            plt.figure(figsize=(8,5))

            df[column].hist(
                bins=20,
                edgecolor="black"
            )

            plt.title(column)

            filename = f"{uuid.uuid4()}.png"

            path = os.path.join(
                self.output_dir,
                filename
            )

            plt.savefig(path)
            plt.close()

            charts.append(path)

        return charts