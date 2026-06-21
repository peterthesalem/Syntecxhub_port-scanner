import socket
import threading
from datetime import datetime

print("=" * 50)
print("      SYNTECXHUB TCP PORT SCANNER")
print("=" * 50)

target = input("Enter target IP or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Invalid hostname or IP address.")
    exit()

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target_ip} from port {start_port} to {end_port}")
print(f"Started at: {datetime.now()}\n")

log_file = open("scan_results.txt", "w")

lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))

        with lock:
            if result == 0:
                message = f"[OPEN] Port {port}"
            else:
                message = f"[CLOSED] Port {port}"

            print(message)
            log_file.write(message + "\n")

        sock.close()

    except socket.timeout:
        with lock:
            message = f"[TIMEOUT] Port {port}"
            print(message)
            log_file.write(message + "\n")

    except Exception as e:
        with lock:
            message = f"[ERROR] Port {port}: {e}"
            print(message)
            log_file.write(message + "\n")

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

log_file.close()

print("\nScan Complete!")
print("Results saved to scan_results.txt") 
