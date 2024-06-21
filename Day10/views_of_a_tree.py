class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,root,ele):
        if self.root is None:
            self.root=node(ele)
        elif ele==root.data:
            return "Duplicated can't be taken"
        elif ele<root.data:
            if root.left:
                self.insert(root.left,ele)
            else:
                root.left=node(ele)
        else:
            if root.right:
                self.insert(root.right,ele)
            else:
                root.right=node(ele)
    def inorder(self,root):
        if self.root is None:
            return "Tree is empty"
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    def left_view(self,root,c,s):
        if self.root is None:
            return "Tree is empty"
        if root==None:
            return s
        if c>=len(s):
            s.append(root.data)
        self.left_view(root.left,c+1,s)
        self.left_view(root.right,c+1,s)
        return s
    def right_view(self,root,c,s):
        if self.root is None:
            return "Tree is empty"
        if root==None:
            return s
        if c>=len(s):
            s.append(root.data)
        else:
            s[c]=root.data
        self.right_view(root.left,c+1,s)
        self.right_view(root.right,c+1,s)
        return s
    def top_view(self,d,q,l):
        if self.root is None:
            return "Tree is empty"
        while q:
            root=q[0][0]
            if (q[0][0]).left:
                q.append([root.left,q[0][1]-1])
            if (q[0][0]).right:
                q.append([root.right,q[0][1]+1])
            r=q.pop(0)
            if r[1] not in d:
                d[r[1]]=r[0].data
        return d
    def bottom_view(self,d,q,l):
        if self.root is None:
            return "Tree is empty"
        while q:
            root=q[0][0]
            if (q[0][0]).left:
                q.append([root.left,q[0][1]-1])
            if (q[0][0]).right:
                q.append([root.right,q[0][1]+1])
            r=q.pop(0)
            d[r[1]]=r[0].data
        return d
obj=bst()
while 1:
    print("\n1.Insert\n2.Inorder\n3.Left view\n4.Right view\n5.Top view\n6.Bottom view\n7.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        l=list(map(int,input("Enter the elements:").split()))
        for i in l:
            obj.insert(obj.root,i)
    elif ch==2:
        obj.inorder(obj.root)
    elif ch==3:
        print(obj.left_view(obj.root,0,[]))
    elif ch==4:
        print(obj.right_view(obj.root,0,[]))
    elif ch==5:
        print(obj.top_view({},[[obj.root,0],],0))
    elif ch==6:
        print(obj.bottom_view({},[[obj.root,0],],0))
    elif ch==7:
        print("You are exited")
        break
    else:
        print("Invalid choice")