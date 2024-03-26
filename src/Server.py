import cellworld_experiment_service as ces
import cellworld_tracking as ct
import tcp_messages as tcp
import cellworld as cw
import sys
import json
import errno

class Server:
    def __init__(self) -> None:
        print("=== BotEvade Server ===")
        self.tracking_service   = ServerTrackingService()
        self.experiment_service = ServerExperimentService()
        
    def start(self)->bool:
        if not self.tracking_service.run():
            self.log("ERROR! Failed to start Tracking Service.")
            return False
        if not self.experiment_service.run():
            self.log("ERROR! Failed to start Experiment Service.")
            return False
        return True
    
    def stop(self)->None:
        self.experiment_service.stop()
        self.tracking_service.stop()
        self.exit()
        return
    
    def exit(self)->None:
        self.log("Exiting program")
        sys.exit()

    def log(self, msg, *args):
        additional_info = ', '.join(str(arg) for arg in args)
        if additional_info:
            print(f"[Server] {msg}. Info: {additional_info}")
        else:
            print(f"[Server] {msg}.")

class ServerTrackingService(ct.TrackingService):
    def __init__(self) -> None:
        ct.TrackingService.__init__(self)
        # super().__init__(self)
        self.ip                  = "127.0.0.1"
        self.on_new_connection   = self.on_connection_ts
        # self.send_step           = self.send_step_ts # ask german how to override a method
        
    def run(self)->bool:
        # print('here')
        res = False
        try:
            res = self.start(port=4510)
            self.log("Started service.",res)
        except OSError:
            self.log("lol server is still refreshing")
        return res

    def on_connection_ts(self,msg)->None:
        self.log("New connection.",msg)
    
    def process_step(self, step:ces.Step)->ces.Step: # not being called but i get a message back? 
        print("processing")
        step = ces.Step()
        step.agent_name = "predator"
        return step

    def send_step_ts(self,step:ces.Step=None)->None:
        self.log("received from:",step.agent_name)
        # call gabbie script and gabbie.agent_name + _step = pred_step ## not implemented yet
        step = self.process_step(step)
        self.ts.broadcast_subscribed(ces.Message(step.agent_name + "_step", step))
        print("after")
        return
    
    def log(self, msg, *args):
        additional_info = ', '.join(str(arg) for arg in args)
        if additional_info:
            print(f"[TS] {msg}. Info: {additional_info}")
        else:
            print(f"[TS] {msg}.")
    
    def echo(self,msg):
        self.log("message received:",msg)
        
class ServerExperimentService(ces.ExperimentService):
    def __init__(self):
        super().__init__()
        self.on_new_connection      = self.on_new_connection_es
        self.on_experiment_started  = self.on_experiment_started_es
        self.on_experiment_finished = self.on_experiment_finished_es
        self.on_episode_started     = self.on_episode_started_es
        self.on_episode_finished    = self.on_episode_finished_es
        self.on_experiment_resumed  = self.on_experiment_resumed_es        
        self.set_tracking_service_ip("127.0.0.1")
        pass

    def run(self)->bool:
        res = self.start()
        self.log(f"Started server", res)
        self.join()
        print('after run ') ## never fires 
        return res

    def on_new_connection_es(self,msg:tcp.Connection = None)->None:
        self.log("New connection", msg.state)

    def on_episode_started_es(self,msg:ces.StartEpisodeRequest = None)->None:
        self.log("episode started",msg)
      
    def on_episode_finished_es(self,msg:bool = None)->None:
        self.log("Episode finished.", msg)

    def on_experiment_started_es(self,msg:ces.StartExperimentResponse = None)->None:
        self.log("Experiment started.",f"experiment name: {msg.experiment_name}")
    
    def on_experiment_resumed_es(self,msg:ces.ResumeExperimentRequest = None)->None:
        self.log("Experiment resumed",
                 f"experiment name: {msg.experiment_name}", 
                 f"duration extension: {msg.duration_extension}")

    def on_experiment_finished_es(self,msg:bool = None)->None:
        self.log("Experiment finished.",msg)
  
    def log(self, msg, *args):
        additional_info = ', '.join(str(arg) for arg in args)
        if additional_info:
            print(f"[ES] {msg}. Info: {additional_info}")
        else:
            print(f"[ES] {msg}.")

# as steps come in, append to traj JsonList and then save as trejectory into episode file. 
# output: 1 trajlist, Experiment(Json):Episode_N:Trajectory
# go to experiment.py -> line 28
            

def main():
    s = Server()
    s.start()
if __name__ == "__main__":
    main()