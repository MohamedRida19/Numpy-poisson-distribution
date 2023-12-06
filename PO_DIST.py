import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""x = np.random.poisson(lam= 3, size= 1000)
sns.histplot(x, kde = False, label = 'Graph1')

plt.legend()
plt.show()"""

normal_data = np.random.normal(loc = 50, scale = 7, size =1000)
poisson_data = np.random.poisson(lam = 50, size = 1000)

sns.displot(normal_data, kde= True, linewidth = 0, color= "red", fill = 0)
sns.displot(poisson_data, kde= True, linewidth = 0, color= "green", fill = 0)

plt.show()