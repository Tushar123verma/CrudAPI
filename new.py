from opcua import Client
import time


def connect_to_server(url):
    client = Client(url)
    client.connect()
    print("Connected to server")
    return client


def disconnect_from_server(client):
    client.disconnect()
    print("Disconnected from server")


if __name__ == '__main__':
    server_url = "opc.tcp://172.20.46.31:4840/"
    client2 = connect_to_server(server_url)
    node = client2.get_node("ns=4;s=ESD_PB_1")
    #value = node.get_value()
    #print("Variable value:", value)
    while True:
        value = node.get_value()
        print("Variable value:", value)
        try:
            client2.connect()
            print("Reconnected to server")
            break  # Exit the loop if reconnection is successful
        except Exception as e:
            print("Reconnection failed. Retrying in 5 seconds...")
            time.sleep(5)
        value = node.get_value()
        print("Variable value:", value)

    disconnect_from_server(client2)
