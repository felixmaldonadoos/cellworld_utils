from json_cpp import *
import tcp_messages as tcp
from time import sleep
from cellworld import Location, Step, Episode, World
import cellworld_experiment_service as ces
from cellworld_tracking import TrackingClient as tc 

class TrackingServiceClient(tcp.MessageClient):
    def __init__(self):
        super().__init__()
        self.router.add_route("send_step", self.echo, JsonString)
        self.port = 4510
        self.ip = "127.0.0.1"
        self.b_send_message = False; 
    def run(self):
        if self.connect("127.0.0.1", 4510):
            print("[TS] connected")
            if self.subscribe():
                print("[TS] Subscribed!")
            # if (self.b_send_message):
            #     while True:
            #         self.send_message(tcp.Message(
            #                 header="send_step",
            #                 body=Step()))
            #         sleep(0.1)
        else:
            print("[TS] failed to connect")
    def echo(self,msg):
        print(f"[TS] Sent: {msg}")

class ExperimentServiceClient(ces.ExperimentClient):
    def __init__(self):
        super().__init__()
        self.set_request_time_out(100)
        self.router.add_route("predator_step",self.echo, JsonString)
        self.on_episode_started = self.on_episode_started_es
        print(f"[ES] Port: {self.port}")

    def on_episode_started_es(self, msg:ces.EpisodeStartedMessage):
            print(f"[ES] Episode Started: {msg}")

    def pre_start(self)->None:
        res = self.connect("127.0.0.1")
        print(f"[ES] connection ")
        response_start_experiment = self.start_experiment(suffix="test",prefix="test",world_configuration="hexagonal",world_implementation="canonical",
                        occlusions="21_05", subject_name="alexander",duration=100,
                        rewards_cells=None,rewards_orientations=None)

        print(f"[ES] Start experiment response: {response_start_experiment}")

        try:
            response_start_episode = self.start_episode(experiment_name=response_start_experiment.experiment_name,
                                        rewards_sequence=None)
            print(f"[ES] Start episode response: {response_start_episode}")
        except TimeoutError:
            print("[ES] Start episode timed out")
            return
    
    def run(self)->None:
        self.pre_start()
        # todo: start sending steps 
    
    def echo(self,msg)->None:
        print(f"Sent: {msg}")

TrackingServiceClient().run()
ExperimentServiceClient().run()


"""
1. start experiment -> Name
2. start episode(Name)
3. 


"""