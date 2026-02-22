import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from signal_processing import HeartRateMonitor
from logger import log_data


# -----------------------------
# Initialize Monitor
# -----------------------------

monitor = HeartRateMonitor(
    baseline_window=30,
    smoothing_window=5,
    threshold_percent=0.15,
    cooldown_seconds=120
)


# -----------------------------
# Data Storage
# -----------------------------

raw_values = []
smoothed_values = []
baseline_values = []
trigger_points_x = []
trigger_points_y = []

start_time = time.time()


# -----------------------------
# Heart Rate Simulation
# -----------------------------

def generate_hr():
    hr = random.randint(65, 75)

    # 10 percent chance of stress spike
    if random.random() < 0.1:
        hr = random.randint(95, 115)

    return hr


# -----------------------------
# Animation Update Function
# -----------------------------

def update(frame):

    current_time = time.time() - start_time

    hr = generate_hr()

    triggered, smoothed_hr, baseline = monitor.update(hr)

    raw_values.append(hr)
    smoothed_values.append(smoothed_hr)
    baseline_values.append(baseline if baseline is not None else None)

    log_data(smoothed_hr, baseline, triggered)

    if triggered:
        trigger_points_x.append(current_time)
        trigger_points_y.append(smoothed_hr)
        print("Trigger detected at time:", round(current_time, 2))

    ax.clear()

    ax.plot(smoothed_values, label="Smoothed HR")

    if baseline is not None:
        ax.plot(baseline_values, linestyle="--", label="Baseline")

    ax.scatter(
        [i for i in range(len(trigger_points_y))],
        trigger_points_y,
        marker="o"
    )

    ax.set_title("Real-Time Heart Rate Monitoring")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Heart Rate (BPM)")
    ax.legend()

    return


# -----------------------------
# Plot Setup
# -----------------------------

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()