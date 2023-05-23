from opcua import Client
import traceback
import time
# Create an OPC UA client instance
client = Client("opc.tcp://172.20.46.31:4840/")
def uaclient():
    try:
        # Connect to the OPC UA server
        client.set_user("BPCL")
        client.set_password("adm")
        client.connect()
        print("Connected to OPC UA server")

        connected = True
        # Perform necessary operations while connected
        resp = client.get_node("ns=4;s=ESD_PB_1")

        if (connected == True):
            while True:
                client_value = resp.get_value()
                print(client_value)
                time.sleep(2)
            client.disconnect()
            print("Disconnected from OPC UA server")

        # Reconnect to the OPC UA server
        else:
            time.sleep(2)
            client.connect()
            print("Reconnected to OPC UA server")

            # Perform further operations after reconnecting
            resp = client.get_node("ns=4;s=ESD_PB_1")
            while True:
                client_value = resp.get_value()
                print(client_value)
                time.sleep(2)

    except Exception as e:
        print (traceback.format_exc())
        #client.disconnect()

    finally:
        # Ensure that the client connection is closed properly
        client.disconnect()

if __name__=='__main__':
    uaclient()