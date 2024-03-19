from json_cpp import *
import tcp_messages as tcp
from time import sleep
from cellworld import Location, Step, Episode, World
import cellworld_experiment_service as ces

class ExperimentServiceClient(ces.ExperimentClient):
    def __init__(self):
        super().__init__()
        self.router.add_route()
        self.set_tracking_service_ip("127.0.0.1")
    
    def run(self)->None:
        self.connect()
        return None
    def echo(self,msg):
        print(f"Sent: {msg}")

ExperimentServiceClient().run()