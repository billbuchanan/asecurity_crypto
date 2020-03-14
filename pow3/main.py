# https://asecuritysite.com/encryption/pow3?Length=10
import hashlib
import base64
from cryptography.fernet import Fernet
import sys

keyseed = "12345"
encrypted="gAAAAABbEvwPCSaKjmQW8n3qZ95gfIK675Fiuf5KJYZ3CzVYtncFY5-hoc-OWkeR0B9ua85Zh1EXvXysZsQYc2GhZ2uoFCXcOA=="


if (len(sys.argv)>1):
	encrypted=str(sys.argv[1])
if (len(sys.argv)>2):
	keyseed=str(sys.argv[2])

iters=70000

h = hashlib.sha256(keyseed.encode()).digest()

for x in range(iters):

	try:
		h = hashlib.sha256(h).digest()

		key = base64.urlsafe_b64encode(h)
		decrypted = Fernet(key).decrypt(encrypted.encode())		
		print ("Decrypted:\t",decrypted)
		print ("Key:\t\t",key)
		print ("Iterations:\t",x-1)
		sys.exit()			
	except:
		pass
