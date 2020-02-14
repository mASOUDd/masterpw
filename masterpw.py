#!/usr/bin/env python3

from hashlib import sha512
import getpass

# get master password
p = getpass.getpass('Master password: ')

url = input('The url: ')

# hash of master password
h = sha512(p.encode()).hexdigest()

# specific password for this url
# choose a unique salt
salt = 'salt'
sp = sha512((h + salt + url + h).encode()).hexdigest()
print('Password: {}'.format(sp))
