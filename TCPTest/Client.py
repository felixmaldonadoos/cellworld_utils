from json_cpp import *
import tcp_messages as tcp
from time import sleep
from cellworld import Location

client = tcp.MessageClient()
if client.connect("127.0.0.1", 5000):
# if client.connect("129.105.249.94", 9000):
    print("connected")
    sleep(2)
    if client.subscribe():
        print("Subscribed!")
    # print(client.send_request("method1"))
    # print(client.send_request(tcp.Message(header="test3", body=JsonObject(a=1, b=2, c=3))))
    # print("message test")
    # print(client.send_message(tcp.Message(header="test1")))
    # sleep(3)
    # print("request test")
    #
    # print(client.send_request(tcp.Message(header="test2", body="hello")))
    print(client.messages)
    while(client.messages == []):
        # client.send_message(tcp.Message(header="send_again", body=""))
        broadcast = client.messages.get_message(header="prey_step")
        if broadcast != None:
            print("Found Message")
            values = broadcast.get_body(Location)
            print(values)
            break
    # print(client.messages)
    sleep(2)
    print("Client telling Server to Stop")
    client.send_message("stop_server")
    sleep(2)
    client.disconnect()
else:
    print("failed to connect")

# 192.168.137.51