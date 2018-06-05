import gym
import numpy as np

env = gym.make('CartPole-v0')

best_length = 0
episode_lengths = []
best_weights = np.zeros(4)



for i in range(100):
    new_weights = np.random.uniform(-1.0, 1.0, 4)

    length = []
    for j in range(100):

        observation = env.reset()
        done = False
        cnt = 0

        while not done:
            # env.render()

            cnt += 1

            action = env.action_space.sample()

            observation, reward, done, _ = env.step(action)
    if average_length < best_length:
        bestlength = average_length
        best_weights = new_weights
    episode_lengths.append(average_length)
    if i % 10 == 0:
        print('best length is ', bestlength)

done = False
cnt = 0
env = wrappers.Monitor(env, 'MovieFiles2', force=True)
observation = env.reset()

while not done:
    cnt +=1
    action = 1 if np.dot(observation, best_weights) > 0 else 0
    observation, reward, done, _ = env.step(action)




print("with best weights, game lasted ", cnt, " moves")

env.close()
