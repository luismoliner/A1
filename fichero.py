# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pylab as pl
import pylab as p
import matplotlib
matplotlib.style.use('ggplot')

df = pd.read_csv("dev.csv")

### Have a quick look at the data
#df.head()
#df.columns
#df.describe
#df.dtypes

for column in df.columns:
    print (column)

print(df['ib_var_1'][1])
print (df["ib_var_1"][0])
print (df['ib_var_1'].mean())
