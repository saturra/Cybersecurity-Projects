import socket
import sys
from queue import Queue

if len(sys.argv) == 2:
    target_ip = sys.argv[1]
else:
    target_ip = input("Please enter target IP address: ")

print(f"\n[*] Scanning target: {target_ip}.....\n")

ports_to_check = [21, 22, 80, 443, 8080]
for port in ports_to_check:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print (f"[+]Port {port:<5} is OPEN")
        else:
            print(f"[-]Port {port:<5} is CLOSED")

    except Exception as e:
        print(f"Error on port {port}: {e}")
    finally:
        s.close()





