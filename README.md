# **so1icit's ARP Spoofer**

A simple Python script to perform ARP spoofing using **Scapy**.  
The script continuously sends spoofed ARP packets to a target device and the gateway, allowing you to intercept or manipulate network traffic. Press `CTRL+C` to stop the spoofing and restore the ARP tables.

---

## ⚠️ Warning
**Use this tool responsibly and only on networks where you have explicit permission. Unauthorized use can be illegal.**

---

## ✨ Features
- 🔥 **ARP Spoofing:** Intercepts traffic between a target device and the gateway.
- 🔄 **Auto-Restoration:** Automatically restores ARP tables when the script is stopped.
- 🔧 **Built with Scapy:** Leverages Scapy for flexible packet manipulation.

---

## ⚙️ Requirements
- Python **3.x**
- **Scapy** (Install via: `pip install scapy`)
- Root privileges (`sudo`)

---

## 📚 Installation
```bash
git clone https://github.com/trxycs/so1icitx-arp-spoofer.git
cd arp-spoofer
```
## 🚀 Usage    
```bash
sudo python3 arp_spoofer.py <target_ip> <gateway_ip>
```
### Example:  
```bash
sudo python3 arp_spoofer.py 192.168.1.108 192.168.1.1
```
## 📝 License  
This project is licensed under the **MIT License**.  

---
