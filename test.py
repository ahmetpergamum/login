#!/usr/bin/env python
import requests
import getpass
username=raw_input("username:")
password=getpass.getpass("password:")
address=raw_input("adress:")
print (username + " " + password + " "+ address)
