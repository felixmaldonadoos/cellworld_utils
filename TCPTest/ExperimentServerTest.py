from json_cpp import *
from cellworld_experiment_service import ExperimentService 
import tcp_messages as tcp
from cellworld import Location, Step, Episode, World
from time import sleep

# https://drive.google.com/drive/u/1/folders/1SJ0CZyrv3_Fax3SkkDf42P43zVBP3Ful

def new_connection(self):
    print("new_connection")


# --- Fake Server ---  
exp_srv = ExperimentService()
exp_srv.allow_subscription = True
exp_srv.on_new_connection = new_connection

print("Starting")
exp_srv.start()
print("Started")

exp_srv.join()