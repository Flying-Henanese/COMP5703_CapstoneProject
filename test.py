import simpy
import random
from TaskGenerator import TaskGenerator
from transfer import data_transfer

SIM_TIME = 100
#env = simpy.Environment()
envs = []
#env=simpy.Environment()
#pipe_fog = simpy.Store(env, capacity=2)
#pipe_cloud = simpy.Store(env, capacity=40)
#global processTime
processTime = 0 
lifeTime =0

def process_fog(env):
	global processTime
	global lifeTime
	while True:
		task = yield pipe_fog.get()
		compTime = task['ComputationCost']*1
		yield env.timeout(compTime)
		#processTime = processTime+compTime
		lifeTime = lifeTime+(env.now - task['TimeStamp'])
		#name = task['Name']
		#print '%s processed on fog'%(task['Name'])

def process_cloud(env):
	global lifeTime
	global processTime
	while True:
		task = yield pipe_cloud.get()
		compTime = task['ComputationCost']*0.2
		yield env.timeout(compTime)
		#processTime = processTime + compTime 
		lifeTime = lifeTime +(env.now-task['TimeStamp'])
		#name = task['Name']
		#print '%s processed on cloud'%(task['Name'])

for i in range(1,20):
	envs.append(simpy.Environment())

index = 1
taskAmount = 100

for e in envs:
	lifeTime =0
	pipe_fog = simpy.Store(e, capacity=2)
	pipe_cloud = simpy.Store(e, capacity=20)
	pipe_transfer = simpy.Store(e, capacity=2)
	e.process(TaskGenerator(e, taskAmount, pipe_fog, pipe_cloud, pipe_transfer))
	e.process(data_transfer(e, pipe_transfer, pipe_fog, pipe_cloud))
	e.process(process_fog(e))
	e.process(process_cloud(e))
	e.run(until=5020000)
	print 'total time spent is %.2f for processing %d tasks'%(lifeTime/10, taskAmount)
	taskAmount = taskAmount+1

#env.process(TaskGenerator(env, 10000, pipe_fog, pipe_cloud,10))
#p1 = env.process(process_fog(env))
#p2 = env.process(process_cloud(env))
