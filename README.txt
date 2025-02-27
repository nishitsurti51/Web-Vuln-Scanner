# Web Vulnerability Scanner

A web vulnerability scanner using **Nmap** and **Feroxbuster**, built with **Flask** and **Flask-SocketIO**.

## 🚀 Features
- Runs **Nmap** and **Feroxbuster** sequentially.
- Streams **real-time scan output** to a web-based UI.
- Allows **stopping scans** anytime.
- Uses **Flask-SocketIO** for **live updates**.

---

## 🛠️ Installation Guide

### 1️⃣ Install Python (if not installed)
- Download and install **Python (3.8 or higher)** from:  
  👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Verify installation:
  ```
  python --version
  ```

### 2️⃣ Install Nmap
- **Windows**:
  - Download from: 👉 [https://nmap.org/download.html](https://nmap.org/download.html)
  - Install and **remember the installation path** (e.g., `C:\Program Files (x86)\Nmap\nmap.exe`).
- **Linux (Debian-based)**:
  ```
  sudo apt update && sudo apt install nmap -y
  ```
- **Verify Installation**:
  ```
  nmap --version
  ```git remote add origin YOUR_GITHUB_REPO_URL


### 3️⃣ Install Feroxbuster
- **Windows**:
  - Install Rust (required for Feroxbuster) from 👉 [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install)
  - Then install Feroxbuster:
    ```
    cargo install feroxbuster
    ```
  - **Verify Installation**:
    ```
    feroxbuster --version
    ```
- **Linux**:
  ```
  sudo apt install feroxbuster -y
  ```

### 4️⃣ Download SecLists (Wordlists for Feroxbuster)
- **Windows**:
  - Download from 👉 [https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)
  - Extract it to a folder, e.g., `C:\Users\YourUser\SecLists`
- **Linux**:
  ```
  sudo apt install seclists -y
  ```

---

## 🔧 Configuration
Before running the project, update the paths in `app.py` if necessary:

```python
NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"
FEROXBUSTER_PATH = r"C:\Users\YourUser\.cargo\bin\feroxbuster.exe"
SECLIST_PATH = r"C:\Users\YourUser\SecLists\Discovery\Web-Content\raft-medium-directories.txt"
```

---

## 💻 Run the Web Scanner
### 1️⃣ Clone the repository
```
git clone https://github.com/YOUR_GITHUB_USERNAME/web-vuln-scanner.git
cd web-vuln-scanner
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Start the application
```
python app.py
```
- Open **http://localhost:5000** in your browser.

---

## 🛑 Stop the Scan
- Click the **"Stop Scan"** button in the UI.
- Or manually stop the server: `CTRL + C`

---

## 🛠️ Technologies Used
- **Python**
- **Flask**
- **Nmap**
- **Feroxbuster**
- **Flask-SocketIO**

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

### ✅ Now Your Scanner is Ready! 🚀  
Let me know if you need any modifications or enhancements! 🔥
