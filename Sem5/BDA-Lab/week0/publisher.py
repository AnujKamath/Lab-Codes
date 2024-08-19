import socket
import threading

# Global list to keep track of connected subscribers
subscribers = []

def publish_messages():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12346))
    server_socket.listen()

    print("Publisher is listening on localhost:12345")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Subscriber connected from {address}")
        
        # Add subscriber socket to list
        subscribers.append(client_socket)

        # Start a new thread to handle each subscriber independently
        threading.Thread(target=handle_subscriber, args=(client_socket,)).start()

def handle_subscriber(client_socket):
    try:
        while True:
            # Receive message from subscriber (though in pub-sub, we won't use this)
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received message from subscriber: {message}")

    except Exception as e:
        print(f"Error handling subscriber: {e}")
    finally:
        # Remove subscriber socket from list upon disconnect
        subscribers.remove(client_socket)
        client_socket.close()
        print("Subscriber disconnected")

def start_publisher():
    try:
        while True:
            message = input("Enter message to publish (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            
            # Broadcast message to all subscribers
            for subscriber_socket in subscribers:
                try:
                    subscriber_socket.sendall(message.encode('utf-8'))
                except:
                    # Handle exception (e.g., broken connection)
                    subscribers.remove(subscriber_socket)

    except Exception as e:
        print(f"Error in publisher: {e}")
    finally:
        # Close all subscriber sockets upon exit
        for subscriber_socket in subscribers:
            subscriber_socket.close()

        print("Publisher socket closed")

if __name__ == "__main__":
    threading.Thread(target=publish_messages).start()
    start_publisher()
