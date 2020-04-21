from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
import numpy as np
import pandas as pd
import requests
import json
from django.http import JsonResponse
from .models import Dataset
from .serialize import NumpyArrayEncoder


def data():
    X = Dataset.X
    y = Dataset.y
    datas = zip(X,y)
    return datas
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

def api(request):
    url = "https://api.covid19india.org/data.json"
    response = requests.get(url)
    # response = response.json()
    # response = json.dumps(response)
    item = json.loads(response.content.decode('utf-8'))
    return HttpResponse(item)



def send_json(request):
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

    # numpyData = {"array": X}
    X_json = json.dumps(X, cls=NumpyArrayEncoder)
    Y_json = pd.Series(y).to_json(orient='values')
    data = [{'exp': val2, 'salary': int(y_pred),'accuracy': accuracy,'X':X_json,'Y':Y_json}]

    return JsonResponse(data, safe=False)