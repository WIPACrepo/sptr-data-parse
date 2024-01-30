# parse_sptr.py

import json
import re
import sys

def extract_transfers(data):
    transfers = {
        "projects": [],
    }

    pattern = r"(.{7}) transferred (\d+) files for : ([\d.]+) (KB|MB|GB)"
    matches = re.findall(pattern, data, re.DOTALL | re.MULTILINE)
    for match in matches:
        project, count, volume, unit = match
        data_volume = float(volume)
        if unit == 'KB':
            data_volume = data_volume * 1024
        elif unit == 'MB':
            data_volume = data_volume * (1024 ** 2)
        elif unit == 'GB':
            data_volume = data_volume * (1024 ** 3)
        else:
            raise Exception(f"I don't know what the heck a '{unit}' is")
        data_volume = int(data_volume)
        transfers["projects"].append({
            "project": f"{project}",
            "count": f"{count}",
            "volume": f"{data_volume}",
        })

    pattern = r"Total transfers from Pole: ([\d.]+) (KB|MB|GB)"
    matches = re.findall(pattern, data, re.DOTALL | re.MULTILINE)
    for match in matches:
        volume, unit = match
        data_volume = float(volume)
        if unit == 'KB':
            data_volume = data_volume * 1024
        elif unit == 'MB':
            data_volume = data_volume * (1024 ** 2)
        elif unit == 'GB':
            data_volume = data_volume * (1024 ** 3)
        else:
            raise Exception(f"I don't know what the heck a '{unit}' is")
        data_volume = int(data_volume)
        transfers["total"] = {
            "volume": f"{data_volume}",
        }

    return transfers

def pretty_print_json(data):
    return json.dumps(data, indent=4)

def main_sync():
    # Sample data (replace this with your actual data)
    data = """
    ==============================================================
    Transfers from South Pole to WSC
    Date: Mon 01/01/24
    ==============================================================
    The following projects sent files from Pole:
    A-107-S transferred 1 files for : 861.28 MB (8% of Note 1)
    A-111-S transferred 1 files for : 21.71 KB (0% of Note 1)
    A-128-S transferred 19 files for : 26.85 MB (8% of Note 1)
    A-149-S transferred 35 files for : 2.06 GB (8% of Note 1)
    A-333-S transferred 144 files for : 110.89 GB (105% of Note 1)
    A-365-S transferred 53 files for : 43.84 GB (104% of Note 1)
    A-379-S transferred 117 files for : 178.98 GB (143% of Note 1)
    O-257-S transferred 1 files for : 15.51 MB (1% of Note 1)

    Note 1 = NSF Approved Data Transport Volume
    ==============================================================
    Total transfers from Pole: 336.66 GB
    ==============================================================
    """
    data = sys.stdin.read()

    transfers = extract_transfers(data)
    pretty_json = pretty_print_json(transfers)
    print(pretty_json)

if __name__ == "__main__":
    main_sync()
