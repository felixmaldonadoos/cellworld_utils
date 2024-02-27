from json_cpp import *
import tcp_messages as tcp
from cellworld import Location, Step, Episode, World
from time import sleep

class MyExperimentService(tcp.MessageServer):
    def __init__(self, ip: str = "127.0.0.1"):
        super().__init__(ip)
        self.router.add_route("stop_server", self.stop_service)
        self.on_new_connection = self.on_new_connection_notify

    def on_new_connection_notify():
        print("New connection")
    

def main():
    print("Running.")
    service = MyExperimentService(); 
    service.allow_subscription = True


if __name__ == "__main__":
    main()