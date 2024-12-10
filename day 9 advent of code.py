s = "12345"
e =0
l= []
j = 0
idn = 0
space = "space"
for i in s:
    if (e%2==0):
        while j < int(i):
           l.append(idn)
           j = j+1
        idn+=1
    else:
        while j< int(i):
           l.append(space)
           j = j+1
    e += 1
    j = 0
print(l)
print(len(l))
p = 0
indexa = 0
for i in range(0,len(l)):
    print
    indexa += 1
    if l[i] != "space":
        continue
    else:
        for j in range(len(l)-1,-1,-1):
           if l[j] != "space"and j> i:
                             p = l[j]
                             l[j] = l[i]
                             l[i] = p
                             print(l)
                             break
print(l)
print(1)
sum = 0
u = 0
for i in range(0,len(l)):           
             if l[i]=="space":
                 break
             sum += l[i]*i
             u= u+1
print(sum)