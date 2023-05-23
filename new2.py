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

def read_variable(client, node_id):
    node = client.get_node(node_id)
    value = node.get_value()
    print("Variable value:", value)

if __name__=='__main__':
# Server URL and Node ID of the variable you want to read or modify
    server_url = "opc.tcp://<server_ip_address>:<port>"
    variable_node_id = "<variable_node_id>"

    # Connect to the server
    client = connect_to_server(server_url)

    # Read the variable
    read_variable(client, variable_node_id)

    # Disconnect from the server
    disconnect_from_server(client)

    # Simulating disconnecting the WAN cable
    time.sleep(5)

    # Reconnect to the server
    while True:
        try:
            client.connect()
            print("Reconnected to server")
            break
        except Exception as e:
            print("Reconnection failed. Retrying in 5 seconds...")
            time.sleep(5)

    # Read the variable after reconnecting
    read_variable(client, variable_node_id)

    # Disconnect from the server
    disconnect_from_server(client)
