# summarize_sptr.py

import csv
from datetime import datetime
import json
import os

def process_json_files(directory):
    volume_data = {"total": []}
    count_data = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            date = datetime.strptime(filename.split('.')[0], '%Y-%m-%d').date()
            with open(os.path.join(directory, filename), 'r') as file:
                data = json.load(file)
                volume_data["total"].append((date, data["total"]["volume"]))
                for project in data["projects"]:
                    if project["project"] not in volume_data:
                        volume_data[project["project"]] = []
                        count_data[project["project"]] = []
                    volume_data[project["project"]].append((date, project["volume"]))
                    count_data[project["project"]].append((date, project["count"]))
    return volume_data, count_data

def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        headers = ["date"] + list(data.keys())
        writer.writerow(headers)
        dates = sorted({date for _, series in data.items() for date, _ in series})
        for date in dates:
            row = [date]
            for series in data.values():
                value = next((v for d, v in series if d == date), None)
                row.append(value)
            writer.writerow(row)

def main_sync():
    directory = "test-output"
    volume_data, count_data = process_json_files(directory)
    write_csv("volume.csv", volume_data)
    write_csv("count.csv", count_data)

if __name__ == "__main__":
    main_sync()
