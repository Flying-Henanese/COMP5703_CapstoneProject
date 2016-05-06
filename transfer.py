import simpy

def data_transfer(env , pipe, pipe_fog, pipe_cloud):
	while True:#bandwidth assumed to be 
		task = yield pipe.get()
        if computationCost > 50:
        	task['TimeStamp'] = task['TimeStamp']-task['DataSize']*3
        	yield pipe_cloud.put(task)
        else:
        	task['TimeStamp'] = task['TimeStamp']-task['DataSize']*0.5
        	yield pipe_fog.put(task)
        print 'name'

        yield env.timeout(task['DataSize']*0.5)




