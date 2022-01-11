import requests
url = 'https://raw.githubusercontent.com/giancarlopernudisegura/cmput404-lab1/master/main.py'
r = requests.get(url)
print(r.text)
