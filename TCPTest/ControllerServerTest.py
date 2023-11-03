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

    def send_broadcast(self):
        print("Sending Broadcast Again")
        service.broadcast_subscribed(message=tcp.Message(header="prey_step", 
                             body=Location(800.0, 200.0)))

def new_connection(self):
    print("new_connection")

service = MyService()
service.allow_subscription = True

service.on_new_connection = new_connection
print ("starting")
service.start(port=5000)
print ("started")
sleep(10)
for i in range (0,50):
    service.send_broadcast()
    sleep(2)

service.join()

# service.broadcast(message=tcp.Message(header="Hello", body="teehee"))

# jo = JsonObject.load('{"v":1,"v2":3}')
# print(service.accum(jo))


# if client.connect("129.105.69.134", 9999):
# if client.connect("192.168.137.228", 9999):