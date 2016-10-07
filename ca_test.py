import cellularAutomation as ca
import random
import Tkinter as tki
import time
#from PIL import Image, ImageDraw

from sys import argv

script, rN, iii = argv

root = tki.Tk()

iters = int(iii)
ruleNumber = int(rN)
	#iters = 700
w = 2*iters + 1
h = iters 	# height is number of iterations
if iters < 50:
	cs = 10 		# cube side size
elif iters < 250:
	cs = 3
elif iters < 500:
	cs = 2
else: 
	cs = 1
cn = w 	# cube number in canv side

canv = tki.Canvas(root,width=w*cs,height=h*cs,bg='white',cursor='pencil')

t = time.time()

data = ca.rule(ruleNumber,iters)

zeros = []

for i in range(cn):
	zeros.append([])
	for j in range(cn):
		zeros[i].append(0)

for i in range(len(data)):
	for j in range(len(data[0])):
		if data[i][j] == 1:
			try: zeros[i][j] = data[i][j]
			except IndexError:  print "Wrong index assignment: i = %r, j = %r" % (i,j); quit()		
for i in range(cn):
	for j in range(cn):
		if zeros[i][j] == 1:
			canv.create_rectangle(cs*j,cs*i,cs*j+cs,cs*i+cs,fill="gray",outline="black") 

print "Time: ", time.time() - t
	
canv.pack()

root.mainloop() #'''
	
def getgerid():
	x = cs
	while x < 500:
		canv.create_line(x,0,x,500,width=1,fill="black")
		x += cs

	y = cs
	while y < 500:
		canv.create_line(0,y,500,y,width=1,fill="black")
		y += cs	




