import requests
import os
import random
import string
import json

extras = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'put url here'

names = json.loads(open('names.json').read())
passwords = json.loads(open('passwords.json').read())

for name in names:
	name_extra = extras

	username = names.lower() + name_extra + '@yahoo.com' or '@gmail.com'
	password = passwords

	requests.post(url, allow_redirects=False, data={
		'Put login thing here': username,
		'Put password thing here': password
	})
	print ("sending username: ", username, " and password: ", passwords)