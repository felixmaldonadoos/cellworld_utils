from json_cpp import *
import tcp_messages as tcp
from cellworld import Location, Step, Episode, World
from time import sleep

# https://drive.google.com/drive/u/1/folders/1SJ0CZyrv3_Fax3SkkDf42P43zVBP3Ful

# --- Load an Experiment ---
occlusions = "21_05"
world = World.get_from_parameters_names('hexagonal', "canonical", occlusions)
vr_occlusion_locations = []
print("# Cell locations: ", len(world.implementation.cell_locations))
epi = Episode.load_from_file("PEEK_20230201_1340_FMM13_21_05_RT3_episode_000.json")
traj_obj = epi.trajectories.split_by_agent()
prey_traj = traj_obj['prey']
pred_traj = traj_obj['predator']

print("# prey points: ", len(prey_traj))
print("# pred points: ", len(pred_traj))

# --- Fake Server ---  
class MyService(tcp.MessageServer):

    def __init__(self):
        tcp.MessageServer.__init__(self)
        self.router.add_route("test2", self.test2, str)
        self.router.add_route("test3", self.test3)
        self.router.add_route("stop_server", self.stop_service)
        self.router.add_route("set_destination", self.echo, JsonString)
        self.router.add_route("get_world_implementation", self.add_cells)
        
        # self.router.add_route("send_again", self.send_broadcast)

    # @staticmethod
    # @json_parameters_function()
    # def accum(v: int, v2: int):
    # For adding in the locations of the occlusions into the VR World
    def add_cells(self):
        return JsonString(world.cells)

    #     return v + v2
    def echo(self, msg):
        print("Set Destination: ", msg)
    
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

    def send_broadcast_prey(self, step):
        print(f"Sending prey_step {step.location}")
        service.broadcast_subscribed(message=tcp.Message(header="prey_step", 
                             body=step))
    
    def send_broadcast_pred(self, step):
        # print(f"Sending predator_step {step.location}")
        print(step)
        service.broadcast_subscribed(message=tcp.Message(header="predator_step", body=step))

def new_connection(self):
    print("new_connection")

service = MyService()
service.allow_subscription = True

service.on_new_connection = new_connection
print ("starting")
service.start(port=6001)
print ("started service.")
input("Press any key to start broadcast: ")
print("Starting broadcast in 3 seconds...")
sleep(3)
prey_steps = []

fs_camera = 90; # 90 Hz sampling
dt = 1/fs_camera; 
for i in range(0,len(prey_traj)):
    print(f"Broadcast: {i}")
    # service.send_broadcast_prey(prey_traj[i])
    service.send_broadcast_pred(pred_traj[i])
    sleep(dt) # roughly 90 Hz 
print("\nFinished broadcast. Calling service.join().")
service.join()
