import requests, json

# url = 'http://localhost:5000/schedule'
url = 'https://iothackhotspots.herokuapp.com/rooms'
# data = {'Test' : 'Data'}
# r = requests.post(url, json=data)
r = requests.get(url)
print(r.text)