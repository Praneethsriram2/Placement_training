class node:
    def __init__(self):
        self.data={}
        self.flag=0
class trie:
    def __init__(self):
        self.head=node()
    def insert(self,ele):
        temp=self.head
        for i in ele:
            if i not in temp.data:
                temp.data[i]=node()
                print(temp.data)
            temp=temp.data[i]
        temp.flag=1
        print(temp.flag)
    def prefix(self,word):
        if not self.head:
            print("Dictionary is empty")
            return
        flag=1
        temp=self.head
        for i in word:
            if i not in temp.data:
                flag=0
            else:
                temp=temp.data[i]
        if flag==1:
            print(True)     
        else:
            print(False)
    def search(self,se):
        if not self.head:
            print("Dictionary is empty")
            return
        flag=1
        temp=self.head
        for i in se:
            if i not in temp.data:
                flag=0
            else:
                temp=temp.data[i]
        if flag==1 and temp.flag==1:
            print(True)
        else:
            print(False)
    def search_engine(self,pre,res):
        if not self.head:
            print("Dictionary is empty")
            return
        flag=1
        temp=self.head
        for i in pre:
            if i not in temp.data:
                flag=0
            else:
                temp=temp.data[i]
        if flag==1:
            print(True)
            return self.search_engine2(pre,temp,res)
        else:
            print(False)
    def search_engine2(self,pre,temp,l):
        if temp.flag==1:
            l.append(pre)
        for i in temp.data:
            l=self.search_engine2(pre+i,temp.data[i],l)
        return l
obj=trie()
while 1:
    print("1.Insert\n2.search\n3.Prefix\n4.Search engine\n5.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        ele=input("Enter the element:")
        obj.insert(ele)
    elif ch==2:
        word=input("Enter the search element:")
        obj.search(word)
    elif ch==3:
        se=input("Enter the word to search:")
        obj.prefix(se)
    elif ch==4:
        res=[]
        tot=int(input("Enter the total no.of prefixes:"))
        for i in range(tot):
            pre=input("Enter the prefix:")
            res=obj.search_engine(pre,res)
        print("All possible words with the given prefix is:",res)
        ans=''
        mx=-9999
        for i in res:
            if len(i)>mx:
                mx=len(i)
                ans=i
        print("Longest word with given prefix is:",ans)
        print("Lexicographically smaller word with given prefix is:",min(res))
    elif ch==5:
        print("You are exited")
        break
    else:
        print("Invalid choice")