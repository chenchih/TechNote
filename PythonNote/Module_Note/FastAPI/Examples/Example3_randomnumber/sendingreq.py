import requests
print('===========================')
request= requests.get('http://127.0.0.1:8000')
print(request.json())
#{'example': 'This is an example', 'data': 0}

#get the random 
print('===========================')
request= requests.get('http://127.0.0.1:8000/random')
print(request.json())
#{'numbers': 127, 'limit': 1000}

#send request with limit id
print('===========================')
request= requests.get('http://127.0.0.1:8000/random/100')
print(request.json())
