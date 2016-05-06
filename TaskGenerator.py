import simpy
import random

Types = ['Streaming','imageProcessing', 'computation']

def TaskGenerator(env, num, pipe_fog, pipe_cloud, pipe):

    """
    Treated as things which generete tasks
    """

    for i in range(1, num):
        yield env.timeout(random.randint(5,10))#gap between each two successive tasks
        name = 'Task %d'%(i)
        #computationCost = random.randint(10,100)
        dataSize = random.randint(1, 100)
        computationCost = random.randint(1,100)
        TaskType = random.choice(Types)
        TimeStamp = env.now 

        task = {'Name':name, 'ComputationCost':computationCost, 'DataSize': dataSize, 'TaskType': TaskType, 'TimeStamp': TimeStamp}
        #yield env.timeout(dataSize*0.4)#data transferring time
        #yield pipe.put(task)
        #migration_index = 0 
        yield pipe.put(task)
        
        #if computationCost > threshold:
            #yield env.timeout(dataSize*3)
            #pipe_cloud.put(task)
        #else:
            #yield env.timeout(dataSize*0.5)#data)
            #pipe_fog.put(task)


