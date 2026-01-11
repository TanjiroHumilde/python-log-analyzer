# Python Log Analyzer

This project is a simple Python automation tool designed to analyze system log files and detect common critical events such as errors and warnings.

## Features
- Reads `.log` files
- Detects ERROR, WARNING, and FAILED events
- Generates a CSV report with event counts
- Helps reduce manual troubleshooting time

## Technologies
- Python 3
- CSV module

## Use Case
Ideal for IT support and system administrators who need quick insights from log files without manual scanning.

## How to Run
1. Place your log file in the project folder
2. Run:
   python log_analyzer.py
3. Review the generated `report.csv`
