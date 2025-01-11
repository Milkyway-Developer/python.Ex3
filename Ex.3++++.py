a = input()
e=0
o=0
for i in a :
    if i.isdigit() and int(i)%2==0:
        e+=1
    if i.isdigit() and int(i)%2==1:
            o+=1       
print(e)
print(o)