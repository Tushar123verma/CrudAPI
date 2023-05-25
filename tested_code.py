from opcua import Client
from opcua.crypto import uacrypto
import traceback
import time
while True:
    def uaConnect():
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
            #client.disconnect()
            #return "Done"
        except Exception as e:
            print (traceback.format_exc())
            #client.disconnect()
            return "Done"
        #finally:
            #client.disconnect()

    if __name__ == "__main__":
        uaConnect()