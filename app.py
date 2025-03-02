import os
import subprocess
import re
import psutil  # Required to kill process tree
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Paths
NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"
FEROXBUSTER_PATH = r"C:\Users\nishi\.cargo\bin\feroxbuster.exe"
SECLIST_PATH = r"C:\Users\nishi\SecLists-master\Discovery\Web-Content\raft-medium-directories.txt"

processes = []  # List to track running processes

def run_command(command, scan_type):
    """Runs a command and streams real-time output."""
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        processes.append(process)

        full_output = []  # Collect full output for Nmap

        while True:
            output = process.stdout.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                formatted_output = format_output(output.strip(), scan_type)
                if formatted_output:
                    socketio.emit("update", {"scan_type": scan_type, "data": formatted_output})
                    full_output.append(formatted_output)

        process.wait()
        processes.remove(process)

        return full_output  # Return full output for further processing

    except Exception as e:
        socketio.emit("update", {"scan_type": scan_type, "data": f"Error: {e}"})
        return []

def format_output(line, scan_type):
    """Formats the output for better readability."""
    if scan_type == "Feroxbuster":
        match = re.search(r"(\d{3})\s+(\w+)\s+\d+l\s+\d+w\s+\d+c\s+(https?://\S+)", line)
        if match:
            status_code, method, url = match.groups()
            return f"{status_code} {method} {url}"
    elif scan_type == "Nmap":
        return line  # Return full Nmap output
    return None

def kill_process_tree(pid):
    """Kills the process and all its child processes (fix for Feroxbuster)."""
    try:
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):  # Kill all child processes
            child.terminate()
        parent.terminate()  # Kill parent process
    except psutil.NoSuchProcess:
        pass  # Process already stopped

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("start_scan")
def start_scan(data):
    """Sequentially runs Nmap and then Feroxbuster."""
    target_url = data["url"]

    # Start Nmap first
    socketio.emit("update", {"scan_type": "Nmap", "data": f"Starting Nmap scan on {target_url}..."} )
    nmap_results = run_command([NMAP_PATH, "-sV", "-sC", target_url], "Nmap")

    # Once Nmap is done, start Feroxbuster
    socketio.emit("update", {"scan_type": "Feroxbuster", "data": f"Starting Feroxbuster scan on {target_url}..."} )
    run_command([FEROXBUSTER_PATH, "-u", target_url, "-k", "-w", SECLIST_PATH], "Feroxbuster")

    socketio.emit("scan_complete")  # Mark scan as complete

@socketio.on("stop_scan")
def stop_scan():
    """Stops all running scans."""
    for process in processes:
        try:
            kill_process_tree(process.pid)  # ✅ Stops Feroxbuster and its child processes
            process.wait()
        except Exception as e:
            print(f"Error stopping process: {e}")
    processes.clear()
    socketio.emit("scan_complete")

if __name__ == "__main__":
    socketio.run(app, debug=True)
