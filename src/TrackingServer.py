import cellworld_experiment_service as ces
import cellworld_tracking as ct
import tcp_messages as tm
import cellworld as cw
class VRServer():
    def TrackingService(self):
        self.ts = ct.TrackingService()
        self.ts.ip = "127.0.0.1"
        self.ts.on_new_connection = self.on_connection_ts
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

main()


# class VRExperimentService(ces.ExperimentService):
#     def __init__(self):
#         super().__init__()
#         # self.allow_subscription = True
#         self.on_new_connection = self.new_connection; 
#         self.set_tracking_service_ip = "127.0.0.1"
#         self.port = 4500

#     def new_connection(self) ->None:
#         print("[ES] New connection!")

# class VRTrackingService(ct.TrackingService):
#     def __init__(self):
#         # self.port = 4510
#         self.on_new_connection = self.new_connection
#         # self.allow_subscription = True
#         # self.ip = "127.0.0.1"
        
#     def new_connection(self)->None:
#         print("[TS] New connection!")

# class Server():
#     def __init__(self) -> None:
#         self.es = VRExperimentService()
#         self.ts = VRTrackingService()

#     def StartVRTrackingService(self):
#         print("starting tracking service.")
#         self.ts.ip = "127.0.0.1"
#         self.ts.start(port=4510)
#         # self.ts.port = 4510
#         # self.ts.start()

#     def StartExperimentService(self): 
#         print("starting experiment service.")
#         self.es.start()
#         self.es.join()

# def main(): 
#     # Server().StartExperimentService()
#     Server().StartVRTrackingService()
#     # server.StartExperimentService()
#     print("Waiting for data...")



# if __name__ == "__main__":
#     main()