from model import ARS
import gymnasium as gym
from tqdm import tqdm
import matplotlib.pyplot as plt
import pickle

if __name__ == '__main__':
    ars = ARS(
        input_dim=24, 
        output_dim=4, 
        alpha=0.09, 
        N=16, 
        nu=0.06, 
        b=16, 
        env_name='BipedalWalkerHardcore-v3', 
        seed=42
    )
    
    num_iters = 300
    total_rewards = []
    pbar = tqdm(range(num_iters), desc='Training ARS: ')

    for i in pbar:
        reward, std = ars.train_one_iter(num_iters=i)
        total_rewards.append(reward)
        pbar.set_postfix(
            {
                'Reward': reward, 
                'Std': std
            }
        )

    print('Training complete.')
    print('Weights: \n', ars.weight)
    normalizer_params = {
        'mean' : ars.normalizer.mean,
        'var' : ars.normalizer.var,
    }
    print('Normalizer params: \n', normalizer_params)

    plt.plot(total_rewards)
    plt.xlabel('Iterations')
    plt.ylabel('Reward')
    plt.title('ARS V2 on BipedalWalkerHardcore-v3')
    plt.show()

    # Save rewards
    with open('ars_v2t_bipedalwalker.pkl', 'wb') as f:
        pickle.dump(total_rewards, f)

    # Save weights
    with open('ars_v2t_bipedalwalker_weights.pkl', 'wb') as f:
        pickle.dump(ars.weight, f)

    # Save normalizer
    with open('ars_v2t_bipedalwalker_normalizer.pkl', 'wb') as f:
        pickle.dump(normalizer_params, f)
    


    