# Lab 4 Part 1: Temperature Monitoring System

## Author
**Gabriel Marquez**

---

## 📌 Objectives

- Simulate real-time temperature readings from multiple sensors.
- Compute average temperatures continuously.
- Display all temperature data live on the console without clearing the screen.
- Use threading and synchronization techniques for safe and concurrent operations.

---

## 🛠️ Tools and Concepts Used

- **Python**: Main programming language.
- **Threading**: For running sensors, processor, and display functions concurrently.
- **Queue**: For thread-safe transfer of temperature data between producer and consumer threads.
- **RLock** and **Condition**: For synchronizing shared data access and controlling timed updates.

---

## ✅ Output Snapshot

```
Current temperatures: Latest Temperatures: Sensor 0: 31°C Sensor 1: 40°C Sensor 2: 33°C
Sensor 0 Average: 39.25°C
Sensor 1 Average: 26.33°C
Sensor 2 Average: 20.33°C
```


---

## ⚙️ Task Breakdown

### 3.a. Sensor Simulation
- Implemented `simulate_sensor()` to generate random temperatures (15–40°C) every second.
- Updates the `latest_temperatures` dictionary.

### 3.b. Data Processing
- Implemented `process_temperatures()` to consume data from a shared queue.
- Continuously calculates moving averages and updates `temperature_averages`.

### 3.c. Thread Integration
- Spawned separate threads for each sensor and the processing function.
- Used `daemon=True` to ensure threads exit when the main program exits.

### 3.d. Display Logic
- `initialize_display()` prints the base layout of the temperature monitor.
- `update_display()` refreshes only the values (not the entire screen) using `\r` and cursor movement.

### 3.e. Synchronization
- Used `RLock` to safely access and modify shared dictionaries.
- Used `Condition` to time display and average updates accurately.

### 3.f. Main Program
- Created the queue and shared data structures in the main script.
- Launched all threads.
- Display is updated every **5 seconds**, while sensor readings are updated every **1 second**.

---

## 🧠 Questions & Answers

### 1) Which synchronization mechanism did you use for each task?

| Task                        | Synchronization Mechanism         |
|-----------------------------|-----------------------------------|
| Updating sensor readings    | `RLock` for safe dictionary access |
| Processing data from queue  | No lock (queue is thread-safe)    |
| Updating averages           | `RLock`                           |
| Display refresh control     | `Condition` for timed updates     |

---

### 2) Why did the professor not ask you to compute metrics?

The purpose of this lab is to focus on **concurrent programming techniques** rather than model evaluation or performance analysis. Since this is a **simulation**, the values are random, and computing performance metrics would not be meaningful in this context. The key objective is to correctly **synchronize concurrent data streams and display output in real time**, which is a foundational skill in distributed and parallel systems.

---
