from RL_brain import QLearningTable
from Environment import Environment
#训练
def rl():
	for episode in range(1000):
		#initial state
		curState = [0,0,90,0]
		while True:
			action = RL.choose_action(curState)
			nextState, isFinished = env.step(curState, action)
			reward = env.reward(curState, action)
			RL.learn(curState, action, reward, nextState)
			curState = nextState
			if isFinished:
				break
	#显示训练效果
	print('finished')

env = Environment()
RL = QLearningTable(actions=list(env.actions))