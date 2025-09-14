# 🖧 Network Scanner

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)

A powerful, lightweight Python-based network scanner that discovers devices on your local network, performs vendor identification through MAC address lookup, and conducts comprehensive port scanning. The tool provides both real-time console output and generates detailed CSV reports for network analysis.

</div>

---

## 🌟 Key Features

- **🔍 Automatic Device Discovery**: Scans the entire `/24` subnet using ARP requests
- **🏷️ Vendor Identification**: Identifies device manufacturers through MAC address lookup
- **🔌 Port Scanning**: Checks common ports (21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3389, 8080)
- **📊 Multiple Output Formats**: Console table display and timestamped CSV export
- **⚡ Smart Dependency Management**: Automatically installs missing dependencies
- **🛡️ Cross-Platform Compatibility**: Works on Windows, Linux, and macOS
- **📈 Performance Optimized**: Efficient scanning with configurable timeouts

---

## 🛠️ Prerequisites

### System Requirements
- **Python**: 3.7 or higher
- **Privileges**: Administrative/root access (required for raw socket operations)
- **Network**: Active network connection

### Supported Operating Systems
- Windows 10/11 (with Administrator privileges)
- Linux distributions (Ubuntu, CentOS, Debian, etc.)
- macOS 10.14+ (Mojave and later)

---

## 📦 Installation

### Method 1: Clone Repository (Recommended)
```bash
git clone https://github.com/Sahil01010011/network-scanner.git
cd network-scanner
```

### Method 2: Download Source
Download the latest release from the [releases page](https://github.com/Sahil01010011/network-scanner/releases) and extract the files.

### Dependencies
The script automatically handles dependency installation, but you can install them manually if needed:

```bash
pip install -r requirements.txt
```

**Required packages:**
- [`scapy`](https://scapy.net/) - Packet manipulation library
- [`mac-vendor-lookup`](https://pypi.org/project/mac-vendor-lookup/) - MAC address vendor identification
- [`requests`](https://docs.python-requests.org/) - HTTP library for vendor lookups
- [`psutil`](https://pyutil.readthedocs.io/) - System and process utilities

---

## 🚀 Usage

### Basic Usage

#### On Linux/macOS:
```bash
sudo python3 scanner.py
```

#### On Windows:
```cmd
# Run Command Prompt as Administrator
python scanner.py
```

### Advanced Usage Examples

#### Scanning Specific Network Range
```python
# Modify the script to scan a custom range
network_range = "192.168.1.0/24"  # Custom subnet
```

#### Custom Port Scanning
```python
# Add custom ports to scan
custom_ports = [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 993, 995, 3389, 5432, 5900, 8080, 8443]
```

---

## 📊 Sample Output

### Console Output
```
[*] Scanning the network: 192.168.1.0/24

[+] Detailed Device Scan Results:
IP Address      MAC Address          Vendor                        Open Ports          
-------------------------------------------------------------------------------------
192.168.1.1     aa:bb:cc:dd:ee:ff    NETGEAR                       22, 80, 443
192.168.1.15    11:22:33:44:55:66    Apple, Inc.                   22, 5900
192.168.1.25    ff:ee:dd:cc:bb:aa    Intel Corporate               None
192.168.1.100   ab:cd:ef:12:34:56    Raspberry Pi Foundation       22, 80

[+] Scan results saved to network_scan_results_20241214_143022.csv
```

### CSV Output
The generated CSV file contains structured data perfect for further analysis:
```csv
IP Address,MAC Address,Vendor,Open Ports
192.168.1.1,aa:bb:cc:dd:ee:ff,NETGEAR,"22, 80, 443"
192.168.1.15,11:22:33:44:55:66,"Apple, Inc.","22, 5900"
192.168.1.25,ff:ee:dd:cc:bb:aa,Intel Corporate,None
```

---

## ⚙️ Configuration

### Customizing Scan Parameters

You can modify the following parameters in `scanner.py`:

```python
# Modify timeout for faster/slower scans
sock.settimeout(0.5)  # Increase for slower networks

# Customize port list
common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3389, 8080]

# Change network range detection
network_range = f"{'.'.join(local_ip.split('.')[:-1])}.0/24"
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### **"Permission denied" errors**
- **Linux/macOS**: Run with `sudo python3 scanner.py`
- **Windows**: Run Command Prompt as Administrator

#### **Module not found errors**
The script automatically installs missing dependencies. If manual installation is needed:
```bash
pip install scapy mac-vendor-lookup requests psutil
```

#### **No devices found**
- Ensure you're connected to a network
- Check if your firewall is blocking the scan
- Try running with administrator/root privileges
- Verify your network configuration

#### **Slow scanning**
- Adjust the timeout value in the `scan_ports()` function
- Reduce the port list for faster scans
- Check your network connection speed

#### **"Unknown" vendor results**
- Some MAC addresses may not be in the vendor database
- Private/locally administered MAC addresses will show as "Unknown"
- Ensure internet connectivity for vendor lookups

---

## 🔒 Security Considerations

### Legal and Ethical Usage
- **✅ Authorized Use Only**: Only scan networks you own or have explicit permission to test
- **✅ Educational Purpose**: Ideal for learning network security concepts
- **✅ Network Administration**: Perfect for IT professionals managing networks
- **❌ Unauthorized Scanning**: Do not scan networks without permission

### Best Practices
- Always obtain proper authorization before scanning
- Use responsibly and respect network policies
- Consider the impact on network performance
- Keep scan results confidential and secure

---

## 🤝 Contributing

We welcome contributions to improve the Network Scanner! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Submit detailed bug reports with reproduction steps
- 💡 **Feature Requests**: Suggest new features or improvements
- 🔧 **Code Contributions**: Submit pull requests with enhancements
- 📖 **Documentation**: Improve documentation and examples

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a detailed description

### Code Standards
- Follow PEP 8 style guidelines
- Add comments for complex functionality
- Include error handling for network operations
- Test on multiple platforms when possible

---

## 📈 Roadmap

### Planned Features
- [ ] **GUI Interface**: Cross-platform graphical user interface
- [ ] **Advanced Port Scanning**: Service detection and version identification
- [ ] **Network Mapping**: Visual network topology generation
- [ ] **Scheduled Scanning**: Automated periodic network scans
- [ ] **Alert System**: Notifications for new devices or changes
- [ ] **API Integration**: REST API for external tool integration

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

---

## 🙏 Acknowledgments

- **Scapy Team**: For the excellent packet manipulation library
- **MAC Vendor Database**: For providing vendor identification services
- **Python Community**: For the robust ecosystem and libraries
- **Contributors**: Thanks to all contributors who help improve this project

---

## 📞 Support

### Getting Help
- **Issues**: [GitHub Issues](https://github.com/Sahil01010011/network-scanner/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Sahil01010011/network-scanner/discussions)
- **Documentation**: Check this README and inline code comments

### Contact
- **GitHub**: [@Sahil01010011](https://github.com/Sahil01010011)
- **Repository**: [network-scanner](https://github.com/Sahil01010011/network-scanner)

---

<div align="center">

**⭐ Star this repository if you find it useful!**

Made with ❤️ by [Sahil01010011](https://github.com/Sahil01010011)

</div>

---

## ⚠️ Disclaimer

This tool is provided for educational and authorized testing purposes only. Users are responsible for ensuring they have proper authorization before scanning any network. The developers assume no liability for misuse of this tool or any damages that may result from its use. Always comply with local laws and regulations regarding network scanning and security testing.


