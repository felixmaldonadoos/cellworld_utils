from tcp_messages import MessageServer, Message
from cellworld import *
import socket
from _thread import start_new_thread


class BotEvadeService(MessageServer):
    def __init__(self):
        MessageServer.__init__(self)

        # constants 
        self.header_predator = "predator_step"
        self.header_prey = "prey_step"
        self.port = 6001

        # "settings"
        self.allow_subscription = False
        self.on_new_connection = self.new_connection; 
        
        # service control flow 
        self.router.add_route("status", self.status)
        self.router.add_route("start_episode", self.start_episode)
        self.router.add_route("stop_episode",self.stop_episode)
        self.router.add_route("stop_service", self.stop_service) 
        
        # main messages 
        self.router.add_route(self.header_prey, str) # input 
        self.router.add_route(self.header_predator, str) # output
        
        # error handling 
        self.bFatalError = False
        self.bAbortCalled = False

    def log(self, error_type, error_msg):
        print(f"[{error_type} {error_msg}")
    
    def run(self):
        print("self.run()")
        self.allow_subscription = True

    def start_service(self):
        self.start(self.port)
    
    def start_episode(self):
        print("start episode")

    def stop_episode(self):
        print("stop episode")
        
    def stop_service(self):
        self.stop()
        self.join()

    def abort(self)->None:
        self.log("[FATAL] Aborting; stopping service.")
        self.stop_service()

    def new_connection(self):
        print("New connection!") 
        print(self.connections)

    def msg_step(self, header, body) -> Message:
        return Message(header=self.header, body=body)
    
    def send_broadcast_pred(self, step):
        print(f"Sending predator_step {step.location}")
        self.broadcast_subscribed(message=self.msg_step(self.header_predator, step))
        
if __name__ == "__main__":
    server = BotEvadeService(); 
    server.port = 6001; 

    # allow new connections 
    server.run(); 
