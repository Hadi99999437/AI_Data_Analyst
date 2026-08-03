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
        # -----------------------------------
    # Correlation Heatmap
    # -----------------------------------

    def create_heatmap(self, df):

        numeric_df = df.select_dtypes(
            include="number"
        )

        if numeric_df.shape[1] < 2:
            return None

        plt.figure(figsize=(10, 8))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )

        plt.title("Correlation Heatmap")

        return self._save_plot()

    # -----------------------------------
    # Boxplots
    # -----------------------------------
    def create_boxplots(self, df):

        charts = []

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            plt.figure(figsize=(8, 5))

            sns.boxplot(
                x=df[column]
            )

            plt.title(f"Boxplot - {column}")

            charts.append(
                self._save_plot()
            )

        return charts

    # -----------------------------------
    # Missing Values
    # -----------------------------------

    def create_missing_values_chart(self, df):

        missing = df.isnull().sum()

        missing = missing[
            missing > 0
        ]

        if len(missing) == 0:
            return None

        plt.figure(figsize=(10, 5))

        missing.sort_values().plot.bar()

        plt.title("Missing Values")

        plt.ylabel("Count")

        return self._save_plot()

    # -----------------------------------
    # Bar Charts
    # -----------------------------------

    def create_bar_charts(self, df):

        charts = []

        categorical_columns = df.select_dtypes(
            include=["object", "category"]
        ).columns

        for column in categorical_columns:

            values = (
                df[column]
                .value_counts()
                .head(10)
            )

            if len(values) == 0:
                continue

            plt.figure(figsize=(10, 5))

            values.plot.bar()

            plt.title(column)

            charts.append(
                self._save_plot()
            )

        return charts

    # -----------------------------------
    # Scatter Plots
    # -----------------------------------

    def create_scatter_plots(self, df):

        charts = []

        numeric_df = df.select_dtypes(include="number")

        if numeric_df.shape[1] < 2:
            return charts

        # -----------------------------------
        # Select the most informative columns
        # (highest variance)
        # -----------------------------------

        variance = (
            numeric_df.var()
            .sort_values(ascending=False)
        )

        top_columns = variance.head(5).index.tolist()

        # -----------------------------------
        # Correlation matrix
        # -----------------------------------

        corr = numeric_df[top_columns].corr().abs()

        used_pairs = set()

        for col in top_columns:

            correlations = (
                corr[col]
                .drop(col)
                .sort_values(ascending=False)
            )

            for other in correlations.index:

                pair = tuple(sorted([col, other]))

                if pair in used_pairs:
                    continue

                if correlations[other] < 0.30:
                    continue

                used_pairs.add(pair)

                plt.figure(figsize=(8, 6))

                plt.scatter(
                    df[col],
                    df[other],
                    alpha=0.6
                )

                plt.xlabel(col)
                plt.ylabel(other)

                plt.title(f"{col} vs {other}")

                charts.append(self._save_plot())

                # Maximum 5 scatter plots
                if len(charts) >= 5:
                    return charts

        return charts