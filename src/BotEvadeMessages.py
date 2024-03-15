from json_cpp import JsonObject
from cellworld import * 
from datetime import datetime 

class StartExperimentRequest(JsonObject):
    def __init__(self, prefix: str = "", suffix: str = "", world: World_info = None, subject_name: str = "", duration: int = 0, rewards_cells: Cell_group_builder = None, rewards_orientations: JsonList = None):
        self.prefix = prefix
        self.suffix = suffix
        if not world:
            world = World_info()
        self.world = world
        self.subject_name = subject_name
        self.duration = duration
        if rewards_cells:
            self.rewards_cells = rewards_cells
        else:
            self.rewards_cells = Cell_group_builder()
        if rewards_orientations:
            self.rewards_orientations = rewards_orientations
        else:
            self.rewards_orientations = JsonList(list_type=int)