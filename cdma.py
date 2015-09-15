Cs=-4
X=0
Y=0

Ad=input("Enter Ad :")
if Ad == 0:
 Ad=-1
else :
 Ad=1 
Bd=input("Enter Bd :")
if Bd==0:
 Bd=-1
else :
 Bd=1
s = raw_input("Enter Ak :")
Ak = map(int, s.split())
Ak.insert(0,-1)

#Removing the extra -1 i am getting
del(Ak[0])

print Ak
s = raw_input("Enter Bk :")
Bk = map(int, s.split())
Bk.insert(0,-1)

#Removing the extra -1 i am getting
del(Bk[0])


for n in Ak:
 As=n*Ad
 X=Cs*As+X
for n in Bk:
 Bs=n*Bd
 Y=Cs*Bs+Y
if X>Y:
 print "X is bigger, hence we select channel A"
else :
 print "Y is bigger, hence we select channel B"
