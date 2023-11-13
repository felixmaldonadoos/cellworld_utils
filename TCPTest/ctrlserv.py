from json_cpp import *
import tcp_messages as tcp
from cellworld import Location
from time import sleep

class MyService(tcp.MessageServer):

    def __init__(self):
        tcp.MessageServer.__init__(self)
        self.router.add_route("stop_server", self.stop_service)
        self.router.add_route("set_destination", self.echo, JsonString)
        
    def echo(self, msg):
        print("Hi", msg)
    
    def stop_service(self):
        print("stopping")
        self.stop()
        print("stopped")

    # def send_broadcast(self, loc):
    #     print(f"Sending Broadcast Again {loc}")
    #     service.broadcast_subscribed(message=tcp.Message(header="prey_step", 
    #                          body=loc))

def new_connection(self):
    print("new_connection")

service = MyService()
service.allow_subscription = True

service.on_new_connection = new_connection
print ("starting")
service.start(port=6000)
print ("started")

# sleep(10)
# locations = []
# locations.append(Location(0.0, 0.5))
# locations.append(Location(0.5, 0.5))
# locations.append(Location(0.5, 1.0))
# locations.append(Location(0.5, 0.0))
# locations.append(Location(0.5, 0.5))

# for i in range(0,5):
#     print(f"Broadcast: {i}")
#     service.send_broadcast(locations[i])
#     sleep(5)

service.join()