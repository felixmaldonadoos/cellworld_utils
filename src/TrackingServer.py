import cellworld_experiment_service as ces
import cellworld_tracking as ct
import tcp_messages as tm
import cellworld as cw

class VRServer():
    

    def TrackingService(self):
        def send_step(self, step: ces.Step):
            print(step)
            self.broadcast_subscribed(ces.Message(step.agent_name + "_step", step))
            
        self.ts = ct.TrackingService()
        self.ts.ip = "127.0.0.1"
        self.ts.on_new_connection = self.on_connection_ts
        self.send_step = send_step
        res = self.ts.start(port=4510)
        print(f"[TS] Started: {res} at port {self.ts.port()}")
 
    def ExperimentService(self):
        self.es = ces.ExperimentService()
        self.es.set_tracking_service_ip("127.0.0.1")
        self.es.on_new_connection  = self.on_connection_es
        self.es.on_episode_started = self.on_episode_started_es
        res = self.es.start()
        print(f"[ES] Started: {res} at port {self.es.port()}")
        self.es.join()

    def echo_ts(self,msg)->None:
        return None
        # print(f"Received: {msg}")

    def on_episode_started_es(self, msg):
        print(f"[ES] Episode Started: {msg}")

    def on_connection_es(self, connection_id)->None:
        print("[ES] New connection!")

    def on_connection_ts(self, connection_id)->None:
        print("[TS] New connection!")
        
def main():
    v = VRServer()
    v.TrackingService()
    v.ExperimentService()

if __name__ == "__main__":
    main()