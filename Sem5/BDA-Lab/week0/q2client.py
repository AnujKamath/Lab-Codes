import socket

def send_file_to_server(file_path):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12346))
        print("Connected to the server")

        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            print("File content read")

        client_socket.sendall(file_content.encode('utf-8'))
        print("File content sent to the server")

        # Send an empty byte to indicate end of transmission
        client_socket.shutdown(socket.SHUT_WR)

        word_count = int(client_socket.recv(1024).decode('utf-8'))
        print(f"Word count received: {word_count}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Client socket closed")

if __name__ == "__main__":
    file_path = 'example.txt'
    send_file_to_server(file_path)
