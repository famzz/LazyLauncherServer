import socket
import subprocess

spotify_path = "C:\\Users\\Fahim\\AppData\\Roaming\\Spotify\\Spotify.exe"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 1337))

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

print("The IP address for this computer is {}".format(get_ip()))

while True:
    message, address = server_socket.recvfrom(1024)
    message = message.decode('utf-8')
    print(message)
    if message == "Spotify":
        subprocess.Popen([spotify_path])
