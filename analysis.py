"""
Starter analysis script for the lab playground repo.

Columns in data/sample.csv:
    student_id    - int, unique row identifier
    study_hours   - float, hours studied before the exam
    sleep_hours   - float, hours slept the night before
    exam_score    - int, exam score out of 100

This script is intentionally minimal. It's here so the repo has something
runnable, not as the focus of today's lab.
"""

import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "sample.csv"



def load_data(path=DATA_PATH):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def testchange():
    return 0
#hi changing file

def summarize(rows):
    scores = [float(r["exam_score"]) for r in rows]
    study_hours = [float(r["study_hours"]) for r in rows]
    n = len(rows)
    print(f"n = {n}")
    print(f"mean exam score   = {sum(scores) / n:.1f}")
    print(f"mean study hours  = {sum(study_hours) / n:.2f}")


if __name__ == "__main__":
    data = load_data()
    summarize(data)
