import requests, json

# url = 'http://localhost:5000/user'
url = 'https://tamagotcha.herokuapp.com/user'
data = {'Test' : 'Data'}
r = requests.post(url, json=data)
print(r.text)
data = {'username' : 'user@hello.com', 'password' : 'badpassword'}
r = requests.post(url, json=data)
print(r.text)
data = {'username' : 'user@hello.com', 'password' : 'password'}
r = requests.post(url, json=data)
print(r.text)