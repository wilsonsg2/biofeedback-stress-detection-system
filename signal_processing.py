import numpy as np
import time
from collections import deque


class HeartRateMonitor:
    def __init__(self,
                 baseline_window=30,
                 smoothing_window=5,
                 threshold_percent=0.15,
                 cooldown_seconds=120):

        self.baseline_window = baseline_window
        self.smoothing_window = smoothing_window
        self.threshold_percent = threshold_percent
        self.cooldown_seconds = cooldown_seconds

        self.baseline_buffer = deque(maxlen=baseline_window)
        self.smoothing_buffer = deque(maxlen=smoothing_window)

        self.baseline = None
        self.last_trigger_time = 0

    def update(self, hr_value):

        # Update smoothing buffer
        self.smoothing_buffer.append(hr_value)
        smoothed_hr = np.mean(self.smoothing_buffer)

        # Build baseline
        self.baseline_buffer.append(smoothed_hr)

        if len(self.baseline_buffer) == self.baseline_window:
            self.baseline = np.mean(self.baseline_buffer)

        # If baseline not ready yet
        if self.baseline is None:
            return False, smoothed_hr, None

        current_time = time.time()

        if smoothed_hr > self.baseline * (1 + self.threshold_percent):
            if current_time - self.last_trigger_time > self.cooldown_seconds:
                self.last_trigger_time = current_time
                return True, smoothed_hr, self.baseline

        return False, smoothed_hr, self.baseline