from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import PredefinedSplit
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression
from sklearn.pipeline import Pipeline
from sklearn import metrics
import os
from numpy import genfromtxt
from tqdm import tqdm
import pandas as pd
import random
import scipy.io as sio
from scipy.spatial.distance import cdist


import numpy as np
import scipy.io as sio
import h5py

import time

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.properties')

def load_dataset(data_path,behav_path):
    data = sio.loadmat(data_path)
    X = data['data']
    p = X.shape[0]
    n = X.shape[2]
    y = genfromtxt(behav_path, delimiter=',')
    X = X.reshape(n,p*p)
    return X,y

def rcpm(X,y):
    num_iter = int(config.get('default','iterations'))
    results = np.zeros((num_iter,1))
    pct = 0.1 
    alphas = 10**np.linspace(10,-2,100)*0.5 # specify alphas to search
    reg = Ridge()
    cv10 = KFold(n_splits=2, random_state=665)
    for i in tqdm(range(num_iter)):
        all_pred = cross_val_predict(reg, X,y, cv=cv10, n_jobs=2)
        results[i] = np.corrcoef(all_pred, y)[0, 1]
    df = pd.DataFrame(results)
    df.to_csv("rcpm_iq.csv")


import sys
if __name__ == "__main__":
    database = config.get('default', 'database')
    data_path = config.get('path',database)
    behav_path = config.get('behavior',database)
    X,y = load_dataset(data_path,behav_path)
    rcpm(X,y)
    random.seed(3000)
