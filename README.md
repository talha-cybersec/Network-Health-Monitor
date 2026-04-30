# Smart Network Health Analyzer
A Python-based desktop application for real-time network performance analysis.

## 📌 Project Overview
The **Smart Network Health Analyzer** evaluates the quality and performance of a computer network for a specific domain name (e.g., google.com). It provides users with a clear understanding of their internet connection health through critical networking parameters.

## 🚀 Key Features
* **TCP Latency Measurement:** Establishes multiple TCP connections to measure round-trip time (RTT) in milliseconds.
* **Jitter Analysis:** Determines the amount of change between successive latency measurements to evaluate stability.
* **DNS Resolution Performance:** Converts domain names to IP addresses and measures the resolution delay.
* **Network Health Score:** Automatically computes a score from 0 to 100 based on latency, jitter, and DNS success.
* **Visual Dashboard:** Displays results through a simple GUI and categorizes quality as Good, Average, or Poor.

## 🛠 Tools & Technologies
* **Language:** Python 3
* **GUI Library:** Tkinter
* **Graphing:** Matplotlib (for latency variation bar graphs)
* **Modules:** `socket` (DNS/TCP), `time` (delays), and `statistics` (averages/jitter)

## 🏗 How it Works
1. **User Input:** Enter a domain name and click 'Analyze Network'.
2. **Backend Logic:** The system performs DNS resolution and runs multiple TCP latency tests.
3. **Calculation:** The app calculates the average latency and jitter.
4. **Output:** A final health score and a bar graph of latency variations are displayed.

