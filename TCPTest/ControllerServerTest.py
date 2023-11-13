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
        # self.router.add_route("send_again", self.send_broadcast)

    # @staticmethod
    # @json_parameters_function()
    # def accum(v: int, v2: int):

    #     return v + v2
    def echo(self, msg):
        print("Set Destination: ", msg)
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

    def send_broadcast_prey(self, loc):
        print(f"Sending prey_step {loc}")
        service.broadcast_subscribed(message=tcp.Message(header="prey_step", 
                             body=loc))
    
    def send_broadcast_pred(self, loc):
        print(f"Sending predator_step {loc}")
        service.broadcast_subscribed(message=tcp.Message(header="predator_step", body=loc))

def new_connection(self):
    print("new_connection")

service = MyService()
service.allow_subscription = True

service.on_new_connection = new_connection
print ("starting")
service.start(port=6000)
print ("started")
sleep(10)
prey_locations = []
prey_locations.append(Location(0.0, 0.5))
prey_locations.append(Location(0.5, 0.5))
prey_locations.append(Location(0.5, 1.0))
prey_locations.append(Location(0.5, 0.0))
prey_locations.append(Location(0.5, 0.5))

predator_locations = []
predator_locations.append(Location(1.0, 0.5))
predator_locations.append(Location(0.0, 0.5))
predator_locations.append(Location(0.5, 0.0))
predator_locations.append(Location(0.5, 1.0))
predator_locations.append(Location(1.0, 0.5))

for i in range(0,5):
    print(f"Broadcast: {i}")
    service.send_broadcast_prey(prey_locations[i])
    service.send_broadcast_pred(predator_locations[i])
    sleep(5)
    
service.join()
