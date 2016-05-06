import simpy
import random

#the structure of tasks 
#{'Name', 'ComputationCost', 'DataSize', 'TaskType'} 

def Fog_device(env, cap, in_pipes):

    for pipe in in_pipes:
    	task = yield pipe.get()
    	duration = task['ComputationCost']
    	env.timeout(duration)
    	


    	

    	
        


