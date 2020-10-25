import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':1, 'sex':1, 'cp':1,'trestbps':1,'chol':1,'fbs':1,'restecg':1,'thalach':1,'exang':1,'oldpeak':1,'slope':1,'ca':1,'thal':3})

print(r.json())