import simpy
import random

#the structure of tasks 
#{'Name', 'ComputationCost', 'DataSize', 'TaskType'} 

def cloud(env, cap, in_pipes):
    