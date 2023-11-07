from json_cpp import *
import tcp_messages as tcp
from cellworld import Location
from time import sleep

class MyService(tcp.MessageServer):

    def __init__(self):
        tcp.MessageServer.__init__(self)
        # self.router.add_route("accum", self.accum, JsonObject)
        self.router.add_route("test2", self.test2, str)
        self.router.add_route("test3", self.test3)
        self.router.add_route("stop_server", self.stop_service)
        self.router.add_route("set_destination", self.echo, JsonString)
        self.router.add_route("send_again", self.send_broadcast)

    # @staticmethod
    # @json_parameters_function()
    # def accum(v: int, v2: int):

    #     return v + v2
    def echo(self, msg):
        print("Hi", msg)
        # print(f"Destination {dest.x, dest.y}")
    
    # @staticmethod
    # @json_parameters_function()
    def test3(self, a, b, c):
        return a + b + c
    
    def stop_service(self):
        print("stopping")
        self.stop()
        print("stopped")

    def test2(self, v):
        print("test2", v)
        return 5

    def send_broadcast(self, loc):
        print(f"Sending Broadcast Again {loc}")
        service.broadcast_subscribed(message=tcp.Message(header="prey_step", 
                             body=loc))

def new_connection(self):
    print("new_connection")

service = MyService()
service.allow_subscription = True

service.on_new_connection = new_connection
print ("starting")
service.start(port=5000)
print ("started")
sleep(10)
locations = []
locations.append(Location(0.0, 0.5))
locations.append(Location(0.5, 0.5))
locations.append(Location(0.5, 1.0))
locations.append(Location(0.5, 0.0))
locations.append(Location(0.5, 0.5))

for i in range(0,5):
    print(f"Broadcast: {i}")
    service.send_broadcast(locations[i])
    sleep(5)

# print("Num Messages", len(service.messages))
# if len(service.messages) != 0:
#     for i in range(len(service.messages)):
#         print(service.messages[i])

service.join()



# service.broadcast(message=tcp.Message(header="Hello", body="teehee"))

# jo = JsonObject.load('{"v":1,"v2":3}')
# print(service.accum(jo))


# if client.connect("129.105.69.134", 9999):
# if client.connect("192.168.137.228", 9999):