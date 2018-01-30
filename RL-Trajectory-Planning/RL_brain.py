import numpy as np
import pandas as pd

class QLearningTable:
	def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
		self.actions = actions
		self.lr = learning_rate
		self.gamma = reward_decay
		self.epsilon = e_greedy
		self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

	def choose_action(self, observation):
		self.check_state_exist(observation)
		if np.random.uniform() < self.epsilon:
			state_action = self.q_table.loc[observation,:]
			state_action = state_action.reindex(np.random.permutation(state_action.index))
			action = state_action.idxmax()
		else:
			action = np.random.choice(self.actions)
		return action

	def check_state_exist(self, state):
		if state not in self.q_table.index:
			self.q_table = self.q_table.append(
					pd.Series(
							[0]*len(self.actions),
							index = self.q_table.columns,
							name = state,
							)
					)

	def learn(self, state, action, reward, state_):
		self.check_state_exist(state_)
		q_predict = self.q_table.loc[state,action]
		if state_ != 'terminal':
			q_target = self.reward + self.gamma * self.q_table.loc[state_,:].max()
		else:
			q_target = self.reward
		self.q_table.loc[state,action] += self.lr * (q_target - q_predict)

