from json_cpp import *
import tcp_messages as tcp
from time import sleep

client = tcp.MessageClient()
if client.connect("127.0.0.1", 9999):
    print("connected")
    sleep(2)
    print(client.send_request(tcp.Message(header="test3", body=JsonObject(a=1, b=2, c=3))))
    # print("message test")
    # print(client.send_message(tcp.Message(header="test1")))
    # sleep(3)
    # print("request test")
    #
    # print(client.send_request(tcp.Message(header="test2", body="hello")))
    sleep(2)
    print("stopping")
    print(client.send_message(tcp.Message(header="stop_please")))
    sleep(2)
    client.disconnect()
else:
    print("failed to connect")
