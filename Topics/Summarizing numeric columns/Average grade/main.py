# your code here. The DataFrame is already loaded as grades
n = grades.shape[0]
print(grades.head(n).mean(axis='columns'))
