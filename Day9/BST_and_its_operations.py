class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,temp,ele):
        if self.root is None:
            self.root=node(ele)
        elif temp.data==ele:
            print("Same elements cannot be taken")
            return
        elif ele<temp.data:
            if temp.left:
                self.insert(temp.left,ele)
            else:
                temp.left=node(ele)
        else:
            if temp.right:
                self.insert(temp.right,ele)
            else:
                temp.right=node(ele)
    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data,end=' ')
            self.inorder(temp.right)
    def preorder(self,temp):
        if temp:
            print(temp.data,end=' ')
            self.preorder(temp.left)
            self.preorder(temp.right)
    def postorder(self,temp):
        if temp:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data,end=' ')
    def find_min(self,temp):
        while temp.left!=None:
            temp=temp.left
        return temp.data
    def search(self,root,se):
        if self.root is None:
            print("Tree is empty")
            return
        if root is None:
            return False
        elif se==root.data:
            return True
        elif se<root.data:
            return self.search(root.left,se)
        elif se>root.data:
            return self.search(root.right,se)
        else:
            return False
    def sum_nodes(self,root,c):
        '''
        if root:
            c=self.sum_nodes(root.left,c)
            c+=root.data
            c=self.sum_nodes(root.right,c)
        return c'''
        if not root:
            return 0
        return self.sum_nodes(root.left,c)+self.sum_nodes(root.right,c)+c+root.data
    def add_even(self,root,c):
        if not root:
            return 0
        if (root.data)%2==0:
            return self.add_even(root.left,c)+self.add_even(root.right,c)+c+root.data
        else:
            return self.add_even(root.left,c)+self.add_even(root.right,c)
    def add_odd(self,root,c):
        if not root:
            return 0
        if (root.data)%2!=0:
            return self.add_odd(root.left,c)+self.add_odd(root.right,c)+c+root.data
        else:
            return self.add_odd(root.left,c)+self.add_odd(root.right,c)
    def even_odd_dif(self,root,c):
        if not root:
            return 0
        if (root.data)%2!=0:
            return self.even_odd_dif(root.left,c)+self.even_odd_dif(root.right,c)+c+root.data
        else:
            return abs(self.even_odd_dif(root.left,c)+self.even_odd_dif(root.right,c)+c-root.data)
    def height(self,temp,c):
        if not temp:
            return c-1
        return max((self.height(temp.left,c+1)),self.height(temp.right,c+1))
    def balanced(self,root):
        return abs(self.height(root.left,0)-(self.height(root.right,0)))<=1
    def leaf_node_count(self,root,c):
        if not root:
            return 0
        if root.left is None and root.right is None:
            c+=1
            return c
        return self.leaf_node_count(root.left,c)+self.leaf_node_count(root.right,c)
    def leaf_node_sum(self,root,k):
        if not root:
            return 0
        if root.left is None and root.right is None:
            k+=root.data
            return k
        return self.leaf_node_sum(root.left,k)+self.leaf_node_sum(root.right,k)
    def depth(self,root,ele):
        if self.root is None:
            print("Tree is empty")
            return
        def depth2(root,ele,c):
            if root is None:
                return False
            elif ele==root.data:
                return c
            elif ele<root.data:
                return depth2(root.left,ele,c+1)
            elif ele>root.data:
                return depth2(root.right,ele,c+1)
            else:
                return False
        if self.search(self.root,ele):
            return depth2(self.root,ele,0)
        else:
            return False
obj=bst()
while 1:
    print("\n1.Insert\n2.Inorder\n3.Preorder\n4.Postorder\n5.Minimum node\n6.Search\n7.Add all nodes\n8.Add even\n9.Add odd\n10.Diff blw even and odd nodes\n11.Height of tree\n12.Check tree is balanced\n13.No.of leaf nodes\n14.Sum of leaf nodes\n15.Depth of the given node\n16.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        l=list(map(int,input("Enter the elements:").split()))
        for i in l:
            obj.insert(obj.root,i)
    elif ch==2:
        obj.inorder(obj.root)
    elif ch==3:
        obj.preorder(obj.root)
    elif ch==4:
        obj.postorder(obj.root)
    elif ch==5:
        print("Minimum node is:",obj.find_min(obj.root))
    elif ch==6:
        se=int(input("Enter the element to search:"))
        if obj.search(obj.root,se):
            print(True)
        else:
            print(False)
    elif ch==7:
        print("Sum of all nodes is:",obj.sum_nodes(obj.root,0))
    elif ch==8:
        print("Sum of even data nodes is",obj.add_even(obj.root,0))
    elif ch==9:
        print("Sum of odd data nodes is:",obj.add_odd(obj.root,0))
    elif ch==10:
        print("Diff b/w even and odd sum is:",obj.even_odd_dif(obj.root,0))
    elif ch==11:
        print("Height of tree is:",obj.height(obj.root,0))
    elif ch==12:
        if obj.balanced(obj.root):
            print(True)
        else:
            print(False)
    elif ch==13:
        print("Leaf node count is:",obj.leaf_node_count(obj.root,0))
    elif ch==14:
        print("Sum of data of leaf nodes is:",obj.leaf_node_sum(obj.root,0))
    elif ch==15:
        ele=int(input("Enter a number from the tree:"))
        print(f"Depth of {ele} is:{obj.depth(obj.root,ele)}")
    elif ch==16:
        print("You are exited")
        break
    else:
        print("Invalid choice")