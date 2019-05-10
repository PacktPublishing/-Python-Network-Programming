"""
Genrated from NX-API-BOT 
"""
import requests, logging, time
import json, pprint

#logging configuration
logging.basicConfig(filename='nexus.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%b %d %I:%M:%S')
host = 'nx-osv-1'
process = 'nexus_interface'

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

while True:
    try: 
        response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
        for interface in response['result']['body']['TABLE_intf']:
            interface_name = interface['ROW_intf']['intf-name']
            interface_status = interface['ROW_intf']['admin-state']
            logging.warning(host + ' ' + process + ': ' + interface_name + "=" + interface_status) 
    except: 
        logging.warning('Exception Occured')
    time.sleep(1)


