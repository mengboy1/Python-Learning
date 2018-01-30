import numpy as np

class Environment():
	#初始化环境
	def __init__(self):
		self.acceleration_space = range(-5,5,1)
		self.direction_space = range(-10,10,1)
		self.n_actions = len(self.acceleration_space) * len(self.direction_space)

	#更新
	def render():

	#获得环境反馈：得到下一状态，判断是否结束
	def step(self, state, action):


	#奖赏函数：考虑安全性（与边缘的距离）、舒适度（转角大小）和效率（速度+行驶距离）
	def reward(state, action):
		