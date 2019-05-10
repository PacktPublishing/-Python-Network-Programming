"""
 NX-API-BOT 
"""
import requests
import json, pprint

"""
Modify these please
"""
url='http://172.16.1.79/ins'
switchuser='cisco'
switchpassword='cisco'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show ip int brief",
      "version": 1.2
    },
    "id": 1
  }
]

try: 
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

    pprint.pprint(response)
    print("*" * 10)
    for interface in response['result']['body']['TABLE_intf']:
        print("Interface {0} is {1}".format(interface['ROW_intf']['intf-name'], interface['ROW_intf']['admin-state']))
except: 
    print('Exception Occured')

