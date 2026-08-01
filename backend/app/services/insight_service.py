
class InsightService:

    def generate_insights(self, analysis_result: dict):

        insights = []
        recommendations = []

        rows = analysis_result["rows"]
        columns = analysis_result["columns"]

        insights.append(
            f"The dataset contains {rows} rows and {columns} columns."
        )

        # -----------------------------
        # Missing Values
        # -----------------------------

        missing = analysis_result["missing_values"]

        for column, count in missing.items():

            if count == 0:
                continue

            percentage = round((count / rows) * 100, 2)

            insights.append(
                f"{column} contains {count} missing values ({percentage}%)."
            )

            if percentage > 5:

                recommendations.append(
                    f"Consider handling missing values in '{column}'."
                )

        # -----------------------------
        # Numeric & Categorical Summary
        # -----------------------------

        summary = analysis_result["summary"]

        for column, values in summary.items():

            # Numeric columns

            if values.get("mean") != "":

                minimum = values.get("min")
                maximum = values.get("max")
                mean = values.get("mean")
                std = values.get("std")

                insights.append(
                    f"{column} ranges from {minimum} to {maximum} (mean {round(mean,2)})."
                )

                if std > mean:

                    insights.append(
                        f"{column} shows high variation and may contain outliers."
                    )

                    recommendations.append(
                        f"Inspect '{column}' for potential outliers."
                    )

            # Categorical columns

            elif values.get("top") != "":

                top = values.get("top")
                freq = values.get("freq")
                unique = values.get("unique")

                insights.append(
                    f"The most common value in '{column}' is '{top}' ({freq} records)."
                )

                if unique == 1:

                    recommendations.append(
                        f"'{column}' contains only one unique value and may not be useful."
                    )

        return {
            "insights": insights,
            "recommendations": recommendations,
        }