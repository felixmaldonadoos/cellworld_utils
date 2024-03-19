from json_cpp import *
import tcp_messages as tcp
from time import sleep
from cellworld import Location, Step, Episode, World

def echo(self, msg):
    print("Set Destination: ", msg)

# client = tcp.MessageClient()
# if client.connect("127.0.0.1", 4510):
#     print("connected")
#     if client.subscribe():
#         print("Subscribed!")
    
#     client.router.add_route("send_step",echo, JsonString)
    
#     while True:
        
#         broadcast = client.send_message(
#         client.send_message(tcp.Message(
#                 header="send_step",
#                 body=Step())))
        
#         # broadcast = client.messages.get_message(header="prey_step")
#         if broadcast != None:
#             print("Found Message")
#             values = broadcast.get_body()
#             print(values)

#         sleep(0.1)
# else:
#     print("failed to connect")


class TrackingServiceClient(tcp.MessageClient):
    def __init__(self):
        super().__init__()
        self.router.add_route("send_step", self.echo, JsonString)
        self.port = 4510
        self.ip = "127.0.0.1"

    def run(self):
        if self.connect("127.0.0.1", 4510):
            print("connected")
            if self.subscribe():
                print("Subscribed!")
            while True:
                self.send_message(tcp.Message(
                        header="send_step",
                        body=Step()))
                sleep(0.1)
        else:
            print("failed to connect")
    def echo(self,msg):
        print(f"Sent: {msg}")

TrackingServiceClient().run()