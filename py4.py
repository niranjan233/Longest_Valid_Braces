def check(a,b):
    return True if (a=='(' and b==')') or (a=='[' and b==']') or (a=='{' and b=='}')  else False
s=input()
max=0
l=len(s)
count=0
k=0
while k in range (l-1):
    count+=1
    print("time",count)
    c=0
    i=k
    j=i+1
    c1=1
    if check(s[i],s[j]):
        print(i,j)
        c+=2
        print("Current count",c)
        while c1!=c and (c!=l if l%2==0 else c!=l-1) and j!=l:
            count+=1
            print("time",count)
            c1=c
            if j+2<l and check(s[j+1],s[j+2]):
                print(j+1,j+2)
                j+=2
                c+=2
                print("Current counting",c)
            elif i>0 and j+1<l and check(s[i-1],s[j+1]):
                print(i,j)
                i-=1
                j+=1
                c+=2
                print("Current counter",c)
            if c>max:
                max=c
        k=j
    k+=1
print(max)
        
        
