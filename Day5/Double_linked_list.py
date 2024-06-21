class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if self.head is None:
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.next=node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp=self.head
        print("Linked list is:",end=' ')
        while temp.next!=None:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)
        print("Reversed linked lis is:",end=' ')
        temp=self.tail
        while temp!=self.head:
            print(temp.data,end='->')
            temp=temp.prev
        print(temp.data)
    def addfront(self,x):
        newnode=node(x)
        if self.head is None:
            self.head=newnode
            self.tail=self.head
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def linear_search(self,se):
        if self.head is None:
            print("Linked list is empty")
            return
        flag=0
        temp1=self.head
        temp2=self.tail
        while temp1.next!=temp2 and temp1!=temp2:
            if temp1.data==se:
                print("Found")
                flag=1
                break
            temp1=temp1.next
            if temp2.data==se:
                print("Found")
                flag=1
                break
            temp2=temp2.prev
        if flag==0:
            print("Not found")
    def length(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            print("Odd")
            return
        t1=self.head
        t2=self.tail
        while t1!=None and t1.next!=None and t1.next!=t2 and t1!=t2:
            t1=t1.next.next
            t2=t2.prev.prev
        if (t1==None) or t1.next==t2:
            print("Even")
        else:
            print("Odd")
    #This function run for only even length linked list...
    def palindrome(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            print("Palindrome")
            return
        temp1=self.head
        temp2=self.tail
        flag=1
        while temp1.next!=temp2 and temp1!=temp2:
            if temp1.data!=temp2.data:
                flag=0
                break
            temp1=temp1.next
            temp2=temp2.prev
        if temp1.data!=temp2.data:
            flag=0
        if flag==1:
            print("Palindrome")
        else:
            print("Not palindrome")
    def rotate(self):
        if self.head is None:
            print("Linked list is empty")
            return
        t1=self.head
        t2=self.tail
        while t1.next!=t2:
            t1=t1.next
            t2=t2.prev
        #Below code for changing connections
        '''
        t1.next=None
        t2.prev=None
        t3=self.tail
        t3.next=self.head
        self.head.prev=t3
        self.head=t2
        self.tail=t1'''
        #Below code only swaps ths data, but not change the connections
        t3=self.head
        while t2!=None:
            t2.data,t3.data=t3.data,t2.data
            t2=t2.next
            t3=t3.next
        print("After rotating",end=' ')
        self.display()
    def interchange(self):
        if self.head is None:
            print("Linked list is empty")
            return
        t1=self.head
        t2=self.head.next
        self.head=t2
        p=t1.prev
        n=t2.next
        while t2!=self.tail:
            t1.next=n
            n.prev=t1
            t2.next=t1
            t2.prev=p
            if p!=None:
                p.next=t2
            t1.prev=t2
            t1=n
            t2=n.next
            p=t1.prev
            n=t2.next
        t1.next=n
        t2.next=t1
        t2.prev=p
        p.next=t2
        t1.prev=t2
        self.tail=t1
        self.display()
    def paranthesis(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp=self.head
        res=1
        s=[]
        flag=1
        temp=self.head
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
            print(res)
        else:
            print(-1)    
obj=dll()
l=input("Enter the input:")
for i in l:
    obj.addback(i)
obj.display()
obj.paranthesis()