import socket
import sys
from queue import Queue
import threading

if len(sys.argv) == 2:
    target_ip = sys.argv[1]
else:
    target_ip = input("Please enter target IP address: ")

print(f"\n[*] Scanning target: {target_ip}.....\n")

port_queue = Queue()
for port in range(1, 1025):
    port_queue.put(port)

def worker():
    while not port_queue.empty():
        port = port_queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))

            if result == 0:
                print(f"[+]Port {port:<5} is OPEN")
          

        except Exception as e:
            pass
        finally:
            s.close()
            port_queue.task_done()

thread_count = 100
for _ in range(thread_count): 
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

port_queue.join()
print("\n[*] Scanning completed.")