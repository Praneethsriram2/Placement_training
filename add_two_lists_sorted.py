l1=list(map(int,input("Enter the elements:").split()))
l2=list(map(int,input("Enter the elements:").split()))
l3=[]
'''l3=l1+l2
l3.sort() #or print(sorted(l1+l2))
print("List after 2 lists are merged is:",l3)'''
n1=len(l1)
n2=len(l2)
i=0
j=0
while (i<n1 or j<n2):
    if i<n1 and j<n2:
        if l1[i]<l2[j]:
            l3.append(l1[i])
            i+=1
        elif l1[i]>l2[j]:
            l3.append(l2[j])
            j+=1
        else:
            l3.append(l1[i])
            l3.append(l2[j])
            i+=1
            j+=1
    elif i>=n1 and j<n2:
        l3.append(l2[j])
        j+=1
    else:
        l3.append(l1[i])
        i+=1
print("Sorted list after adding two lists is:",l3)