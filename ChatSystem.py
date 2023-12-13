import datetime
import socket
import threading


class Server:
    def __init__(self, ip:str, port:int,log:str="server.log"):
        self.ip = ip
        self.port = port
        self.log = log
        self.clients = []
       
      
    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(5)
        self.write_to_log(f"Server started on {self.ip}:{self.port}")
        while True:
            client, addr = self.server.accept()
            self.write_to_log(f"New connection from {addr}")
            threading.Thread(target=self.accept_connections, args=(client,)).start()
    
    def write_to_log(self, msg:str):
        with open(self.log, "a") as file:
            #get aktuelle datum und zeit
            date = datetime.datetime.now()
            #schreibe in log
            print(f"[{date.strftime('%d.%m.%Y %H:%M:%S')}] {msg}"  )
            file.write(f"[{date.strftime('%d.%m.%Y %H:%M:%S')}] {msg}\n")
            
    def accept_connections(self, client:socket.socket):
        self.clients.append(client)
        self.write_to_log(f"New connection from {client}")
        while True:
            # try:
            #     data = client.recv(1024)
            #     if data:
            #         self.write_to_log(f"Received data from {client}: {data}")
            #         for c in self.clients:
            #             if c != client:
            #                 c.send(data)
            #     else:
            #         self.write_to_log(f"Connection to {client} closed")
            #         self.clients.remove(client)
            #         client.close()
            #         break
            # except:
            #     self.write_to_log(f"Connection to {client} closed")
            #     self.clients.remove(client)
            #     client.close()
            #     break
            

class Client:
    def __init__(self, ip:str, port:int,name:str,log:str="client.log"):
        self.ip = ip
        self.port = port
        self.name = name
        self.log = log
        self.server = None
        self.connected = False
        
    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.ip, self.port))
        self.connected = True
        self.write_to_log(f"Connected to {self.ip}:{self.port}")
    
    def write_to_log(self, msg:str):
        with open(self.log, "a") as file:
            date = datetime.datetime.now()
            print(f"[{date.strftime('%d.%m.%Y %H:%M:%S')}] {msg}")
            file.write(f"[{date.strftime('%d.%m.%Y %H:%M:%S')}] {msg}\n")


if __name__ == "__main__":
    server = Server("127.0.0.1",6666,"server.log")
    client = Client("127.0.0.1",6666,"client.log")
    server.start()
    client.connect()
