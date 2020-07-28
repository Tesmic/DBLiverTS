from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
# Create your views here.
#from sklearn.externals import joblib
import joblib

arima=joblib.load('./models/CallPredModel.pkl')


def callindex(request):
    temp={}
    temp['interval']=12
    
    context ={'temp':temp}
    return render(request,'call.html',context)
 #   return HttpResponse({'a':1})

def cpredict(request):
    context ={'temp':'  '}
    print (request)
    if request.method == 'POST':
        temp={}
        temp['interval']=request.POST.get('interval')
        
        #Datapreprocessing Convert the values to float
        interval=int(temp['interval'])
        
     #   result = [interval]
        #Passing data to model & loading the model from disks
       # prediction = arima.predict([result])[0]
        prediction=arima.forecast(steps=interval)
        pred=prediction[0]
        for i in range(len(pred)):
            pred[i]=int(pred[i])


      #  conf_score =  np.max(classifier.predict_proba([result]))*100
        if prediction == 1 :
            context ={'a':'Liver Disease Prediction : Infected','temp':temp }
        else:
            context ={'a':pred,'temp':temp }
    return render(request,'call.html',context)