import pandas as pd


df_rock = pd.read_csv('/Users/liudawei/Desktop/Spam Filter/Topics/Summarizing categorical columns/Non-na values/data/dataset/input.txt')
n = df_rock.labels.count()
print(n)

