class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,ele):
        newnode=node(ele)
        if self.head is None:
            self.head=newnode
            print(f"{ele} inserted at begin successfully")
            return
        newnode.next=self.head
        self.head=newnode
        print(f"{ele} inserted at begin successfully")
    def insert_at_end(self,ele):
        newnode=node(ele)
        if self.head is None:
            self.head=newnode
            print(f"{ele} inserted at end successfully")
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        print(f"{ele} inserted at end successfully")
    def insert_at_specific_pos(self,ele,pos):
        if pos<1:
            print("Invalid position")
            return
        newnode=node(ele)
        if self.head is None:
            print("Linked list is empty")
            return
        temp=self.head
        count=1
        if pos==1:
            newnode.next=self.head
            self.head=newnode
            print(f"{ele} is inserted at position {pos} successfully")
            return
        while temp.next!=None and count<pos-1:
            temp=temp.next
            count+=1
        if temp.next==None:
            print("Invalid position")
            return
        newnode.next=temp.next
        temp.next=newnode
        print(f"{ele} inserted at position {pos} successfully")
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        print("Linked list is:")
        temp=self.head
        while temp.next!=None:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)
    def delete_at_begin(self):
        if self.head is None:
            print("Linked list is empty")
            return
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
            print("Linked list empty")
            return
        if pos<1:
            print("Invalid position")
            return
        temp=self.head
        count=1
        if pos==1:
            self.head=self.head.next
            print(f"Deleted at position {pos} successfully")
            return
        while temp.next is not None and count<pos-1:
            count+=1
            temp=temp.next
        if temp.next is None:
            print("Invalid position")
            return
        temp.next=temp.next.next
        print(f"Deleted at positon {pos} successfully")
    def display_reverse(self):
        if self.head is None:
            print("Linked list is empty")
            return
        next=None
        prev=None
        curr=self.head
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        print("Reversed",end=' ')
        self.display()
        next=None
        prev=None
        curr=self.head
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
    def middle(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp1=self.head
        temp2=self.head
        prev=None
        while temp2!=None and temp2.next!=None:
            prev=temp1
            temp2=temp2.next.next
            temp1=temp1.next
        if temp2==None:
            print(f"Middle nodes are:{prev.data,temp1.data}")
            return
        print(f"Middle node is:{temp1.data}")
    def length(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp1=self.head
        temp2=self.head
        c=1
        while temp2!=None and temp2.next!=None:
            temp2=temp2.next.next
            temp1=temp1.next
            c+=2
        if temp2==None:
            c-=1
            print(f"Length of linked list is even {c}")
            return
        print(f"Length of linked list is odd {c}")
    def max_length(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp=self.head
        mx1,mx2=1,1
        while temp.next!=None:
            if (int(temp.next.data)-int(temp.data))==1:
                mx1+=1
            else:
                if mx1>mx2:
                    mx2=mx1
                mx1=1
            temp=temp.next
        print(f"Maximum length of consecutive elements is:{mx2}")
    def pairs(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp1=self.head
        while temp1!=None:
            temp2=temp1.next
            while temp2!=None:
                print(temp1.data,end='')
                print(temp2.data)
                temp2=temp2.next
            temp1=temp1.next
    def bubble_sort(self):
        if self.head is None:
            print("Linked list is empty")
            return
        c=0
        temp1=self.head
        while temp1:
            flag=0
            temp2=self.head
            while temp2.next:
                if int(temp2.next.data)<int(temp2.data):
                    flag=1
                    temp2.data,temp2.next.data=temp2.next.data,temp2.data
                    c+=1
                temp2=temp2.next
            if flag==0:
                break
            temp1=temp1.next
        print(f"Total iterations are:{c}")
        print("After bubble sort is:",end=' ')
        self.display()
obj=sll()
while 1:
    print("1.Insert at begin\n2.Insert at end\n3.Insert at specific position\n4.Delete at begin\n5.Delete at end\n6.Delete at specific position\n7.Display\n8.Display reversed linked list\n9.Middle node\n10.Even or odd length\n11.Max length of cons ele\n12.All possible pairs\n13.Bubble sort\n14.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        ele=input("Enter the element:")
        obj.insert_at_begin(ele)
    elif ch==2:
        ele=input("Enter the element:")
        obj.insert_at_end(ele)
    elif ch==3:
        ele=input("Enter the element:")
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
        obj.middle()
    elif ch==10:
        obj.length()
    elif ch==11:
        obj.max_length()
    elif ch==12:
        obj.pairs()
    elif ch==13:
        obj.bubble_sort()
    elif ch==14:
        print("You are exited")
        break
    else:
        print("Invalid choice")