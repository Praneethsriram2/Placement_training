class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,ele):
        newnode=node(ele)
        if self.head is None:
            self.head=newnode
            print(f"{ele} is inserted at begin successfully")
            return
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
        print(f"{ele} inserted at begin successfully")
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp=self.head
        print("Double linked list is:",end=' ')
        while temp.next!=None:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)
    def insert_at_end(self,ele):
        newnode=node(ele)
        if self.head is None:
            self.head=newnode
            print(f"{ele} is inserted at end successfully")
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
        print(f"{ele} is inserted at end successfully")
    def insert_at_specific_pos(self,ele,pos):
        newnode=node(ele)
        if pos<1:
            print("Invalid position")
            return
        if self.head is None:
            print("Linked list is empty")
            return
        count=1
        temp=self.head
        while temp.next!=None and count<pos-1:
            temp=temp.next
            count+=1
        if temp.next is None:
            print("Invalid position")
            return
        newnode.next=temp.next
        temp.next.prev=newnode
        newnode.prev=temp
        temp.next=newnode
        print(f"{ele} inserted at position {pos} successfully")
    def delete_at_begin(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head.next.prev=None
        self.head=self.head.next
        print("Deleted at begin successfully")
    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            self.head=None
            print("Deleted at end successfully")
            return
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        print("Deleted at end successfully")
    def delete_at_specific_pos(self,pos):
        if self.head is None:
            print("Linked list is empty")
            return
        if pos<1:
            print("Invalid position")
            return
        if self.head.next==None and pos==1:
            self.head=None
            print(f"Deleted at posititon {pos} successfully")
            return
        if pos==1:
            self.head.next.prev=None
            self.head=self.head.next
            print(f"Deleted at position {pos} successfully")
            return
        temp=self.head
        count=1
        while temp.next!=None and count<pos-1:
            temp=temp.next
            count+=1
        if temp.next is None:
            print("Invalid position")
            return
        temp.next=temp.next.next
        if temp.next is not None:
            temp.next.prev=temp
        print(f"Deleted at position {pos} successfully")
    def display_reverse(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        print("Reversed linked list is:",end=' ')
        while temp.prev!=None:
            print(temp.data,end='->')
            temp=temp.prev
        print(temp.data)
    def even_odd_sub(self,even,odd,temp):
        if temp==None:
            return abs(even-odd)
        if int(temp.data)%2==0:
            even+=int(temp.data)
        elif int(temp.data)%2!=0:
            odd+=int(temp.data)
        return self.even_odd_sub(even,odd,temp.next)
    def prime_count(self,temp,c):
        if temp==None:
            return c
        k=2
        def prime(k,a):
            if a<2:
                return False
            if k==(a//2)+1:
                return True
            if (a)%k==0:
                return False
            return prime(k+1,a)
        if prime(k,temp.data):
            c+=1
        return self.prime_count(temp.next,c)
obj=dll()
while 1:
    print("1.Insert at begin\n2.Insert at end\n3.Insert at specific position\n4.Delete at begin\n5.Delete at end\n6.Delete at specific position\n7.Display\n8.Display reverse\n9.Even odd difference\n10.Primes in list\n11.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        ele=int(input("Enter the element:"))
        obj.insert_at_begin(ele)
    elif ch==2:
        ele=int(input("Enter the element:"))
        obj.insert_at_end(ele)
    elif ch==3:
        ele=int(input("Enter the element:"))
        pos=int(input("Enter the position to insert:"))
        obj.insert_at_specific_pos(ele,pos)
    elif ch==4:
        obj.delete_at_begin()
    elif ch==5:
        obj.delete_at_end()
    elif ch==6:
        pos=int(input("Enter the position to delete:"))
        obj.delete_at_specific_pos(pos)
    elif ch==7:
        obj.display()
    elif ch==8:
        obj.display_reverse()
    elif ch==9:
        print(obj.even_odd_sub(0,0,obj.head))
    elif ch==10:
        print(obj.prime_count(obj.head,0))
    elif ch==11:
        print("You are exited")
        break
    else:
        print("Invalid choice")