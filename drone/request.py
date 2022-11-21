import requests

t = {'c':'takeoff'}
# r = requests.post('http://192.168.191.214:9000/',payload=t)
r = requests.post('http://0.0.0.0:8000/',json=t)

print(r.url)
