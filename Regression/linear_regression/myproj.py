#%% 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %%
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
#%%
print(X)
#%%
print(y)
# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)