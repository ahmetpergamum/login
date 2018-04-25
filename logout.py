#!/usr/bin/env python
import requests
import warnings
from random import randint


username=input("username:")
address=input("adress:")
a=1524640000000+randint(3000000,9999999)

payload = {"mode": "193", "username": username, "a": a, "producttype": "0"}
url = "https://" + address + "/logout.xml"
s = requests.session()
warnings.filterwarnings("ignore")
try:
    r=s.post(url, data=payload, verify=False)

    r.raise_for_status()

except Exception as exc:
    print('There was a problem: %s' % (exc))
    exit(0)

# check the http status code 200
# this is unnecessary if you use raise_for_status() try-catch block
if r.status_code == requests.codes.ok:
    print ("ok")
#     print len(r.text)
#     print(r.text[:1250])
#     print soup.prettify()

else:
    print "Page error"
    exit(0)
