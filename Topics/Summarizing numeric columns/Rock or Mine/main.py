import pandas as pd


df_rock = pd.read_csv('/Users/liudawei/Desktop/Spam Filter/Topics/Summarizing numeric columns/Rock or Mine/data/dataset/input.txt')
m = round(df_rock.loc[df_rock.labels == 'M', 'null_deg'].median(), 3)
r = round(df_rock.loc[df_rock.labels == 'R', 'null_deg'].median(), 3)
print(f'M = {m} R = {r}')
