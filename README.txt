# Web Vulnerability Scanner

## 🚀 First Documentation 🚀  

## 😕 What the heck is a ferox anyway?

Ferox is short for Ferric Oxide. Ferric Oxide, simply put, is rust. The name rustbuster was taken, so I decided on a
variation. 🤷

## 🤔 What's it do tho?

`feroxbuster` is a tool designed to perform [Forced Browsing](https://owasp.org/www-community/attacks/Forced_browsing).

Forced browsing is an attack where the aim is to enumerate and access resources that are not referenced by the web
application, but are still accessible by an attacker.

`feroxbuster` uses brute force combined with a wordlist to search for unlinked content in target directories. These
resources may store sensitive information about web applications and operational systems, such as source code,
credentials, internal network addressing, etc...

This attack is also known as Predictable Resource Location, File Enumeration, Directory Enumeration, and Resource
Enumeration.

## ⏳ Quick Start

This section will cover the minimum amount of information to get up and running with feroxbuster. Please refer the the [documentation](https://epi052.github.io/feroxbuster-docs/docs/), as it's much more comprehensive.

### 💿 Installation

There are quite a few other [installation methods](https://epi052.github.io/feroxbuster-docs/docs/installation/), but these snippets should cover the majority of users. 

#### Kali 

If you're using kali, this is the preferred install method. Installing from the repos adds a [**ferox-config.toml**](https://epi052.github.io/feroxbuster-docs/docs/configuration/ferox-config-toml/) in `/etc/feroxbuster/`, adds command completion for bash, fish, and zsh, includes a man page entry, and installs `feroxbuster` itself. 

```
sudo apt update && sudo apt install -y feroxbuster
```

#### Linux (32 and 64-bit) & MacOS

Install to a particular directory
```
curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh | bash -s $HOME/.local/bin
```

Install to current working directory
```
curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh | bash
```

#### MacOS via Homebrew 

```
brew install feroxbuster
```

#### Windows x86_64

```
Invoke-WebRequest https://github.com/epi052/feroxbuster/releases/latest/download/x86_64-windows-feroxbuster.exe.zip -OutFile feroxbuster.zip
Expand-Archive .\feroxbuster.zip
.\feroxbuster\feroxbuster.exe -V
```

#### Windows via Winget

```
winget install epi052.feroxbuster
```

#### Windows via Chocolatey

```
choco install feroxbuster
```

#### All others 

Please refer the the [documentation](https://epi052.github.io/feroxbuster-docs/docs/).

### Updating feroxbuster (new in v2.9.1)

```
./feroxbuster --update
```

## 🧰 Example Usage

Here are a few brief examples to get you started.  Please note, feroxbuster can do a **lot more** than what's listed below.  As a result, there are **many more** examples, with **demonstration gifs** that highlight specific features, in the [documentation](https://epi052.github.io/feroxbuster-docs/docs/).

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
