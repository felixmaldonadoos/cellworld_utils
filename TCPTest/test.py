import socket

def main():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('127.0.0.1', 6000)
    print(f"Connecting to {server_address[0]} port {server_address[1]}")
    client_socket.connect(server_address)
    print("here")
    try:
        # Continuously receive data from the server and print it
        while True:
            data = client_socket.recv(1024)
            print(f"Received: {data.decode('utf-8')}")
            if not data:
                # If no data is received, break out of the loop
                print("No data from server, closing connection.")
                break
    finally:
        # Clean up the connection
        client_socket.close()
        print("Disconnected from server.")

if __name__ == "__main__":
    main()