#!/usr/env/bin python3
"""
 NX-API-BOT 
"""
import requests
import json
import pprint # this was added

"""
Modify these please
"""
url='http://172.16.1.91/ins'
switchuser='cisco'
switchpassword='cisco'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

# additional section
pprint.pprint(response)
print("*" * 10)
print("This is the hostname: ")
print(response['result']['body']['host_name'])
