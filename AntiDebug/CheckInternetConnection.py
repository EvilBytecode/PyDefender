import socket

def check_connection():
    try:
        socket.create_connection(("google.com", 80), timeout=5)
        return True, None
    except socket.error as ex:
        error_message = f"Error checking internet connection: {ex}"
        print(f"[DEBUG] {error_message}")
        return False, Exception(error_message)