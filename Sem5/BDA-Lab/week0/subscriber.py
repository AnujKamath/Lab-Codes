import socket

def subscribe_messages():
    try:
        subscriber_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        subscriber_socket.connect(('localhost', 12346))
        print("Connected to publisher")

        while True:
            message = subscriber_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received message: {message}")

    except Exception as e:
        print(f"Error in subscriber: {e}")
    finally:
        subscriber_socket.close()
        print("Subscriber socket closed")

if __name__ == "__main__":
    subscribe_messages()
