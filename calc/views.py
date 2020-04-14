from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
import numpy as np
import pandas as pd
from .models import Dataset


def data():
    X = Dataset.X
    y = Dataset.y
    data = zip(X,y)
    return data
# Create your views here.
def home(request):
    
    return render(request,'home.html',{'exp':0,'result':0,'accuracy':0,'data':data()})

def add(request):
    val2 = float(request.GET['num2'])
    p = staticfiles_storage.path('Salary_Data.csv')
    dataset = pd.read_csv(p)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    yettopredict = np.array([[val2]])
    y_pred = regressor.predict(yettopredict)
    accuracy = regressor.score(X_test,y_test)
    accuracy = accuracy*100
    accuracy = int(accuracy)


    return render(request,'home.html',{'exp':val2,'result':int(y_pred),'accuracy':accuracy,'data':data()})