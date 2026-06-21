import socket

target = input("Enter target IP or hostname: ")

with open("scan_results.txt", "w") as file:

    print(f"\nScanning {target}...\n")

    for port in range(1, 101):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            message = f"Port {port} is OPEN"
            print(message)
            file.write(message + "\n")

        sock.close()

print("\nResults saved to scan_results.txt")
