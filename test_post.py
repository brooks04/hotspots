import requests, json

# url = 'http://localhost:5000/schedule'
url = 'https://iothackhotspots.herokuapp.com/schedule'
data = {'Test' : 'Data'}
r = requests.post(url, json=data)
print(r.text)