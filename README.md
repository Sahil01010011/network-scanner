# 🖧 Network Scanner

A lightweight Python-based network scanner that discovers devices on your local network, identifies their vendors using MAC address lookup, and checks for open common ports. Results are displayed in the console and exported to a CSV file for later analysis.

---

## 📌 Features
- Automatic installation of required dependencies if missing.
- Detects the local IP and scans the entire `/24` subnet.
- Discovers devices using ARP requests.
- Identifies device vendor from MAC address.
- Scans common ports (21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3389, 8080).
- Saves results with timestamp into a CSV file.

---

## ⚙️ Requirements
- Python **3.7+**
- Administrative/root privileges (required for ARP scanning)

### Dependencies
The script automatically checks and installs:
- [`scapy`](https://scapy.net/)
- [`mac-vendor-lookup`](https://pypi.org/project/mac-vendor-lookup/)
- [`requests`](https://docs.python-requests.org/)

You can also install them manually:
```bash
pip install scapy mac-vendor-lookup requests

## 🚀 Usage

### Clone this repository
```bash
git clone https://github.com/your-username/network-scanner.git
cd network-scanner
python scanner.py
sudo python3 scanner.py


The script will:

Detect your local IP

Scan all devices in the subnet

Print results in a table

Save results to a timestamped CSV file (network_scan_results_YYYYMMDD_HHMMSS.csv)


### OUTPUT
[+] Detailed Device Scan Results:
IP Address      MAC Address          Vendor                        Open Ports
-------------------------------------------------------------------------------------
192.168.1.1     00:1A:2B:3C:4D:5E    Cisco Systems                 80, 443
192.168.1.5     11:22:33:44:55:66    Intel Corporation             None


🔒 Permissions

Windows: Run from an elevated Command Prompt (Administrator).

Linux/macOS: Run with sudo.

⚠️ Disclaimer

This tool is intended for educational and authorized use only.
Do not scan networks you do not own or have explicit permission to analyze.
Unauthorized scanning may violate local laws.


