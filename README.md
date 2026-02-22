# Real-Time Biofeedback Stress Detection System

## Overview

This project implements a closed-loop physiological monitoring system that detects elevated heart rate and triggers a guided breathing intervention.

The system processes pulse oximeter heart rate data, applies signal smoothing and baseline modeling, and detects stress events using a relative threshold framework.

Currently validated using simulated heart rate input. Bluetooth Low Energy integration with a pulse oximeter is in progress.

---

## System Architecture

Input:
Heart rate data (simulated or BLE pulse oximeter)

Processing:
- Moving average smoothing
- Rolling baseline calibration
- Relative threshold detection
- Cooldown control logic

Output:
- Triggered breathing intervention
- Real-time visualization
- CSV data logging

---

## Features

- Modular Python architecture
- Real-time matplotlib visualization
- Adaptive baseline modeling
- Threshold-based detection
- Structured CSV logging
- Designed for BLE integration

---

## Project Structure

signal_processing.py  
breathing.py  
logger.py  
simulation_test.py  
live_plot_simulation.py  

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- Bleak (BLE integration in development)

---

## Future Work

- Live BLE heart rate streaming
- Calibration phase refinement
- Heart rate variability analysis
- GUI implementation
- Experimental validation study
