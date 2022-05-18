l=[]
temp=[]
output=[]
for i in range(1,n+1):
    l.append(i)
for j in range(len(l)):
    if l[j]==target[j]:
        temp.append(l[j])
        output.append("Push")
    else:
        temp.append(l[j])
        temp.pop()
        output.append("Pop")
        if temp==target:
            return output