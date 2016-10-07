import time
# opt1 iter = 1000 time = 12.074 sec
# opt2 iter = 1000 time = 11.479 sec
# opt3 iter = 1000 time = 7.798 sec
def rrr(Number,a,b,c):
	egg = 4*a+2*b+c
	k = bin(int(egg))
	N = bin(Number)
	N = N.lstrip('0b')
	if len(N) < 8:
		N = '0'*(8-len(N))+ N
	for i in range(8):
		if k == bin(i):
			return int(N[7-i])
			
def rule(Number,iteration):
	aaa = 2*iteration + 1
	data = [[]]
	
	for i in range(aaa):
		data[0].append(0)
		
		if i == iteration:
			data[0][i] = 1
	for i in range(1,iteration+1):
		data.append([])		
		for k in range(aaa):
			data[i].append(0)
		for j in range(iteration-i,iteration+i+1):
			
			if j == 0:
				data[i][j] = rrr(Number,0,data[i-1][j],data[i-1][j+1])
			elif j == aaa-1:
				data[i][j] = rrr(Number,data[i-1][j-1],data[i-1][j],0)
			else:
				data[i][j] = rrr(Number,data[i-1][j-1],data[i-1][j],data[i-1][j+1])
	return data
	
#print rule30(3)
#t = time.time()
#print rule30(2)
#print rule(121,5)
#	print i
#print time.time() - t
