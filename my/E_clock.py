import time
while   True :
	ts=(time.localtime(time.time()))
	print(ts[3],":",ts[4],":",ts[5])
	time.sleep(1)
