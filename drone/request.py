import requests

t = {'c':'takeoff'}
# r = requests.post('http://193.167.101.41:8080/',payload=t)
r = requests.post('http://193.167.101.41:8080/',json=t)

print(r.url)
