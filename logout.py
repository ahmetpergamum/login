#!/usr/bin/env python
import requests
from lxml import html


payload = {"mode": "193", "username": "aaaa", "a": "1524643588998", "producttype": "0"}
url = "https://ip:port/logout.xml"
s = requests.session()
try:
    r=s.post(url, data=payload, verify=False)

#     r = s.get('http://detectportal.firefox.com/success.txt')
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
