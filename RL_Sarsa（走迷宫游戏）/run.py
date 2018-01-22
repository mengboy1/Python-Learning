# Sarsa算法
# 走迷宫

from maze_env import Maze
from RL_brain import SarsaTable

def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()
        action = RL.choose_action(str(observation))
        while True:
            # fresh env
            env.render()

            # 在环境中采取行为，获得下一个state_(observation_),reward和是否终止
            observation_, reward, done = env.step(action)

            # 根据下一个state(observation_)选取下一个action_
            action_ = RL.choose_action(str(observation_))

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_),action_)

            # swap observation,action
            observation = observation_
            action = action_

            # break while loop when end of this episode
            if done:
                break
    # end of game
    print('game over')
    env.destroy()

env = Maze()
RL = SarsaTable(actions=list(range(env.n_actions)))
env.after(100, update)
env.mainloop()