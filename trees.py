class Node:
    def __init__(self, content):
        self.lchild = None
        self.rchild = None
        #self.parent = None
        self.content = content

    def printTree(self):
        if self.lchild:
            self.lchild.printTree()
        print(self.content)
        if self.rchild:
            self.rchild.printTree()

    def insert(self, data):
        if self.content:
            if data < self.content:
                if self.lchild is None:
                    self.lchild = Node(data)
                    self.lchild.parent = self
                
                else:
                    self.lchild.insert(data)

            elif data >= self.content:
                if self.rchild is None:
                    self.rchild = Node(data)
                    self.rchild.parent = self

                else:
                    self.rchild.insert(data)

        else:
            self.content = data

    def search(self, number):
        if number == self.content:
            print("value found")
        elif number > self.content:
            if self.rchild is None:
                print("value not found")
            else:
                self.rchild.search(number)
        elif number < self.content:
            if self.lchild is None:
                print("value not found")
            else:
                self.lchild.search(number)

"""
    def successor(self, number):
        if number == self.content:
            if self.rchild:
                temp = self.rchild
                while(temp is not None):
                    if temp.lchild is None:
                        break
                    temp = temp.lchild

                print(temp.content)

            else:
                p = self.parent
                while(p is not None):
                    if self != p.rchild:
                        break
                    p = p.parent
                print(self.parent)

        elif number > self.content:
            if self.rchild is None:
                print("value not found")
            else:
                self.rchild.successor(number)

        elif number < self.content:
            if self.lchild is None:
                print("value not found")
            else:
                self.lchild.successor(number)

    def predecessor(self, number):
        if number == self.content:
            if self.lchild:
                if self.lchild.rchild:
                    temp = self.lchild.rchild
                    while(temp is not None):
                        if temp.rchild is None:
                            break
                        temp = temp.rchild

                    print(temp.content)

                else:
                    print(self.lchild.content)

            else:
                print(self.parent.content)
                p = self.parent
                while(p is not None):
                    if self != p.rchild:
                        break
                    p = p.parent
                print(p.content)
                
        elif number > self.content:
            if self.rchild is None:
                print("value not found")
            else:
                self.rchild.predecessor(number)
                
        elif number < self.content:
            if self.lchild is None:
                print("value not found")
            else:
                self.lchild.predecessor(number)
                """


            

def findPreAndSuc(root, key): 

    if root is None: 
        return
  
    if root.content == key: 
  
        if root.lchild is not None: 
            tmp = root.lchild  
            while(tmp.rchild): 
                tmp = tmp.rchild  
            findPreAndSuc.pre = tmp 
  
        if root.rchild is not None: 
            tmp = root.rchild 
            while(tmp.lchild): 
                tmp = tmp.lchild  
            findPreAndSuc.suc = tmp  
  
        return 
  
    if root.content > key : 
        findPreAndSuc.suc = root  
        findPreAndSuc(root.lchild, key) 
  
    else: 
        findPreAndSuc.pre = root 
        findPreAndSuc(root.rchild, key) 

root = Node(None)
root.insert(5)
root.insert(2)
root.insert(7)
root.insert(1)
root.insert(3)
root.insert(9)

root.printTree()

findPreAndSuc.pre = None
findPreAndSuc.suc = None

root.search(3)
root.search(10)


findPreAndSuc(root, 9) 
  
if findPreAndSuc.pre: 
    print(findPreAndSuc.pre.content)
  
else: 
    print("no predecessor")
  
if findPreAndSuc.suc: 
    print(findPreAndSuc.suc.content)
else: 
    print("no successor")

#root.printTree()

