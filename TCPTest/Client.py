from json_cpp import *
import tcp_messages as tcp
from time import sleep
from cellworld import Location

client = tcp.MessageClient()
if client.connect("127.0.0.1", 6000):
    print("connected")
    if client.subscribe():
        print("Subscribed!")
        
    while True:
        # print(client.send_request(tcp.Message(header="test2", body="hello")))
        # print(client.messages)
        # client.send_message(tcp.Message(header="send_again", body=""))
        broadcast = client.messages.get_message(header="prey_step")
        if broadcast != None:
            print("Found Message")
            values = broadcast.get_body()
            print(values)
        # sleep(2)
        # print("Client telling Server to Stop")
        # client.send_message("stop_server")
        sleep(0.1)
        
    # client.disconnect()
else:
    print("failed to connect")

# 192.168.137.51