from opcua import Client
import traceback
import time
# Create an OPC UA client instance
#client = Client("opc.tcp://172.20.46.31:4840/")
while True:
    def uaclient():
        client = Client("opc.tcp://172.20.46.31:4840/")
        client.set_user("BPCL")
        client.set_password("adm")
        is_connected = False
        while not is_connected:
            try:
                # Connect to the OPC UA server
                client.connect()
                is_connected=True

                # Perform necessary operations while connected
                resp = client.get_node("ns=4;s=ESD_PB_1")
                while is_connected:
                    client_value = resp.get_value()
                    print(client_value)
                    time.sleep(2)

            except Exception as e:
                is_connected= False
                client.disconnect()
                print (traceback.format_exc())
                time.sleep(5)
    if __name__=='__main__':
        uaclient()