# import modules used to create tcp socket 
import socket
import json
import os
from json_cpp import *
import tcp_messages as tcp
from time import sleep
from cellworld import Location, Step, Episode, World
import cellworld_experiment_service as ces
from cellworld_tracking import TrackingClient as tc 

# create a basic tcp socket client connecting to port 4566
import socket

class Client:
    def __init__(self) -> None:
        # ts = tcp.MessageClient()
        # ts.ip = "127.0.0.1"
        # ts.connect(ts.ip, 4566)
        # es = ces.ExperimentClient()
        # es.connect()
        # es.router.add_route("get_cell_locations")

        pass

if __name__ == "__main__":
    client = Client()
    # client.es.send_request("get_cell_locations","21_05")
