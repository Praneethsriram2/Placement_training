class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def paranthesis(head):
    if head is None:
        print("Linked list is empty")
        return
    temp=head
    res=1
    s=[]
    flag=1
    temp=head
    while temp:
        if temp.data=='(' or temp.data=='{' or temp.data=='[':
            s.append(temp.data)
        elif s:
             if (temp.data==']' and s[-1]=='[') or (temp.data=='}' and s[-1]=='{') or (temp.data==')' and s[-1]=='('):
                s.pop()
             else:
                flag=0
                break
        else:
            flag=0
            break
        res+=1
        temp=temp.next
    if flag==0:
        return res
    else:
        return -1
l=input("Enter the input:")
head=node(l[0])
temp=head
pre=None
for i in range(1,len(l)):
    pre=temp
    temp.next=node(l[i])
    temp=temp.next
    temp.prev=pre
print(paranthesis(head))