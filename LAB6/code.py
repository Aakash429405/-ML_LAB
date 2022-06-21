//K-Means Clustering

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv('diabetes.csv')
plt.scatter(df.insulin,df['diastolic_bp'])

plt.ylabel('insulin')
plt.xlabel('diastolic_bp')

from sklearn.cluster import KMeans
km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(df[['insulin','diastolic_bp']])
y_predicted


df['cluster']=y_predicted
km.cluster_centers_

df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]
plt.scatter(df1.insulin,df1['diastolic_bp'],color='yellow')
plt.scatter(df2.insulin,df2['diastolic_bp'],color='orange')
plt.scatter(df3.insulin,df3['diastolic_bp'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.ylabel('insulin')
plt.xlabel('diastolic_bp')
plt.legend()
