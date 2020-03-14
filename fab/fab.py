# https://asecuritysite.com/encryption/fab?Length=10
import sys

j = 3
k = 7
modval = 10

val = "8675309"

if (len(sys.argv)>1):
	val=str(sys.argv[1])
if (len(sys.argv)>2):
	modval=int(sys.argv[2])

def conv(val):
	arr = []
	for i in range(len(val)):
		arr.append(int(val[i]))
	return arr

def showvals(val,j,k):
	for i in range(len(val)):
		if (i==j-1):  
			print ("[%3d]"%val[i], end = '')
		elif (i==k-1):  
			print ("[%3d]"%val[i], end = '')
		else:
			print ("%3d"%val[i], end = '')

s=conv(val)

print ("j=",j," k=",k)
print ("Seed:\t",val)

if (len(s)<k):
	print ("Value needs to be larger than 7")
	exit()

showvals(s,j,k)

for n in range(20):
    out = (s[j-1] + s[k-1]) % modval
    for i in range(len(s)-1):
      s[i] = s[i+1] 

    s[len(s)-1] = out
             
    print ("-->",out)
    showvals(s,j,k)

print ("-->",out)
