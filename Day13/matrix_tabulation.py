"""
ip:-
    given 2 strings
    abcd
    axbdc
op:-
    print all the sub sequence
    abcd-a,ab,ac,ad,abc,abd,abcd,b,bc,bd,bcd,c,cd,d
"""
'''
res=[]
def all_sub_sequence(s,res_s):
    if res_s not in res:
        res.append(res_s)
    if not s:
        return
    all_sub_sequence(s[1:],res_s+s[0])
    all_sub_sequence(s[1:],res_s)
def sub_sequence(s):
    for i in range(len(s)):
        all_sub_sequence(s[i+1:],s[i])
s="abcdx"
sub_sequence(s)
print(res)'''
s1='abcd'
s2='axbdc'
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])
for i in m:
    print(i)
res=''
u=len(s1)
v=len(s2)
while u!=0 and v!=0:
    if s1[u-1]==s2[v-1]:
        res+=s1[u-1]
        u-=1
        v-=1
    else:
        if m[u][v]==m[u-1][v]:
            u-=1
        else:
            v-=1
print("".join(reversed(res)))