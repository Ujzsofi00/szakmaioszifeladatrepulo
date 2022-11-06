import random

#1.

Tlista=[]

for i in range(0,20):
    Tlista.append(random.randint(0,9))

print(Tlista) 

#2.

maxmagassag=0

for mag in Tlista:
    if(maxmagassag<mag):
        maxmagassag=mag

print(maxmagassag) 

#3.

minmagassag=9

for mag in Tlista:
    if(minmagassag!=0):
        if(minmagassag>mag):
            minmagassag=mag
     


#4.

dbviz=0

for mag in Tlista:
    if(mag==0):
        dbviz+=1

if(dbviz>10):
    print("Több van a vízből.")
elif(dbviz==10):
    print("Ugyanannyivíz és sziget van.")
else:
    print("Több van a szárazföldből.")                