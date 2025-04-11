D1={'ok':1,'nok':2}
D2={'ok':2,'new':3}
for i in D2:
    if i not in D1:
        D1[i]=D2[i]
print("D1_UNIOIN:",D1)     
D1 = {'ok': 1, 'nok': 2}
D_INTERSECTION={}
for i,j in D1.items():
    if i in D2:
        D_INTERSECTION[i]=j
print("D_INTERSECTION:",D_INTERSECTION) 

Difference={}
for key in D1.keys() - D2.keys():
    Difference[key]=D1[key]
print("D1-D2=",Difference)

 
for i, j in D1.items():
    if i not in D2:
       D2[i]=j
    else:
        D2[i]+=j        
        
print("D_MERGE:",(D2))  



