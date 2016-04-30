#!/usr/bin/env python3

from hashlib import sha1
import getpass

# get master password
p = getpass.getpass('Master password: ')

url = input('The url: ')

# hash of master password
h = sha1(p.encode()).hexdigest()

# specific password for this url
# 'ehem': because why not
sp = sha1((h + 'ehem' + url + h).encode()).hexdigest()
print('Password: {}'.format(sp))
