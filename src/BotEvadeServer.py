import cellworld_experiment_service as ces
import cellworld_tracking as ct
import tcp_messages as tcp
import cellworld as cw

class BotEvadeServer():
    def __init__(self) -> None:
        print("=== BotEvade Server ===")
        pass
    def TrackingService(self):
        def send_step(step: ces.Step)->None:
            print(step.agent_name)
            # call gabbie script and gabbie.agent_name + _step = pred_step ## not implemented yet
            # step = self.process_step(step)
            self.ts.broadcast_subscribed(ces.Message(step.agent_name + "_step", step))
        
        self.ts                     = ct.TrackingService()
        self.ts.ip                  = "127.0.0.1"
        self.ts.on_new_connection   = self.on_connection_ts
        self.ts.send_step           = send_step
        res                         = self.ts.start(port=4510)
        print(f"[TS] Started: {res} at port {self.ts.port()}")
 
    def ExperimentService(self):
        self.es                     = ces.ExperimentService()
        # self.es.router.add_route("start_experiment_vr",self.start_experiment_vr, ces.StartExperimentRequestVR)
        self.es.on_new_connection   = self.on_connection_es
        self.es.on_episode_started  = self.on_episode_started_es
        self.es.set_tracking_service_ip("127.0.0.1")
        res = self.es.start()
        print(f"[ES] Started: {res} at port {self.es.port()}")
        self.es.join()
            
    def process_step(self, step:ces.Step)->ces.Step:
        print("processing")
        step.agent_name = "predator"
        return step
    def echo_ts(self,msg)->None:
        # print(f"Received: {msg}")
        return None
    def on_episode_started_es(self, msg):
        print(f"[ES] Episode Started: {msg}")
    def on_connection_es(self, connection_id)->None:
        print("[ES] New connection!")
    def on_connection_ts(self, connection_id)->None:
        print("[TS] New connection!")
def main():
    s = BotEvadeServer()
    s.TrackingService()
    s.ExperimentService()

if __name__ == "__main__":
    main()