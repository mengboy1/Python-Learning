# Q Learning brain

import numpy as np
import pandas as pd


class QLearningTable:
	def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
		self.actions = actions
		self.lr = learning_rate
		self.gamma = reward_decay
		self.epsillon = e_greedy
		self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

	def choose_action(self, observation):
		self.check_state_exist(observation)
		# 选择action
		if np.random.uniform() < self.epsillon:		#选择Q value最高的action
			state_action = self.q_table.loc[observation,:]
			# 同一个state,可能会有多个相同的Q action value ,所以乱序一下
			state_action = state_action.reindex(np.random.permutation(state_action.index))
			action = state_action.argmax()
		else:	#随机选择 action
			action = np.random.choice(self.actions)
		return action

	def learn(self, s, a, r, s_):
		self.check_state_exist(s_)
		q_predict = self.q_table.loc[s,a]
		if s_!='terminal':
			q_target = r + self.gamma*self.q_table.loc[s_,:].max()
		else:
			q_target = r
		self.q_table.loc[s,a] += self.lr*(q_target - q_predict)

	def check_state_exist(self,state):
		if state not in self.q_table.index:
			self.q_table = self.q_table.append(
				pd.Series(
					[0]*len(self.actions),
					index=self.q_table.columns,
					name=state,
					)
				)



