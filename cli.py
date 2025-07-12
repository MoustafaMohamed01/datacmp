import argparse
import pandas as pd
from datacmp.run_pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="Datacmp: Run EDA and cleaning pipeline from CLI.")
    parser.add_argument("--file", required=True, help="Path to input CSV file.")
    parser.add_argument("--config", default="config.yaml", help="Path to config YAML file.")
    parser.add_argument("--export_csv", help="Path to export cleaned CSV.")
    parser.add_argument("--export_report", help="Path to export TXT report.")

    args = parser.parse_args()

    try:
        df = pd.read_csv(args.file)
        run_pipeline(
            df,
            config_path=args.config,
            export_csv_path=args.export_csv,
            export_report_path=args.export_report
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
