from django.db import models
from django.contrib.staticfiles.storage import staticfiles_storage
import numpy as np
import pandas as pd
# Create your models here.
class Dataset:
    p = staticfiles_storage.path('Salary_Data.csv')
    data = pd.read_csv(p)
    dataset = np.array(data)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, 1].values