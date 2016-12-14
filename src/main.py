from vocollect_core.task.task_runner import TaskRunnerBase
from MainTask import MainTask
from vocollect_core.utilities import obj_factory, pickler
from vocollect_core.dialog.functions import prompt_ready

class MainTask_Custom(MainTask):
	
	def welcome_prompt(self):
		prompt_ready("Welcome to my custom version", True)
		
#obj_factory.set_override(MainTask, MainTask_Custom)

class Inventory(TaskRunnerBase):
	
	def __init__(self):
		super(Inventory, self).__init__()
		
		import InvGlobals
		InvGlobals.runner = self
		
	def startUp(self):
		self.launch(obj_factory.get(MainTask, self), None)
		
	def initialize(self):
		self.app_name = "Inventory"

# This is the driver function for the voice application.
def main():
	start = Inventory()
	start = pickler.register_pickle_obj("Inventory", start)
	start.execute()
