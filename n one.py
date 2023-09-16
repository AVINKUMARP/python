a=str(input("enter the word:"))

# while True:
#  print(len(a))
#  break
i=0
l=''
d={}
count=0
while i<=len(a)-1:
    if a[i] in l:
        count+=1
        l+=a[i]
        d[a[i]]=count
    else:
        count=1
        l+=a[i]
        d[a[i]]=count
    i=i+1
print(d)
        
    
     