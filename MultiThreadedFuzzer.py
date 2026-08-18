import requests
import sys
import threading
from queue import Queue

if len(sys.argv) == 2:
    target_url = sys.argv[1].rstrip("/")
else:
    target_url = input("Please enter target URL(e.g., http://example.com): ").rstrip("/")

wordlist = [
    "admin",
    "login",
    "dashboard",
    "config",
    "backup",
    "db",
    "robots.txt"
]
path_queue = Queue()

for path in wordlist:
   path_queue.put(path)

def fuzzer_worker():
   while not path_queue.empty():
       path = path_queue.get()
       url = f"{target_url}/{path}" 

       try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"[+] Found: {url} (Status Code: {response.status_code})")
        elif response.status_code == 403:
            print(f"[-] Forbidden: {url} (Status Code: {response.status_code})") 
       except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
       finally:
        path_queue.task_done()

thread_count = 10
for _ in range(thread_count):
    t = threading.Thread(target=fuzzer_worker)
    t.daemon = True
    t.start()

path_queue.join()
print("\n[*] Fuzzing completed.")
