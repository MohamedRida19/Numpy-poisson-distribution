import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

"""x = np.random.logistic(loc= 0, scale=4, size=3)

print(x)"""

logistic_data = np.random.logistic( scale = 2, size=1000)
normal_data = np.random.normal( size= 1000)

sns.histplot(logistic_data, kde= True, linewidth =0, fill =0, color= "red", label='logistic' )
sns.histplot(normal_data, kde= True, linewidth =0, fill =0, color= "green", label= 'Normal' )

plt.legend()
plt.show()