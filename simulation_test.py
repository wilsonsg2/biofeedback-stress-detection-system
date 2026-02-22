import random
import time

from signal_processing import HeartRateMonitor
from breathing import start_breathing
from logger import log_data


monitor = HeartRateMonitor(
    baseline_window=30,
    smoothing_window=5,
    threshold_percent=0.15,
    cooldown_seconds=120
)

print("Simulating heart rate data...\n")

for _ in range(300):

    # Simulate normal resting HR
    hr = random.randint(65, 75)

    # Occasionally simulate stress spike
    if random.random() < 0.1:
        hr = random.randint(95, 115)

    triggered, smoothed_hr, baseline = monitor.update(hr)

    print(f"Raw HR: {hr} | Smoothed HR: {round(smoothed_hr,2)} | Baseline: {baseline}")

    log_data(smoothed_hr, baseline, triggered)

    if triggered:
        start_breathing(cycles=5)

    time.sleep(1)