import os
import sys
import re
import subprocess

cmd = ""

if str(sys.argv[1]) == "fastjobs" or str(sys.argv[1]) == "FASTJOBS":
	VC_Name = '''https://cosmos08.osdinfra.net/cosmos/bingads.algo.fastjobs/'''
	cmd 	= '''scope.exe joblist -vc https://cosmos08.osdinfra.net/cosmos/bingads.algo.fastjobs/ -jobname "arellave" -state "queued" '''

if str(sys.argv[1]) == "vc2" or str(sys.argv[1]) == "VC2":
	VC_Name = '''https://cosmos08.osdinfra.net/cosmos/bingads.algo.VC2/'''
	cmd 	= '''scope.exe joblist -vc https://cosmos08.osdinfra.net/cosmos/bingads.algo.VC2/ -jobname "arellave" -state "queued" '''



#Fetch the output from command prompt
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out


result = re.findall(r"Job ID:.*\n", out)
print result


for JobID in result:
	JobID = JobID.rstrip()
	length = len(JobID)
	Job_ID  = JobID[length-36:length]
	print Job_ID
	cmd = 'scope.exe updatejob ' +Job_ID +' -vc ' + VC_Name  +' -p ' +str(990)
	os.system(cmd)
	