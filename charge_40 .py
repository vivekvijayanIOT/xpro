#python code: BEACON
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import time
import math
from random import randint
import numpy as nr
import math
from decimal import *


y10 = []
starttime=time.time()
visited=0
times=0
mfile=open("mobile_node_data.txt","w")
mfile.write("\t\tData collected by Mobile node\n\n---------------------------------------------------\n\n")

lefttime=[]
nodename=[]

def timer():
	global times
	times=times+1
class node:
	qq=0
	def __init__(self,c,x,y):
		self.radius=2
		self.xpos=x
		self.ypos=y
		self.charge=c
		self.xp1=self.radius+self.xpos
		self.xm1=self.radius-self.xpos
		self.yp1=self.radius+self.ypos
		self.ym1=self.radius-self.ypos
		self.check=0
		self.times=0
	def discharge(self):
		if(self.charge>2):
			self.charge-=0.53   # to change the battery level
	def charger(self,n):
		global times
		for x in range(0,100):
			n=n+10
			b = "\t\tCharging [" + "*" * x+"] %d%%"%n
			print(b,end="\r")
			time.sleep(1)
			times=times+1
			self.times=times
			if(n>=80):
				break
		self.charge=self.charge+n-5

		print("\t\t************ 80% Charging completed*************")

	def show(self):
		u="Unknown -Not yet visited"
		if(self.check==1):
			c=str(round(self.charge))+"%"
			return c
		else:
			return u
	def update_time(self,times):
		self.times=times


class dyn_node:
	def __init__(self,radius):
		self.charge=100
		self.xpos=0
		self.ypos=0
		self.radius=radius
		self.xp1=radius+self.xpos
		self.xm1=radius-self.xpos
		self.yp1=radius+self.ypos
		self.ym1=radius-self.ypos
	def discharge(self):
		self.charge-=5
		self.radius-=5


total_nodes=40
charg=[0]

print("**** WSN Execution starts ****\n")
Mobile_node_radius=int(input("Enter the Mobile node range\t :"))
D=dyn_node(Mobile_node_radius)
ques=input("Do you want to set the charge of static node? Y or N \n")
if ques=='y':
	print('OK.. enter the charge of nodes respectively..')
	for a in range(1,41):
		print("Charge of Node-%d"%a)
		w=int(input())
		charg.append(w)
else:
	print('The default value of charge : 100% is set to all nodes')
	for a in range(1,41):
		print("Charge of Node-%d : 100"%a)
		charg.append(100)

def effect():
	effect=0
	if(N1.charge!=0.0):
		effect=effect+1
	if(N2.charge!=0.0):
		effect=effect+1
	if(N3.charge!=0.0):
		effect=effect+1
	if(N4.charge!=0.0):
		effect=effect+1
	if(N5.charge!=0.0):
		effect=effect+1
	if(N6.charge!=0.0):
		effect=effect+1
	if(N7.charge!=0.0):
		effect=effect+1
	if(N8.charge!=0.0):
		effect=effect+1
	if(N9.charge!=0.0):
		effect=effect+1
	if(N10.charge!=0.0):
		effect=effect+1
	if(N11.charge!=0.0):
		effect=effect+1
	if(N12.charge!=0.0):
		effect=effect+1
	if(N13.charge!=0.0):
		effect=effect+1
	if(N14.charge!=0.0):
		effect=effect+1
	if(N15.charge!=0.0):
		effect=effect+1
	if(N16.charge!=0.0):
		effect=effect+1
	if(N17.charge!=0.0):
		effect=effect+1
	if(N18.charge!=0.0):
		effect=effect+1
	if(N19.charge!=0.0):
		effect=effect+1
	if(N20.charge!=0.0):
		effect=effect+1
	if(N21.charge!=0.0):
		effect=effect+1
	if(N22.charge!=0.0):
		effect=effect+1
	if(N23.charge!=0.0):
		effect=effect+1
	if(N24.charge!=0.0):
		effect=effect+1
	if(N25.charge!=0.0):
		effect=effect+1
	if(N26.charge!=0.0):
		effect=effect+1
	if(N27.charge!=0.0):
		effect=effect+1
	if(N28.charge!=0.0):
		effect=effect+1
	if(N29.charge!=0.0):
		effect=effect+1
	if(N30.charge!=0.0):
		effect=effect+1
	if(N31.charge!=0.0):
		effect=effect+1
	if(N32.charge!=0.0):
		effect=effect+1
	if(N33.charge!=0.0):
		effect=effect+1
	if(N34.charge!=0.0):
		effect=effect+1
	if(N35.charge!=0.0):
		effect=effect+1
	if(N36.charge!=0.0):
		effect=effect+1
	if(N37.charge!=0.0):
		effect=effect+1
	if(N38.charge!=0.0):
		effect=effect+1
	if(N39.charge!=0.0):
		effect=effect+1
	if(N40.charge!=0.0):
		effect=effect+1

	return effect/40*100

def leftcheck():
	if N1.charge<1 and N1.qq==0:
		lefttime.append(times)
		nodename.append('Node 1')
		N1.qq=1
	if N2.charge<1 and N2.qq==0:
		lefttime.append(times)
		nodename.append('Node 2')
		N2.qq=1
	if N3.charge<1 and N3.qq==0:
		lefttime.append(times)
		nodename.append('Node 3')
		N3.qq=1
	if N4.charge<1 and N4.qq==0:
		lefttime.append(times)
		nodename.append('Node 4')
		N4.qq=1
	if N5.charge<1 and N5.qq==0:
		lefttime.append(times)
		nodename.append('Node 5')
		N5.qq=1
	if N6.charge<1 and N6.qq==0:
		lefttime.append(times)
		nodename.append('Node 6')
		N6.qq=1
	if N7.charge<1 and N7.qq==0:
		lefttime.append(times)
		nodename.append('Node 7')
		N7.qq=1
	if N8.charge<1 and N8.qq==0:
		lefttime.append(times)
		nodename.append('Node 8')
		N8.qq=1
	if N9.charge<1 and N9.qq==0:
		lefttime.append(times)
		nodename.append('Node 9')
		N9.qq=1
	if N10.charge<1 and N10.qq==0:
		lefttime.append(times)
		nodename.append('Node 10')
		N10.qq=1
	if N11.charge<1 and N11.qq==0:
		lefttime.append(times)
		nodename.append('Node 11')
		N11.qq=1
	if N12.charge<1 and N12.qq==0:
		lefttime.append(times)
		nodename.append('Node 12')
		N12.qq=1
	if N13.charge<1 and N13.qq==0:
		lefttime.append(times)
		nodename.append('Node 13')
		N13.qq=1
	if N14.charge<1 and N14.qq==0:
		lefttime.append(times)
		nodename.append('Node 14')
		N14.qq=1
	if N15.charge<1 and N15.qq==0:
		lefttime.append(times)
		nodename.append('Node 15')
		N15.qq=1
	if N16.charge<1 and N16.qq==0:
		lefttime.append(times)
		nodename.append('Node 16')
		N16.qq=1
	if N17.charge<1 and N17.qq==0:
		lefttime.append(times)
		nodename.append('Node 17')
		N17.qq=1
	if N18.charge<1 and N18.qq==0:
		lefttime.append(times)
		nodename.append('Node 18')
		N18.qq=1
	if N19.charge<1 and N19.qq==0:
		lefttime.append(times)
		nodename.append('Node 19')
		N19.qq=1
	if N20.charge<1 and N20.qq==0:
		lefttime.append(times)
		nodename.append('Node 20')
		N20.qq=1
	if N21.charge<1 and N21.qq==0:
		lefttime.append(times)
		nodename.append('Node 21')
		N21.qq=1
	if N22.charge<1 and N22.qq==0:
		lefttime.append(times)
		nodename.append('Node 22')
		N22.qq=1
	if N23.charge<1 and N23.qq==0:
		lefttime.append(times)
		nodename.append('Node 23')
		N23.qq=1
	if N24.charge<1 and N24.qq==0:
		lefttime.append(times)
		nodename.append('Node 24')
		N24.qq=1
	if N25.charge<1 and N25.qq==0:
		lefttime.append(times)
		nodename.append('Node 25')
		N25.qq=1
	if N26.charge<1 and N26.qq==0:
		lefttime.append(times)
		nodename.append('Node 26')
		N26.qq=1
	if N27.charge<1 and N27.qq==0:
		lefttime.append(times)
		nodename.append('Node 27')
		N27.qq=1
	if N28.charge<1 and N28.qq==0:
		lefttime.append(times)
		nodename.append('Node 28')
		N28.qq=1
	if N29.charge<1 and N29.qq==0:
		lefttime.append(times)
		nodename.append('Node 29')
		N29.qq=1
	if N30.charge<1 and N30.qq==0:
		lefttime.append(times)
		nodename.append('Node 30')
		N30.qq=1
	if N31.charge<1 and N31.qq==0:
		lefttime.append(times)
		nodename.append('Node 31')
		N31.qq=1
	if N32.charge<1 and N32.qq==0:
		lefttime.append(times)
		nodename.append('Node 32')
		N32.qq=1
	if N33.charge<1 and N33.qq==0:
		lefttime.append(times)
		nodename.append('Node 33')
		N33.qq=1
	if N34.charge<1 and N34.qq==0:
		lefttime.append(times)
		nodename.append('Node 34')
		N34.qq=1
	if N35.charge<1 and N35.qq==0:
		lefttime.append(times)
		nodename.append('Node 35')
		N35.qq=1
	if N36.charge<1 and N36.qq==0:
		lefttime.append(times)
		nodename.append('Node 36')
		N36.qq=1
	if N37.charge<1 and N37.qq==0:
		lefttime.append(times)
		nodename.append('Node 37')
		N37.qq=1
	if N38.charge<1 and N38.qq==0:
		lefttime.append(times)
		nodename.append('Node 38')
		N38.qq=1
	if N39.charge<1 and N39.qq==0:
		lefttime.append(times)
		nodename.append('Node 39')
		N39.qq=1
	if N40.charge<1 and N40.qq==0:
		lefttime.append(times)
		nodename.append('Node 40')
		N40.qq=1

xp=[20,70,20,100,40,50,90,90,20,50,200,150,120,60,190,110,130,130,100,0,200,170,260,100,140,380,130,350,250,190,300,150,210,360,290,250,130,130,350,20]
yp=[60,10,350,90,120,110,120,20,190,50,130,60,40,250,30,160,50,100,360,0,250,210,380,190,320,360,170,50,300,390,130,160,40,180,30,250,350,300,150,30]
'''for a in range(0,40):
	xp.append(int(input('Enter the X-axis value for NODE - %d : '%a)))
	yp.append(int(input('Enter the Y-axis value for NODE - %d : '%a)))

'''


# Node declaration
N1,N2,N3,N4,N5=node(charg[1],20,60),node(charg[2],70,10),node(charg[3],20,350),node(charg[4],100,90),node(charg[5],40,120)
N6,N7,N8,N9,N10=node(charg[6],50,110),node(charg[7],90,120),node(charg[8],90,20),node(charg[9],20,190),node(charg[10],50,50)
N11,N12,N13,N14,N15=node(charg[11],200,130),node(charg[12],150,60),node(charg[13],120,40),node(charg[14],60,250),node(charg[15],190,30)
N16,N17,N18,N19,N20=node(charg[16],110,160),node(charg[17],130,50),node(charg[18],130,100),node(charg[19],100,360),node(charg[20],0,0)

'''N21,N22,N23,N24,N25=node(charg[21],xp[20],yp[20]),node(charg[22],xp[21],yp[21]),node(charg[23],xp[22],yp[22]),node(charg[24],xp[23],yp[23]),node(charg[25],xp[24],yp[24])
N26,N27,N28,N29,N30=node(charg[26],xp[25],yp[25]),node(charg[27],xp[26],yp[26]),node(charg[28],xp[27],yp[27]),node(charg[29],xp[28],yp[28]),node(charg[30],xp[29],yp[29])
N31,N32,N33,N34,N35=node(charg[31],xp[30],yp[30]),node(charg[32],xp[31],yp[31]),node(charg[33],xp[32],yp[32]),node(charg[34],xp[33],yp[33]),node(charg[35],xp[34],yp[34])
N36,N37,N38,N39,N40=node(charg[36],xp[35],yp[35]),node(charg[37],xp[36],yp[36]),node(charg[38],xp[37],yp[37]),node(charg[39],xp[38],yp[38]),node(charg[40],xp[39],yp[39])'''

N21,N22,N23,N24,N25=node(charg[21],200,250),node(charg[22],170,210),node(charg[23],260,380),node(charg[24],100,190),node(charg[25],140,320)
N26,N27,N28,N29,N30=node(charg[26],380,360),node(charg[27],130,170),node(charg[28],350,50),node(charg[29],250,300),node(charg[30],190,390)
N31,N32,N33,N34,N35=node(charg[31],300,130),node(charg[32],150,160),node(charg[33],210,40),node(charg[34],360,180),node(charg[35],290,30)
N36,N37,N38,N39,N40=node(charg[36],250,250),node(charg[37],130,350),node(charg[38],130,300),node(charg[39],350,150),node(charg[40],20,30)



#endnode
N41=node(400,400,400)

n=1

nodexpos=xp
nodeypos=yp


# Searching function starts here
def result():
	global visited
	data='''\t\t\t-----*****Result******-----\n\n\n\tTotal Nodes : %d \t\t Nodes visited: %d\n
	        \t\tNote : 0-Not visited   1-Visited\n\n\n
		Node 1 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 2 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 3 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 4 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 5 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 6 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 7 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 8 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 9 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 10 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 11 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 12 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 13 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 14 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 15 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 16 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 17 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 18 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 19 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 20 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 21 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 22 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 23 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 24 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 25 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 26 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 27 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 28 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 29 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 30 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 31 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 32 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 33 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 34 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 35 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 36 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 37 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 38 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 39 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 40 :  %d -->Time: %d sec 	---> Charge remaining : %s
		'''%(total_nodes,visited,N1.check,N1.times,N1.show(),N2.check,N2.times,N2.show(),N3.check,N3.times,N3.show(),N4.check,N4.times,N4.show(),N5.check,N5.times,N5.show(),N6.check,N6.times,N6.show(),N7.check,N7.times,N7.show(),N8.check,N8.times,N8.show(),N9.check,N9.times,N9.show(),N10.check,N10.times,N10.show(),N11.check,N11.times,N11.show(),N12.check,N12.times,N12.show(),N13.check,N13.times,N13.show(),N14.check,N14.times,N14.show(),N15.check,N15.times,N15.show(),N16.check,N16.times,N16.show(),N17.check,N17.times,N17.show(),N18.check,N18.times,N18.show(),N19.check,N19.times,N19.show(),N20.check,N20.times,N20.show(),N21.check,N21.times,N21.show(),N22.check,N22.times,N22.show(),N23.check,N23.times,N23.show(),N24.check,N24.times,N24.show(),N25.check,N25.times,N25.show(),N26.check,N26.times,N26.show(),N27.check,N27.times,N27.show(),N28.check,N28.times,N28.show(),N29.check,N29.times,N29.show(),N30.check,N30.times,N30.show(),N31.check,N31.times,N31.show(),N32.check,N32.times,N32.show(),N33.check,N33.times,N33.show(),N34.check,N34.times,N34.show(),N35.check,N35.times,N35.show(),N36.check,N36.times,N36.show(),N37.check,N37.times,N37.show(),N38.check,N38.times,N38.show(),N39.check,N39.times,N39.show(),N40.check,N40.times,N40.show())
	print(data)
	write_to_file(data)
def discharge_all():
	N1.discharge()
	N2.discharge()
	N3.discharge()
	N4.discharge()
	N5.discharge()
	N6.discharge()
	N7.discharge()
	N8.discharge()
	N9.discharge()
	N10.discharge()
	N11.discharge()
	N12.discharge()
	N13.discharge()
	N14.discharge()
	N15.discharge()
	N16.discharge()
	N17.discharge()
	N18.discharge()
	N19.discharge()
	N20.discharge()
	N21.discharge()
	N22.discharge()
	N23.discharge()
	N24.discharge()
	N25.discharge()
	N26.discharge()
	N27.discharge()
	N28.discharge()
	N29.discharge()
	N30.discharge()
	N31.discharge()
	N32.discharge()
	N33.discharge()
	N34.discharge()
	N35.discharge()
	N36.discharge()
	N37.discharge()
	N38.discharge()
	N39.discharge()
	N40.discharge()
file=open("Output.txt","w")
def write_to_file(data):
	global n
	now = time.asctime( time.localtime(time.time()))
	if n==1:
		a="*******Python Code**********\n\tOutput for Execution done on :"+now+"\n\n *** With charging ***"
		file.write(a)
	if n==0:
		a="*******Python Code**********\n\tOutput for Execution done on :"+now+"\n\n *** Without charging *** "
		file.write(a)
	file.write(data)
def searching(x,y,r,times):
	leftcheck()
	global visited
	global n
	if(N1.check!=1):
		z=math.sqrt((pow(N1.xpos-x,2))+pow(N1.ypos-y,2))
		if(z < (N1.radius+r)):
			w=("\t\tNode1 Found at [xpos:%s][ypos:%s]  \n\t\tNode1 -> Charge:%d"%(N1.xpos,N1.ypos,N1.charge))
			mfile.write("\n\n"+w)
			print(w)
			N1.check=1
			visited+=1
			N1.update_time(times)
			if N1.charge<40 and n==1:
				print("\t\tLow Battery...")
				N1.charger(N1.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N2.check!=1):
		z=math.sqrt((pow(N2.xpos-x,2))+pow(N2.ypos-y,2))
		if(z < (N2.radius+r)):
			w=("\t\tNode2 Found at [xpos:%s][ypos:%s]  \n\t\tNode2 -> Charge:%d"%(N2.xpos,N2.ypos,N2.charge))
			mfile.write("\n\n"+w)
			print(w)
			N2.check=1
			visited+=1
			N2.update_time(times)
			if N2.charge<40 and n==1:
				print("\t\tLow Battery...")
				N2.charger(N2.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N3.check!=1):
		z=math.sqrt((pow(N3.xpos-x,2))+pow(N3.ypos-y,2))
		if(z < (N3.radius+r)):
			w=("\t\tNode3 Found at [xpos:%s][ypos:%s]  \n\t\tNode3 -> Charge:%d"%(N3.xpos,N3.ypos,N3.charge))
			mfile.write("\n\n"+w)
			print(w)
			N3.check=1
			visited+=1
			N3.update_time(times)
			if N3.charge<40  and n==1:
				print("\t\tLow Battery...")
				N3.charger(N3.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N4.check!=1):
		z=math.sqrt((pow(N4.xpos-x,2))+pow(N4.ypos-y,2))
		if(z < (N4.radius+r)):
			w=("\t\tNode4 Found at [xpos:%s][ypos:%s]  \n\t\tNode4 -> Charge:%d"%(N4.xpos,N4.ypos,N4.charge))
			mfile.write("\n\n"+w)
			print(w)
			N4.check=1
			N4.update_time(times)
			visited+=1
			if N4.charge<40  and n==1:
				print("\t\tLow Battery...")
				N4.charger(N4.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N5.check!=1):
		z=math.sqrt((pow(N5.xpos-x,2))+pow(N5.ypos-y,2))
		if(z < (N5.radius+r)):
			w=("\t\tNode5 Found at [xpos:%s][ypos:%s]  \n\t\tNode5 -> Charge:%d"%(N5.xpos,N5.ypos,N5.charge))
			mfile.write("\n\n"+w)
			print(w)
			N5.check=1
			visited+=1
			N5.update_time(times)
			if N5.charge<40  and n==1:
				print("\t\tLow Battery...")
				N5.charger(N5.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N6.check!=1):
		z=math.sqrt((pow(N6.xpos-x,2))+pow(N6.ypos-y,2))
		if(z < (N6.radius+r)):
			w=("\t\tNode6 Found at [xpos:%s][ypos:%s]  \n\t\tNode6 -> Charge:%d"%(N6.xpos,N6.ypos,N6.charge))
			mfile.write("\n\n"+w)
			print(w)
			N6.check=1
			visited+=1
			N6.update_time(times)
			if N6.charge<40  and n==1:
				print("\t\tLow Battery...")
				N6.charger(N6.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N7.check!=1):
		z=math.sqrt((pow(N7.xpos-x,2))+pow(N7.ypos-y,2))
		if(z < (N7.radius+r)):
			w=("\t\tNode7 Found at [xpos:%s][ypos:%s]  \n\t\tNode7 -> Charge:%d"%(N7.xpos,N7.ypos,N7.charge))
			mfile.write("\n\n"+w)
			print(w)
			N7.check=1
			visited+=1
			N7.update_time(times)
			if N7.charge<40  and n==1:
				print("\t\tLow Battery...")
				N7.charger(N7.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N8.check!=1):
		z=math.sqrt((pow(N8.xpos-x,2))+pow(N8.ypos-y,2))
		if(z < (N8.radius+r)):
			w=("\t\tNode8 Found at [xpos:%s][ypos:%s]  \n\t\tNode8 -> Charge:%d"%(N8.xpos,N8.ypos,N8.charge))
			mfile.write("\n\n"+w)
			print(w)
			N8.check=1
			visited+=1
			N8.update_time(times)
			if N8.charge<40  and n==1:
				print("\t\tLow Battery...")
				N8.charger(N8.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N9.check!=1):
		z=math.sqrt((pow(N9.xpos-x,2))+pow(N9.ypos-y,2))
		if(z < (N9.radius+r)):
			w=("\t\tNode9 Found at [xpos:%s][ypos:%s]  \n\t\tNode9 -> Charge:%d"%(N9.xpos,N9.ypos,N9.charge))
			mfile.write("\n\n"+w)
			print(w)
			N9.check=1
			visited+=1
			N9.update_time(times)
			if N9.charge<40  and n==1:
				print("\t\tLow Battery...")
				N9.charger(N9.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N10.check!=1):
		z=math.sqrt((pow(N10.xpos-x,2))+pow(N10.ypos-y,2))
		if(z < (N10.radius+r)):
			w=("\t\tNode10 Found at [xpos:%s][ypos:%s]  \n\t\tNode10 -> Charge:%d"%(N10.xpos,N10.ypos,N10.charge))
			mfile.write("\n\n"+w)
			print(w)
			N10.check=1
			visited+=1
			N10.update_time(times)
			if N10.charge<40  and n==1:
				print("\t\tLow Battery...")
				N10.charger(N10.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N11.check!=1):
		z=math.sqrt((pow(N11.xpos-x,2))+pow(N11.ypos-y,2))
		if(z < (N11.radius+r)):
			w=("\t\tNode11 Found at [xpos:%s][ypos:%s]  \n\t\tNode11 -> Charge:%d"%(N11.xpos,N11.ypos,N11.charge))
			mfile.write("\n\n"+w)
			print(w)
			N11.check=1
			visited+=1
			N11.update_time(times)
			if N11.charge<40  and n==1:
				print("\t\tLow Battery...")
				N11.charger(N11.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N12.check!=1):
		z=math.sqrt((pow(N12.xpos-x,2))+pow(N12.ypos-y,2))
		if(z < (N12.radius+r)):
			w=("\t\tNode12 Found at [xpos:%s][ypos:%s]  \n\t\tNode12 -> Charge:%d"%(N12.xpos,N12.ypos,N12.charge))
			mfile.write("\n\n"+w)
			print(w)
			N12.check=1
			visited+=1
			N12.update_time(times)
			if N12.charge<40  and n==1:
				print("\t\tLow Battery...")
				N12.charger(N12.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N13.check!=1):
		z=math.sqrt((pow(N13.xpos-x,2))+pow(N13.ypos-y,2))
		if(z < (N13.radius+r)):
			w=("\t\tNode13 Found at [xpos:%s][ypos:%s]  \n\t\tNode13 -> Charge:%d"%(N13.xpos,N13.ypos,N13.charge))
			mfile.write("\n\n"+w)
			print(w)
			N13.check=1
			visited+=1
			N13.update_time(times)
			if N13.charge<40  and n==1:
				print("\t\tLow Battery...")
				N13.charger(N13.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N14.check!=1):
		z=math.sqrt((pow(N14.xpos-x,2))+pow(N14.ypos-y,2))
		if(z < (N14.radius+r)):
			w=("\t\tNode14 Found at [xpos:%s][ypos:%s]  \n\t\tNode14 -> Charge:%d"%(N14.xpos,N14.ypos,N14.charge))
			mfile.write("\n\n"+w)
			print(w)
			N14.check=1
			visited+=1
			N14.update_time(times)
			if N14.charge<40  and n==1:
				print("\t\tLow Battery...")
				N14.charger(N14.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N15.check!=1):
		z=math.sqrt((pow(N15.xpos-x,2))+pow(N15.ypos-y,2))
		if(z < (N15.radius+r)):
			w=("\t\tNode15 Found at [xpos:%s][ypos:%s]  \n\t\tNode15 -> Charge:%d"%(N15.xpos,N15.ypos,N15.charge))
			mfile.write("\n\n"+w)
			print(w)
			N15.check=1
			visited+=1
			N15.update_time(times)
			if N15.charge<40  and n==1:
				print("\t\tLow Battery...")
				N15.charger(N15.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N16.check!=1):
		z=math.sqrt((pow(N16.xpos-x,2))+pow(N16.ypos-y,2))
		if(z < (N16.radius+r)):
			w=("\t\tNode16 Found at [xpos:%s][ypos:%s]  \n\t\tNode16 -> Charge:%d"%(N16.xpos,N16.ypos,N16.charge))
			mfile.write("\n\n"+w)
			print(w)
			N16.check=1
			visited+=1
			N16.update_time(times)
			if N16.charge<40  and n==1:
				print("\t\tLow Battery...")
				N16.charger(N16.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N17.check!=1):
		z=math.sqrt((pow(N17.xpos-x,2))+pow(N17.ypos-y,2))
		if(z < (N17.radius+r)):
			w=("\t\tNode17 Found at [xpos:%s][ypos:%s]  \n\t\tNode17 -> Charge:%d"%(N17.xpos,N17.ypos,N17.charge))
			mfile.write("\n\n"+w)
			print(w)
			N17.check=1
			visited+=1
			N17.update_time(times)
			if N17.charge<40  and n==1:
				print("\t\tLow Battery...")
				N17.charger(N17.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N18.check!=1):
		z=math.sqrt((pow(N18.xpos-x,2))+pow(N18.ypos-y,2))
		if(z < (N18.radius+r)):
			w=("\t\tNode18 Found at [xpos:%s][ypos:%s]  \n\t\tNode18 -> Charge:%d"%(N18.xpos,N18.ypos,N18.charge))
			mfile.write("\n\n"+w)
			print(w)
			N18.check=1
			visited+=1
			N18.update_time(times)
			if N18.charge<40  and n==1:
				print("\t\tLow Battery...")
				N18.charger(N18.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N19.check!=1):
		z=math.sqrt((pow(N19.xpos-x,2))+pow(N19.ypos-y,2))
		if(z < (N19.radius+r)):
			w=("\t\tNode19 Found at [xpos:%s][ypos:%s]  \n\t\tNode19 -> Charge:%d"%(N19.xpos,N19.ypos,N19.charge))
			mfile.write("\n\n"+w)
			print(w)
			N19.check=1
			visited+=1
			N19.update_time(times)
			if N19.charge<40  and n==1:
				print("\t\tLow Battery...")
				N19.charger(N19.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N20.check!=1):
		z=math.sqrt((pow(N20.xpos-x,2))+pow(N20.ypos-y,2))
		if(z < (N20.radius+r)):
			w=("\t\tNode20 Found at [xpos:%s][ypos:%s]  \n\t\tNode20 -> Charge:%d"%(N20.xpos,N20.ypos,N20.charge))
			mfile.write("\n\n"+w)
			print(w)
			N20.check=1
			visited+=1
			N20.update_time(times)
			if N20.charge<40  and n==1:
				print("\t\tLow Battery...")
				N20.charger(N20.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N21.check!=1):
		z=math.sqrt((pow(N21.xpos-x,2))+pow(N21.ypos-y,2))
		if(z < (N21.radius+r)):
			w=("\t\tNode21 Found at [xpos:%s][ypos:%s]  \n\t\tNode21 -> Charge:%d"%(N21.xpos,N21.ypos,N21.charge))
			mfile.write("\n\n"+w)
			print(w)
			N21.check=1
			visited+=1
			N21.update_time(times)
			if N21.charge<40 and n==1:
				print("\t\tLow Battery...")
				N21.charger(N21.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N22.check!=1):
		z=math.sqrt((pow(N22.xpos-x,2))+pow(N22.ypos-y,2))
		if(z < (N22.radius+r)):
			w=("\t\tNode22 Found at [xpos:%s][ypos:%s]  \n\t\tNode22 -> Charge:%d"%(N22.xpos,N22.ypos,N22.charge))
			mfile.write("\n\n"+w)
			print(w)
			N22.check=1
			visited+=1
			N22.update_time(times)
			if N22.charge<40 and n==1:
				print("\t\tLow Battery...")
				N22.charger(N22.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N23.check!=1):
		z=math.sqrt((pow(N23.xpos-x,2))+pow(N23.ypos-y,2))
		if(z < (N23.radius+r)):
			w=("\t\tNode23 Found at [xpos:%s][ypos:%s]  \n\t\tNode23 -> Charge:%d"%(N23.xpos,N23.ypos,N23.charge))
			mfile.write("\n\n"+w)
			print(w)
			N23.check=1
			visited+=1
			N23.update_time(times)
			if N23.charge<40  and n==1:
				print("\t\tLow Battery...")
				N23.charger(N23.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N24.check!=1):
		z=math.sqrt((pow(N24.xpos-x,2))+pow(N24.ypos-y,2))
		if(z < (N24.radius+r)):
			w=("\t\tNode24 Found at [xpos:%s][ypos:%s]  \n\t\tNode24 -> Charge:%d"%(N24.xpos,N24.ypos,N24.charge))
			mfile.write("\n\n"+w)
			print(w)
			N24.check=1
			N24.update_time(times)
			visited+=1
			if N24.charge<40  and n==1:
				print("\t\tLow Battery...")
				N24.charger(N24.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N25.check!=1):
		z=math.sqrt((pow(N25.xpos-x,2))+pow(N25.ypos-y,2))
		if(z < (N25.radius+r)):
			w=("\t\tNode25 Found at [xpos:%s][ypos:%s]  \n\t\tNode25 -> Charge:%d"%(N25.xpos,N25.ypos,N25.charge))
			mfile.write("\n\n"+w)
			print(w)
			N25.check=1
			visited+=1
			N25.update_time(times)
			if N25.charge<40  and n==1:
				print("\t\tLow Battery...")
				N25.charger(N25.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N26.check!=1):
		z=math.sqrt((pow(N26.xpos-x,2))+pow(N26.ypos-y,2))
		if(z < (N26.radius+r)):
			w=("\t\tNode6 Found at [xpos:%s][ypos:%s]  \n\t\tNode6 -> Charge:%d"%(N26.xpos,N26.ypos,N26.charge))
			mfile.write("\n\n"+w)
			print(w)
			N26.check=1
			visited+=1
			N26.update_time(times)
			if N26.charge<40  and n==1:
				print("\t\tLow Battery...")
				N26.charger(N26.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N27.check!=1):
		z=math.sqrt((pow(N27.xpos-x,2))+pow(N27.ypos-y,2))
		if(z < (N27.radius+r)):
			w=("\t\tNode27 Found at [xpos:%s][ypos:%s]  \n\t\tNode27 -> Charge:%d"%(N27.xpos,N27.ypos,N27.charge))
			mfile.write("\n\n"+w)
			print(w)
			N27.check=1
			visited+=1
			N27.update_time(times)
			if N27.charge<40  and n==1:
				print("\t\tLow Battery...")
				N27.charger(N27.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N28.check!=1):
		z=math.sqrt((pow(N28.xpos-x,2))+pow(N28.ypos-y,2))
		if(z < (N28.radius+r)):
			w=("\t\tNode28 Found at [xpos:%s][ypos:%s]  \n\t\tNode8 -> Charge:%d"%(N28.xpos,N28.ypos,N28.charge))
			mfile.write("\n\n"+w)
			print(w)
			N28.check=1
			visited+=1
			N28.update_time(times)
			if N28.charge<40  and n==1:
				print("\t\tLow Battery...")
				N28.charger(N28.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N29.check!=1):
		z=math.sqrt((pow(N29.xpos-x,2))+pow(N29.ypos-y,2))
		if(z < (N29.radius+r)):
			w=("\t\tNode29 Found at [xpos:%s][ypos:%s]  \n\t\tNode9 -> Charge:%d"%(N29.xpos,N29.ypos,N29.charge))
			mfile.write("\n\n"+w)
			print(w)
			N29.check=1
			visited+=1
			N29.update_time(times)
			if N29.charge<40  and n==1:
				print("\t\tLow Battery...")
				N29.charger(N29.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N30.check!=1):
		z=math.sqrt((pow(N30.xpos-x,2))+pow(N30.ypos-y,2))
		if(z < (N30.radius+r)):
			w=("\t\tNode30 Found at [xpos:%s][ypos:%s]  \n\t\tNode10 -> Charge:%d"%(N30.xpos,N30.ypos,N30.charge))
			mfile.write("\n\n"+w)
			print(w)
			N30.check=1
			visited+=1
			N30.update_time(times)
			if N30.charge<40  and n==1:
				print("\t\tLow Battery...")
				N30.charger(N30.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N31.check!=1):
		z=math.sqrt((pow(N31.xpos-x,2))+pow(N31.ypos-y,2))
		if(z < (N31.radius+r)):
			w=("\t\tNode31 Found at [xpos:%s][ypos:%s]  \n\t\tNode11 -> Charge:%d"%(N31.xpos,N31.ypos,N31.charge))
			mfile.write("\n\n"+w)
			print(w)
			N31.check=1
			visited+=1
			N31.update_time(times)
			if N31.charge<40  and n==1:
				print("\t\tLow Battery...")
				N31.charger(N31.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N32.check!=1):
		z=math.sqrt((pow(N32.xpos-x,2))+pow(N32.ypos-y,2))
		if(z < (N32.radius+r)):
			w=("\t\tNode32 Found at [xpos:%s][ypos:%s]  \n\t\tNode12 -> Charge:%d"%(N32.xpos,N32.ypos,N32.charge))
			mfile.write("\n\n"+w)
			print(w)
			N32.check=1
			visited+=1
			N32.update_time(times)
			if N32.charge<40  and n==1:
				print("\t\tLow Battery...")
				N32.charger(N32.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N33.check!=1):
		z=math.sqrt((pow(N33.xpos-x,2))+pow(N33.ypos-y,2))
		if(z < (N33.radius+r)):
			w=("\t\tNode33 Found at [xpos:%s][ypos:%s]  \n\t\tNode33 -> Charge:%d"%(N33.xpos,N33.ypos,N33.charge))
			mfile.write("\n\n"+w)
			print(w)
			N33.check=1
			visited+=1
			N33.update_time(times)
			if N33.charge<40  and n==1:
				print("\t\tLow Battery...")
				N33.charger(N33.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N34.check!=1):
		z=math.sqrt((pow(N34.xpos-x,2))+pow(N34.ypos-y,2))
		if(z < (N34.radius+r)):
			w=("\t\tNode34 Found at [xpos:%s][ypos:%s]  \n\t\tNode14 -> Charge:%d"%(N34.xpos,N34.ypos,N34.charge))
			mfile.write("\n\n"+w)
			print(w)
			N34.check=1
			visited+=1
			N34.update_time(times)
			if N34.charge<40  and n==1:
				print("\t\tLow Battery...")
				N34.charger(N34.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N35.check!=1):
		z=math.sqrt((pow(N35.xpos-x,2))+pow(N35.ypos-y,2))
		if(z < (N35.radius+r)):
			w=("\t\tNode35 Found at [xpos:%s][ypos:%s]  \n\t\tNode15 -> Charge:%d"%(N35.xpos,N35.ypos,N35.charge))
			mfile.write("\n\n"+w)
			print(w)
			N35.check=1
			visited+=1
			N35.update_time(times)
			if N35.charge<40  and n==1:
				print("\t\tLow Battery...")
				N35.charger(N35.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N36.check!=1):
		z=math.sqrt((pow(N36.xpos-x,2))+pow(N36.ypos-y,2))
		if(z < (N36.radius+r)):
			w=("\t\tNode36 Found at [xpos:%s][ypos:%s]  \n\t\tNode16 -> Charge:%d"%(N36.xpos,N36.ypos,N36.charge))
			mfile.write("\n\n"+w)
			print(w)
			N36.check=1
			visited+=1
			N36.update_time(times)
			if N36.charge<40  and n==1:
				print("\t\tLow Battery...")
				N36.charger(N36.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N37.check!=1):
		z=math.sqrt((pow(N37.xpos-x,2))+pow(N37.ypos-y,2))
		if(z < (N37.radius+r)):
			w=("\t\tNode37 Found at [xpos:%s][ypos:%s]  \n\t\tNode17 -> Charge:%d"%(N37.xpos,N37.ypos,N37.charge))
			mfile.write("\n\n"+w)
			print(w)
			N37.check=1
			visited+=1
			N37.update_time(times)
			if N37.charge<40  and n==1:
				print("\t\tLow Battery...")
				N37.charger(N37.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N38.check!=1):
		z=math.sqrt((pow(N38.xpos-x,2))+pow(N38.ypos-y,2))
		if(z < (N38.radius+r)):
			w=("\t\tNode38 Found at [xpos:%s][ypos:%s]  \n\t\tNode18 -> Charge:%d"%(N38.xpos,N38.ypos,N38.charge))
			mfile.write("\n\n"+w)
			print(w)
			N38.check=1
			visited+=1
			N38.update_time(times)
			if N38.charge<40  and n==1:
				print("\t\tLow Battery...")
				N38.charger(N38.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N39.check!=1):
		z=math.sqrt((pow(N39.xpos-x,2))+pow(N39.ypos-y,2))
		if(z < (N39.radius+r)):
			w=("\t\tNode39 Found at [xpos:%s][ypos:%s]  \n\t\tNode19 -> Charge:%d"%(N39.xpos,N39.ypos,N39.charge))
			mfile.write("\n\n"+w)
			print(w)
			N39.check=1
			visited+=1
			N39.update_time(times)
			if N39.charge<40  and n==1:
				print("\t\tLow Battery...")
				N39.charger(N39.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N40.check!=1):
		z=math.sqrt((pow(N40.xpos-x,2))+pow(N40.ypos-y,2))
		if(z < (N40.radius+r)):
			w=("\t\tNode40 Found at [xpos:%s][ypos:%s]  \n\t\tNode20 -> Charge:%d"%(N40.xpos,N40.ypos,N40.charge))
			mfile.write("\n\n"+w)
			print(w)
			N40.check=1
			visited+=1
			N40.update_time(times)
			if N40.charge<40  and n==1:
				print("\t\tLow Battery...")
				N40.charger(N40.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N41.check!=1):
		N41.update_time(times)
r=Mobile_node_radius
def forward(y,r):
	global l
	global final
	l=[]
	for a in nr.arange(y,y+r,0.01):
		v=round(a,2)
		l.append(v)
	myFormattedList = [ float(Decimal('%.2f'% elem)) for elem in l ]
	z=round((r/400),2)*10 # deleted 10from the code
	while(D.ypos in myFormattedList):
		if(D.ypos<400):
			timer()
			D.ypos+=z
			D.ypos=round(D.ypos,2)
			D.xpos+=10
			time.sleep(0.5)
			searching(D.xpos,D.ypos,D.radius,times)
			discharge_all()
			a=("Mobile node postion of ypos: %r  xpos: %d "%(D.ypos,D.xpos))
			print(a,end="\r")
			final=times
		else:
			final=times
			break
	l.clear()
def backward(y,r):
	global l
	global final
	l=[]
	for a in nr.arange(y,y+r,0.01):
		v=round(a,2)
		l.append(v)
	myFormattedList = [ float(Decimal('%.2f'% elem)) for elem in l ]
	z=round((r/400),2)*10 # deleted 10from the code
	while(D.ypos in myFormattedList):
		if(D.ypos<400):
			timer()
			D.ypos+=z
			D.ypos=round(D.ypos,2)
			D.xpos-=10
			time.sleep(0.5)
			searching(D.xpos,D.ypos,D.radius,times)
			discharge_all()
			a=("Mobile node postion of ypos: %r  xpos: %d "%(D.ypos,D.xpos))
			print(a,end="\r")
			final=times
		else:
			final=times
			break
	l.clear()
def whennetworkstop():
	print('''*** Node dying time ***''')
	if N1.check!=0:
		print( ' Node 1 dies at %s sec'%round((N1.charge*2)+times))
	if N2.check!=0:
		print(' Node 2 dies at %s sec'%round((N2.charge*2)+times))
	if N3.check!=0:
		print(' Node 3 dies at %s sec'%round((N3.charge*2)+times))
	if N4.check!=0:
		print( ' Node 4 dies at %s sec'%round((N4.charge*2)+times))
	if N5.check!=0:
		print( ' Node 5 dies at %s sec'%round((N5.charge*2)+times))
	if N6.check!=0:
		print( ' Node 6 dies at %s sec'%round((N6.charge*2)+times))
	if N7.check!=0:
		print( ' Node 7 dies at %s sec'%round((N7.charge*2)+times))
	if N8.check!=0:
		print( ' Node 8 dies at %s sec'%round((N8.charge*2)+times))
	if N9.check!=0:
		print( ' Node 9 dies at %s sec'%round((N9.charge*2)+times))
	if N10.check!=0:
		print( ' Node 10 dies at %s sec'%round((N10.charge*2)+times))
	if N11.check!=0:
		print( ' Node 11 dies at %s sec'%round((N11.charge*2)+times))
	if N12.check!=0:
		print( ' Node 12 dies at %s sec'%round((N12.charge*2)+times))
	if N13.check!=0:
		print( ' Node 13 dies at %s sec'%round((N13.charge*2)+times))
	if N14.check!=0:
		print( ' Node 14 dies at %s sec'%round((N14.charge*2)+times))
	if N15.check!=0:
		print( ' Node 15 dies at %s sec'%round((N15.charge*2)+times))
	if N16.check!=0:
		print( ' Node 16 dies at %s sec'%round((N16.charge*2)+times))
	if N17.check!=0:
		print( ' Node 17 dies at %s sec'%round((N17.charge*2)+times))
	if N18.check!=0:
		print( ' Node 18 dies at %s sec'%round((N18.charge*2)+times))
	if N19.check!=0:
		print( ' Node 19 dies at %s sec'%round((N19.charge*2)+times))
	if N20.check!=0:
		print( ' Node 20 dies at %s sec'%round((N20.charge*2)+times))
	if N21.check!=0:
		print( ' Node 21 dies at %s sec'%round((N21.charge*2)+times))
	if N22.check!=0:
		print(' Node 22 dies at %s sec'%round((N22.charge*2)+times))
	if N23.check!=0:
		print(' Node 23 dies at %s sec'%round((N23.charge*2)+times))
	if N24.check!=0:
		print( ' Node 24 dies at %s sec'%round((N24.charge*2)+times))
	if N25.check!=0:
		print( ' Node 25 dies at %s sec'%round((N25.charge*2)+times))
	if N26.check!=0:
		print( ' Node 26 dies at %s sec'%round((N26.charge*2)+times))
	if N27.check!=0:
		print( ' Node 27 dies at %s sec'%round((N27.charge*2)+times))
	if N28.check!=0:
		print( ' Node 28 dies at %s sec'%round((N28.charge*2)+times))
	if N29.check!=0:
		print( ' Node 29 dies at %s sec'%round((N29.charge*2)+times))
	if N30.check!=0:
		print( ' Node 30 dies at %s sec'%round((N30.charge*2)+times))
	if N31.check!=0:
		print( ' Node 31 dies at %s sec'%round((N31.charge*2)+times))
	if N32.check!=0:
		print( ' Node 32 dies at %s sec'%round((N32.charge*2)+times))
	if N33.check!=0:
		print( ' Node 33 dies at %s sec'%round((N33.charge*2)+times))
	if N34.check!=0:
		print( ' Node 34 dies at %s sec'%round((N34.charge*2)+times))
	if N35.check!=0:
		print( ' Node 35 dies at %s sec'%round((N35.charge*2)+times))
	if N36.check!=0:
		print( ' Node 36 dies at %s sec'%round((N36.charge*2)+times))
	if N37.check!=0:
		print( ' Node 37 dies at %s sec'%round((N37.charge*2)+times))
	if N38.check!=0:
		print( ' Node 38 dies at %s sec'%round((N38.charge*2)+times))
	if N39.check!=0:
		print( ' Node 39 dies at %s sec'%round((N39.charge*2)+times))
	if N40.check!=0:
		print( ' Node 40 dies at %s sec'%round((N40.charge*2)+times))
# Execution starts
print("**** Mobile node starts ****")
forward(0,r)
backward(r,r)
forward(2*r,r)
backward(3*r,r)
forward(4*r,r)
result()
endtime=time.time()
exetime=endtime-starttime
file.write("Total time taken : %d sec"%final)
file.close()
mfile.close()
y10.append(N1.times)
y10.append(N2.times)
y10.append(N3.times)
y10.append(N4.times)
y10.append(N5.times)
y10.append(N6.times)
y10.append(N7.times)
y10.append(N8.times)
y10.append(N9.times)
y10.append(N10.times)
y10.append(N11.times)
y10.append(N12.times)
y10.append(N13.times)
y10.append(N14.times)
y10.append(N15.times)
y10.append(N16.times)
y10.append(N17.times)
y10.append(N18.times)
y10.append(N19.times)
y10.append(N20.times)
y10.append(N21.times)
y10.append(N22.times)
y10.append(N23.times)
y10.append(N24.times)
y10.append(N25.times)
y10.append(N26.times)
y10.append(N27.times)
y10.append(N28.times)
y10.append(N29.times)
y10.append(N30.times)
y10.append(N31.times)
y10.append(N32.times)
y10.append(N33.times)
y10.append(N34.times)
y10.append(N35.times)
y10.append(N36.times)
y10.append(N37.times)
y10.append(N38.times)
y10.append(N39.times)
y10.append(N40.times)
print('Node left time:\n*********************************')
lenn=len(nodename)
for v1,v2 in zip(lefttime,nodename):
	print("%s Left at the time : %d sec"%(v2,v1))
print('deleted : %d'%lenn)
effecting=int((40-lenn)/40*100)
print('\n\nefficiency of network: %d %%'%effecting)
valx=N26.check+N27.check+N28.check+N29.check+N30.check+N31.check+N32.check+N33.check+N34.check+N35.check+N36.check+N37.check+N38.check+N39.check+N40.check
balance=N1.check+N2.check+N3.check+N4.check+N5.check+N6.check+N7.check+N8.check+N9.check+N10.check+N11.check+N12.check+N13.check+N14.check+N15.check+N16.check+N17.check+N18.check+N19.check+N20.check+N21.check+N22.check+N23.check+N24.check+N25.check+valx
print('\n%d Nodes alive in network'%(80-lenn-balance))
whennetworkstop()
x10 = []
for w in range(1,41):
	x10.append(w)
plt.plot(x10, y10, color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='red', markersize=12)
plt.ylim(1,max(y10)+5)
plt.xlim(1,40)
plt.xlabel('Nodes in Network')
plt.ylabel('Time')
plt.title('Visit order of static node')
plt.show()
for plotx,ploty,node in zip(nodexpos,nodeypos,range(1,41)):
	plt1.text(plotx,ploty+5 ,node )
plt1.plot(nodexpos,nodeypos, 'ro')
plt1.axis([0,400, 0, 405])
plt1.xlabel('x- axis')
plt1.ylabel('y - axis')
plt1.title('Static node position')
plt1.show()
