import simpy
import random
from TaskGenerator import TaskGenerator

#the structure of tasks 
#{'Name', 'ComputationCost', 'DataSize', 'TaskType'}

CACHE_SIZE_FOG=10
CACHE_SIZE_CLOUD=500

TimeSpent = 0 

env = simpy.Environment()#setup for simpy environment

Things_to_Fog = [simpy.Store(env, capacity=1)]*CACHE_SIZE_FOG#restore tasks from Things to Fog
Fog_to_Cloud = [simpy.Store(env, capacity=1)]*CACHE_SIZE_CLOUD#restore tasks from Fog to Cloud 

#generate tasks
env.process(TaskGenerator(env, 100000, Things_to_Fog))
