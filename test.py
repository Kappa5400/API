'''
Curl script to test api on local 8000 socket.
'''
#!/bin/bash

results = curl -l http://127.0.0.1:8000/fruit/?format=json

print (results)