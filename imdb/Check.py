import numpy as np
import pandas as pd
import os
print(os.getcwd())
data = pd.read_csv('Test2.csv')
print(data.isnull().sum())