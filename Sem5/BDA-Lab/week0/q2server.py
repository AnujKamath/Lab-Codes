import socket

def count_words(file_content):
    words = file_content.split()
    return len(words)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12346))
    server_socket.listen()

    print("Server is listening on localhost:12345")
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        try:
            file_content = b''
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file_content += data
            print("File content received from the client")

            word_count = count_words(file_content.decode('utf-8'))
            client_socket.sendall(str(word_count).encode('utf-8'))
            print("Word count sent to the client")

        finally:
            client_socket.close()
            print("Client socket closed")

if __name__ == "__main__":
    start_server()
