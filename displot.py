import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

all_rates_list = np.load('all_rates_list.npy')

print(f'min rate {np.min(all_rates_list)}')
print(f'max rate {np.max(all_rates_list)}')
print(f'mean: {np.mean(all_rates_list)}')
print(f'standard dev: {np.std(all_rates_list)}')
print(f'5th percentile {np.percentile(all_rates_list,5)}')
print(f'95th percentile {np.percentile(all_rates_list,95)}')
print(f'2.5th percentile {np.percentile(all_rates_list,2.5)}')
print(f'97.5th percentile {np.percentile(all_rates_list,97.5)}')
sns.displot(all_rates_list, kde=True, bins=20)
plt.show()
