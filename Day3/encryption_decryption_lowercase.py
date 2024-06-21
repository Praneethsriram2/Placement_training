s=input("Enter a string:")
target=int(input("Enter a number:"))
low=97
high=122
res=''
target=target%26
for i in s:
    l=abs(ord(i)-(target))
    if low<=l<=high:
        res+=chr(l)
    else:
        z=target-(ord(i)-low)
        l=abs((high+1)-z)
        res+=chr(l)
print(res)