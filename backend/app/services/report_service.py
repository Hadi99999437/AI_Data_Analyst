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
                analysis_result["correlation"],

            "charts":
                analysis_result["charts"],

            "rule_based":
                analysis_result["rule_based"],

            "ai":
                analysis_result["ai"],
        }