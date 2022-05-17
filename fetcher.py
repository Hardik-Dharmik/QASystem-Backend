import requests

data = {
	'context' : 'This is context',
	'question' : 'This is question.'
}

x = requests.post('http://127.0.0.1:8000/', data = data)

print(x.text)