import scapy.all as scapy
import sys
import subprocess
import socket
import os
import ipaddress
import psutil
import csv
from datetime import datetime

# Required packages
required_packages = {
    "scapy": "scapy",
    "mac_vendor_lookup": "mac-vendor-lookup",
    "requests": "requests" # Keeping requests in case it's used elsewhere or for future expansion
}

# --- Package Installation Check ---
# This part ensures necessary libraries are installed.
for module, package in required_packages.items():
    try:
        __import__(module)
    except ImportError:
        print(f"'{module}' not found. Installing '{package}'...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except Exception as e:
            print(f"Error installing {package}: {e}. Please install manually: pip install {package}")
            sys.exit(1) # Exit if essential packages can't be installed

# Re-import MacLookup after potential installation
from mac_vendor_lookup import MacLookup

# --- Network Utilities ---
def get_local_ip():
    """Get your local IP address"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80)) # Connect to an external address to get local IP
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1" # Fallback if no network connection
    finally:
        s.close()
    return ip

def scan_network(ip_range):
    """Scan the network using ARP requests and return IP-MAC mappings"""
    print(f"[*] Scanning the network: {ip_range}")
    try:
        arp_request = scapy.ARP(pdst=ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        devices = []
        for element in answered_list:
            devices.append({"ip": element[1].psrc, "mac": element[1].hwsrc})
        return devices
    except Exception as e:
        print(f"Error during network scan: {e}")
        print("Make sure you run this script with administrative/root privileges for network scanning (e.g., sudo python script.py).")
        return []

def get_vendor(mac_address):
    """Get the vendor name for a given MAC address"""
    try:
        vendor = MacLookup().lookup(mac_address)
        return vendor
    except KeyError:
        return "Unknown"
    except Exception as e:
        return f"Error getting vendor: {e}"

def scan_ports(ip_address, common_ports=[21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3389, 8080]):
    """Scan common ports on a given IP address"""
    open_ports = []
    print(f"[*] Scanning common ports on {ip_address}...")
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Shorter timeout for quicker scans
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# --- Main Execution ---
if __name__ == "__main__":
    local_ip = get_local_ip()
    network_range = f"{'.'.join(local_ip.split('.')[:-1])}.0/24" # Assuming a /24 subnet

    # Perform network scan
    connected_devices = scan_network(network_range)

    scan_results = []
    print("\n[+] Detailed Device Scan Results:")
    print("{:<15} {:<20} {:<30} {:<20}".format("IP Address", "MAC Address", "Vendor", "Open Ports"))
    print("-" * 85)

    for device in connected_devices:
        ip = device["ip"]
        mac = device["mac"]
        vendor_name = get_vendor(mac)
        open_ports = scan_ports(ip)
        open_ports_str = ", ".join(map(str, open_ports)) if open_ports else "None"

        scan_results.append({
            "IP Address": ip,
            "MAC Address": mac,
            "Vendor": vendor_name,
            "Open Ports": open_ports_str
        })
        print("{:<15} {:<20} {:<30} {:<20}".format(ip, mac, vendor_name, open_ports_str))

    # --- Save Results to CSV ---
    if scan_results:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"network_scan_results_{timestamp}.csv"
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ["IP Address", "MAC Address", "Vendor", "Open Ports"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for row in scan_results:
                    writer.writerow(row)
            print(f"\n[+] Scan results saved to {filename}")
        except Exception as e:
            print(f"\n[-] Error saving results to CSV: {e}")
    else:
        print("\nNo devices found to save results.")