# your code here. The DataFrame is already loaded as grades
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/liudawei/Downloads/2015.csv')
df.plot(y='Family', kind='box')
plt.show()
