#this code is created to detect a figure that is a triangle or not by entering the figure angles
#define an array to put angles in
angles=[]
#enter angles with a space between them then press enter
a,b,c=input('enter your figure angles with a space between them. then press enter to be detected if it is a triangle :  ').split()
#convert text to integer
a,b,c=int(a),int(b),int(c)
angles.append(a)
angles.append(b)
angles.append(c)
if angles.count(0)==0 and sum(angles)==180:
    print("the figure is triangle")
else:
    print("it is not a triangle!")    
