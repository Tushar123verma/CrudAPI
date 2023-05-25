import socket
from time import sleep
from opcua import Client
import time
import traceback

# configure socket and connect to server
#clientSocket = socket.socket()

# keep track of connection status
#connected = True
#print("connected to server")

while True:
    clientSocket = socket.socket()
    connected = True
    print("connected to server")
    def uaconnect():
    # attempt to send and receive wave, otherwise reconnect
        client = Client("opc.tcp://172.20.46.31:4840/")
        try:
            client.set_user("BPCL")
            client.set_password("adm")
            client.connect()
            resp = client.get_node("ns=4;s=ESD_PB_1")
            while True:
                client_value = resp.get_value()
                print(client_value)
                time.sleep(2)
        except Exception as e:
            # set connection status and recreate socket
            print(traceback.format_exc())
            connected = False
            clientSocket = socket.socket()
            print("connection lost... reconnecting")
            while not connected:
                # attempt to reconnect, otherwise sleep for 2 seconds
                try:
                    clientSocket.connect('opc.tcp://172.20.46.31:4840')
                    connected = True
                    print("re-connection successful")
                except socket.error:
                    sleep(2)

        clientSocket.close()
    if __name__ == "__main__":
        uaconnect()