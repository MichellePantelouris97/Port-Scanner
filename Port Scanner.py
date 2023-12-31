import pyfiglet
import sys
import socket
import concurrent.futures
from datetime import datetime

# Create ascii banner
def ascii_banner():
    # Generate ASCII banner
    ascii_banner = pyfiglet.figlet_format("Port Scanning")
    print(ascii_banner)

# Scanned ports
def ports_scanned(target, port_start, port_end):
    try:
        print("-" * 50)
        print("Scanning Target: " + target)
        print("Scanning started at: " + str(datetime.now()))
        print("-" * 50)

          # Ports are scanned in parallel using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(ports_scanned, target, port) for port in range(start_port, end_port + 1)]
            concurrent.futures.wait(futures)

        # Ports are scanned in the specified range
        for port in range(port_start, port_end + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # Check if the port is open
            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\nExiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\nThe Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\nThe server Is Not Responding !!!!")
        sys.exit()

if __name__ == "__main__":
    ascii_banner()

    # Define target and port range
    if len(sys.argv) == 4:
        target = socket.gethostbyname(sys.argv[1])
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
    else:
        print("Invalid arguments. Usage: python script.py <destination> <beginning_port> <ending_port>")
        sys.exit()

    ports_scanned(target, start_port, end_port)
