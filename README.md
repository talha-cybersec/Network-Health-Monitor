# Smart Network Health Analyzer

A Python desktop application that checks how healthy your connection to a given host is. It measures TCP latency and jitter, checks DNS resolution, and turns the results into a single **0–100 health score** with a plain-language verdict.

> Built as a Computer Networks course project. The project report and presentation are in [`docs/`](docs/).

## ✨ Features

- **TCP latency measurement:** opens 6 TCP connections to the target (port 80) and records the connect time of each in milliseconds
- **Jitter analysis:** computes the standard deviation of the latency samples to show how stable the connection is
- **DNS check:** confirms the hostname resolves to an IP address
- **Health score (0–100):** penalises high average latency (>80 ms, >150 ms) and high jitter (>20 ms, >50 ms)
- **Verdict:** `GOOD`, `MODERATE` or `POOR`, with a recommendation (e.g. "Gaming, Streaming, Browsing OK")
- **Visual output:** bar chart of every latency sample, drawn in the Tkinter GUI

## 🛠 Tech Stack

| Component | Used for |
|---|---|
| Python 3 | Core language |
| Tkinter | Desktop GUI and bar chart (canvas) |
| `socket` | TCP connections and DNS resolution |
| `time`, `statistics` | Timing, mean latency and jitter |

It uses only the Python standard library, so there's nothing extra to install.

## 🚀 Getting Started

```bash
git clone https://github.com/talha-cybersec/Network-Health-Monitor.git
cd Network-Health-Monitor
python network_health_gui.py
```

Enter a host such as `google.com` and click **Analyze Network**.

> On Linux, Tkinter may need to be installed separately: `sudo apt install python3-tk`

## ⚙️ How the Score Works

| Condition | Penalty |
|---|---|
| Average latency > 150 ms | −40 |
| Average latency > 80 ms | −20 |
| Jitter > 50 ms | −30 |
| Jitter > 20 ms | −15 |

Score ≥ 80 → **GOOD** · 50–79 → **MODERATE** · < 50 → **POOR**

## 📁 Project Structure

```
Network-Health-Monitor/
├── network_health_gui.py   # Application (network tests + GUI)
├── docs/
│   ├── CN-PROJECT.pdf      # Project report
│   └── CN-Project.pptx     # Presentation slides
└── README.md
```

## 🔮 Possible Improvements

- Measure DNS resolution time as well as success or failure
- Add ICMP ping and packet-loss percentage
- Run tests in a background thread so the GUI stays responsive
- Export results to CSV

## 👤 Author

**Muhammad Talha** · [@talha-cybersec](https://github.com/talha-cybersec)
