import csv

LOG_FILE = "sample.log"
REPORT_FILE = "report.csv"

KEYWORDS = ["ERROR", "WARNING", "FAILED"]

def analyze_log(file_path):
    results = {key: 0 for key in KEYWORDS}

    with open(file_path, "r") as file:
        for line in file:
            for key in KEYWORDS:
                if key in line:
                    results[key] += 1

    return results

def generate_report(results, output_file):
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Event Type", "Count"])

        for key, value in results.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    analysis_results = analyze_log(LOG_FILE)
    generate_report(analysis_results, REPORT_FILE)

    print("Log analysis completed.")
    print("Report generated:", REPORT_FILE)
