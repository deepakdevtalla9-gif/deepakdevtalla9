import csv
import json
from pathlib import Path

OUTPUT_DIR = Path("practice_output")
OUTPUT_DIR.mkdir(exist_ok=True)

# CSV: write data
csv_path = OUTPUT_DIR / "students.csv"
students = [
    {"id": "101", "name": "Aman", "marks": 85},
    {"id": "102", "name": "Riya", "marks": 92},
]

with csv_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "marks"])
    writer.writeheader()
    writer.writerows(students)

# CSV: read data
with csv_path.open("r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print("CSV record:", row)

# JSON: write data
json_path = OUTPUT_DIR / "students.json"
with json_path.open("w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

# JSON: read data
with json_path.open("r", encoding="utf-8") as file:
    loaded_students = json.load(file)

print("JSON records:", loaded_students)
