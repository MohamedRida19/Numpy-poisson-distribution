import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
"""
x = np.random.uniform(size=10).reshape(2,5)
print(x)
"""

#showing the figure
a= 0
b= 10
Uniform_data = np.random.uniform( a, b,size=100)
Uniform_data = np.clip(Uniform_data, a,b)
sns.displot(Uniform_data, kde = True, linewidth= 0, fill= 0, color = 'red', label= 'UNIFORM')

plt.legend()
plt.show()
