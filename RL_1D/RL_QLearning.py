'''
A simple example for Reinforcement Learning using table lookup Q-learning method
An agent "o" is on the left of a 1 dimensional world, the treasure is on the rightmost location
'''

import numpy as np
import pandas as pd
import time

N_STATES = 6 #1维世界的宽度
ACTIONS = ['left','right'] #探索者的可用动作
EPSILON = 0.9 #贪婪度 greedy:90%的时间选择当前最优策略，10%的时间来探索
ALPHA = 0.1	#学习率
GAMMA = 0.9	#奖励递减值
MAX_EPISODES = 13 #最大回合数
FRESH_TIME = 0.3 #移动间隔时间

# 建立q表，存储所有状态下所有动作的行为值
def build_q_table(n_states, actions):
	table = pd.DataFrame(np.zeros((n_states,len(actions))),columns=actions)
	return table
# q_table:
'''
	left  right
0	0.0	  0.0
1	0.0   0.0
2	0.0   0.0
3	0.0   0.0
4	0.0   0.0
5	0.0   0.0
'''

# 在某个state地点，选择行为
def choose_action(state, q_table):
	state_actions = q_table.iloc[state,:]
	if(np.random.uniform() > EPSILON) or (state_actions.all() == 0):	#非贪婪或者这个state还没有探索过
		action_name = np.random.choice(ACTIONS)
	else:
		action_name = state_actions.argmax()  #贪婪模式，选择最优策略
	return action_name

# 环境反馈S_,R
def get_env_feedback(S,A):
	if A == 'right':
		if S == N_STATES - 2:
			S_ = 'terminal'
			R = 1
		else:
			S_ = S + 1
			R = 0
	else:
		R = 0
		if S == 0:
			S_ = S
		else:
			S_ = S - 1
	return S_,R

# 环境更新
def updata_env(S, episode, step_counter):
	env_list = ['-']*(N_STATES-1)+['T']
	if S == 'terminal':
		interaction = 'Episode %s:total_steps = %s' % (episode+1,step_counter)
		print('\r{}'.format(interaction),end='')
		time.sleep(2)
		print('\r            ',end='')
	else:
		env_list[S]='o'
		interaction = ''.join(env_list)
		print('\r{}'.format(interaction), end='')
		time.sleep(FRESH_TIME)

# 强化学习主循环
def rl():
	q_table = build_q_table(N_STATES, ACTIONS)
	for episode in range(MAX_EPISODES):
		step_counter = 0
		S = 0
		is_terminated = False
		updata_env(S, episode, step_counter)
		while not is_terminated:
			A = choose_action(S, q_table)
			S_,R = get_env_feedback(S,A)
			q_predict = q_table.loc[S,A]	#估算的（状态-行为）值
			if S_ != 'terminal':
				q_target = R + GAMMA*q_table.iloc[S_,:].max()	#实际的（状态-行为）值（回合没结束）
			else:
				q_target = R 	#实际的（状态-行为）值（回合结束）
				is_terminated = True

			q_table.loc[S,A] += ALPHA*(q_target - q_predict)	#q_table更新
			S = S_
			updata_env(S,episode,step_counter+1)
			step_counter += 1
	return q_table

q_table = rl()
print('\r\nQ-table:\n')
print(q_table)
