# SarsaLambda brain

import numpy as np
import pandas as pd


class SarsaLambdaTable:
	def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9, trace_decay=0.9):
		self.actions = actions
		self.lr = learning_rate
		self.gamma = reward_decay
		self.epsillon = e_greedy
		self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
		self.lambda_ = trace_decay
		self.eligibility_trace = self.q_table.copy()

	def choose_action(self, observation):
		self.check_state_exist(observation)
		# 选择action
		if np.random.uniform() < self.epsillon:		#选择Q value最高的action
			state_action = self.q_table.loc[observation, :]
			# 同一个state,可能会有多个相同的Q action value ,所以乱序一下
			state_action = state_action.reindex(np.random.permutation(state_action.index))
			action = state_action.idxmax()
		else:	#随机选择 action
			action = np.random.choice(self.actions)
		return action

	def learn(self, s, a, r, s_, a_):
		self.check_state_exist(s_)
		q_predict = self.q_table.loc[s,a]
		if s_!='terminal':
			q_target = r + self.gamma*self.q_table.loc[s_, a_]
		else:
			q_target = r
		error = q_target - q_predict
		self.eligibility_trace.loc[s, :] *= 0
		self.eligibility_trace.loc[s, a] = 1
		self.q_table += self.lr * error * self.eligibility_trace
		self.eligibility_trace *= self.gamma * self.lambda_

	def check_state_exist(self,state):
		if state not in self.q_table.index:
			to_be_append = pd.Series(
				[0]*len(self.actions),
				index=self.q_table.columns,
				name=state,
				)
			self.q_table = self.q_table.append(to_be_append)
			self.eligibility_trace = self.eligibility_trace.append(to_be_append)





