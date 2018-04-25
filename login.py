#!/usr/bin/env python
import requests
import warnings


payload = {"mode": "191", "username": "aaaa", "password": "aaa", "a": "1524643588998"}
url = "https://ip:port/login.xml"
s = requests.session()
warnings.filterwarnings("ignore")
try:
    r=s.post(url, data=payload, verify=False)

    r = s.get('http://detectportal.firefox.com/success.txt')
    r.raise_for_status()

except Exception as exc:
    print('There was a problem: %s' % (exc))
    exit(0)

# check the http status code 200
# this is unnecessary if you use raise_for_status() try-catch block
if r.status_code == requests.codes.ok:
    print ("ok")
#     print len(r.text)
    print(r.text[:8])

else:
    print "Page error"
    exit(0)
