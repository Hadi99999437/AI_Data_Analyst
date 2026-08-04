from datetime import datetime


class ReportService:

    def generate_report(self, analysis_result: dict):

        return {
            "title": "AI Data Analysis Report",

            "generated_at": datetime.utcnow().isoformat(),

            "dataset": {
                "rows": analysis_result["rows"],
                "columns": analysis_result["columns"],
                "column_names": analysis_result["column_names"],
            },

            "quality": {
                "missing_values": analysis_result["missing_values"],
                "duplicate_rows": analysis_result["duplicate_rows"],
            },

            "summary_statistics":
                analysis_result["summary"],

            "correlation":
                analysis_result.get("correlation", {}),

            "visualizations":
                analysis_result.get("visualizations", {}),

            "rule_based":
                analysis_result.get("rule_based", {}),

            "ai":
                analysis_result.get("ai", {}),

            "advanced_analysis": {
                "outliers": analysis_result.get("outliers", {}),
                "skewness": analysis_result.get("skewness", {}),
                "constant_columns": analysis_result.get("constant_columns", []),
                "high_correlations": analysis_result.get("high_correlations", []),
                "numeric_statistics": analysis_result.get("numeric_statistics", {})
            }
        }