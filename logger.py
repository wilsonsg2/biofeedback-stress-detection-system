import csv
from datetime import datetime


def log_data(hr, baseline, triggered):

    with open("session_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            hr,
            baseline if baseline is not None else "NA",
            triggered
        ])