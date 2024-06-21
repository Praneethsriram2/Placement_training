'''
ip:-
    string:- school
    n=3
    operation 1:- L 2 rotate left by 2 to string
    operation 2:- R 3 rotate right by 3 to string
    operation 3:- L 1 rotate left by 1 to string
    take first letters of each output
    and check whether it is an anagram of the subsequence string
op:-
    yes or no '''
l=input("Enter the input:")
n=int(input("Enter a number(queries):"))
q=[]
for i in range(n):
    z=input("Enter the input:")
    q.append(z)
res=[]
for i in range(len(q)):
    if q[i][0]=='L':
        a=l[int(q[i][1:]):]
        res.append(a)
    elif q[i][0]=='R':
        a=l[-(int(q[i][1:])):]
        res.append(a)
ans=''
for i in res:
    ans+=i[0]
ans=''.join(sorted(ans))
print(ans)
st=[]
for i in range(len(l)-(len(ans)-1)):
    st.append(l[i:i+len(ans)])
for i in st:
    i="".join(sorted(i))
print(st)
flag=0
for i in st:
    if ans in st:
        flag=1
if flag==1:
    print(True)
else:
    print(False)