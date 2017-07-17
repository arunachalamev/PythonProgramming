#!/usr/bin/python
import os
import sys

#Usage:
#python test.py URL <Priority>

#First argument passed as a link
link = sys.argv[1]
length = len(link)

#Fetches GUID and VC name
Job_ID  = link[length-36:length]
VC_Name = link[:-43]

#Job_ID = 'beb66627-124a-4ce0-bb02-8475b4dcd47d'
#VC_Name = 'https://cosmos08.osdinfra.net/cosmos/bingads.algo.fastjobs'

#if there is a second argument, then set that priority
if len(sys.argv) > 2:
	cmd = 'scope.exe updatejob ' +Job_ID +' -vc ' + VC_Name  +' -p ' +str(sys.argv[2])
else:
	cmd = 'scope.exe updatejob ' +Job_ID +' -vc ' + VC_Name  +' -p ' +str(999)

os.system(cmd)
