import socket
import time
import statistics
import tkinter as tk
from tkinter import messagebox

# ---------------- NETWORK TEST FUNCTIONS ---------------- #

def tcp_latency_test(host, port=80, attempts=6):
    latencies = []
    for _ in range(attempts):
        try:
            start = time.time()
            sock = socket.create_connection((host, port), timeout=3)
            end = time.time()
            sock.close()
            latencies.append(round((end - start) * 1000, 2))
        except:
            pass
    return latencies


def dns_test(host):
    try:
        socket.gethostbyname(host)
        return "Resolved (DNS OK)"
    except:
        return "DNS Failed"


def calculate_health(avg_latency, jitter):
    score = 100

    if avg_latency > 150:
        score -= 40
    elif avg_latency > 80:
        score -= 20

    if jitter > 50:
        score -= 30
    elif jitter > 20:
        score -= 15

    return max(score, 0)


# ---------------- GUI ACTION ---------------- #

def analyze_network():
    host = entry.get().strip()

    if not host:
        messagebox.showerror("Input Error", "Please enter a target host")
        return

    output.delete("1.0", tk.END)
    canvas.delete("all")

    output.insert(tk.END, f"Analyzing network for: {host}\n\n")

    latencies = tcp_latency_test(host)

    if not latencies:
        output.insert(tk.END, "❌ Network unreachable or host blocked\n")
        return

    avg_latency = round(statistics.mean(latencies), 2)
    jitter = round(statistics.pstdev(latencies), 2)
    dns_result = dns_test(host)
    health_score = calculate_health(avg_latency, jitter)

    if health_score >= 80:
        status = "GOOD"
        recommendation = "✔ Gaming, Streaming, Browsing OK"
    elif health_score >= 50:
        status = "MODERATE"
        recommendation = "✔ Browsing OK\n✖ Gaming not recommended"
    else:
        status = "POOR"
        recommendation = "✖ Poor network quality"

    # TEXT OUTPUT
    output.insert(tk.END, f"TCP Avg Latency : {avg_latency} ms\n")
    output.insert(tk.END, f"Jitter          : {jitter} ms\n")
    output.insert(tk.END, f"DNS Result      : {dns_result}\n\n")
    output.insert(tk.END, f"Network Health Score: {health_score}/100\n\n")
    output.insert(tk.END, "Analysis Summary:\n")
    output.insert(tk.END, recommendation + "\n")

    status_label.config(text=f"Network Status: {status}")

    # DRAW LATENCY BARS (VISUAL DEMO)
    bar_width = 40
    x = 20
    for latency in latencies:
        bar_height = min(latency * 2, 200)
        canvas.create_rectangle(
            x, 250 - bar_height, x + bar_width, 250, fill="blue"
        )
        canvas.create_text(x + 20, 250 - bar_height - 10,
                           text=f"{latency}ms", font=("Arial", 8))
        x += 60


# ---------------- GUI SETUP ---------------- #

root = tk.Tk()
root.title("Smart Network Health Analyzer")
root.geometry("700x600")

tk.Label(root, text="Target Host (e.g. google.com):",
         font=("Arial", 12)).pack(pady=5)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Analyze Network",
          command=analyze_network,
          font=("Arial", 12)).pack(pady=10)

status_label = tk.Label(root, text="Network Status: ---",
                        font=("Arial", 14, "bold"), fg="orange")
status_label.pack(pady=10)

canvas = tk.Canvas(root, width=600, height=260, bg="white")
canvas.pack(pady=10)

output = tk.Text(root, height=10, width=80, font=("Consolas", 10))
output.pack(pady=10)

root.mainloop()
