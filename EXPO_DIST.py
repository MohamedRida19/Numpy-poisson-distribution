import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

'''x = np.random.exponential(scale = 2.5, size= (2,4))
print(x)'''

expo_data = np.random.exponential(scale = 7, size =1000)
sns.histplot(expo_data, kde=False, color='red', label= 'EXPO DIST', fill=0)
plt.legend()
plt.show()