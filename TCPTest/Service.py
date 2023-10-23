from json_cpp import *
import tcp_messages as tcp

class MyService(tcp.MessageServer):

    def __init__(self):
        tcp.MessageServer.__init__(self)
        # self.router.add_route("accum", self.accum, JsonObject)
        self.router.add_route("test1", self.test1)
        self.router.add_route("test2", self.test2, str)
        self.router.add_route("test3", self.test3)
        self.router.add_route("stop_please", self.stop_service)

    # @staticmethod
    # @json_parameters_function()
    # def accum(v: int, v2: int):

    #     return v + v2

    
    # @staticmethod
    # @json_parameters_function()
    def test3(self, a, b, c):
        return a + b + c

    def test1(self, m):
        print("test1", m)

    def stop_service(self):
        print("stopping")
        self.stop()
        print("stopped")

    def test2(self, v):
        print("test2", v)
        return 5



def new_connection(self):
    print("new_connection")

service = MyService()

service.on_new_connection = new_connection
print ("starting")
service.start(port=9999)
print ("started")

service.join()
# jo = JsonObject.load('{"v":1,"v2":3}')
# print(service.accum(jo))


# if client.connect("129.105.69.134", 9999):
# if client.connect("192.168.137.228", 9999):