t=17
c=[2,3,4,5]
'''
s=[]
for i in range(len(c)):
    l=[]
    for j in range(t+1):
        l.append(0)
    s.append(l)'''
s=[[0 for i in range(t+1)]for j in range(len(c))]
for i in s:
    print(i)
for i in range(1):
    for j in range(1,t+1):
        if j%c[i]==0:
            s[i][j]=j//c[i]
print()
for i in s:
    print(i)
print()
for i in range(1,len(c)):
    for j in range(1,t+1):
        if j%c[i]==0:
            s[i][j]=j//c[i]
        elif j<s[i][j]:
            s[i][j]=s[i-1][j]
        else:
            l=abs(j-c[i])
            if s[i][l]!=0:
                s[i][j]=s[i][l]+1
            else:
                s[i][j]=s[i-1][j]
for i in s:
    print(i)
print(f"Minimum coins to make {t} is:{s[-1][-1]}")
'''
#Nithin code->only one list keeps updated...
l=[3,4]
cost=5
sir_tab=[-1 for i in range(cost+1)]
print()
print("Sir Tabulation Sheet:-")
print(sir_tab)
sir_tab[0]=0
for i in l:
    for j in range(i,cost+1):
        if j%i==0:
            sir_tab[j]=j//i
        if sir_tab[j-i]!=-1:
            sir_tab[j]=1+sir_tab[j-i]
print(sir_tab)
print(sir_tab[-1])'''