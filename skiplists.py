import random 
  
class Node(object): 
    def __init__(self, content, level): 
        self.content = content 
  
        self.pointer = [None]*(level+1) 
  
class SkipList(object): 
    def __init__(self, lvlcap, pp): 
        self.levelcap = lvlcap
  
        self.P = pp 
  
        self.header = self.createNode(self.levelcap, -1) 
  
        self.level = 0
      
    def createNode(self, lvl, content): 
        n = Node(content, lvl) 
        return n 
      
    def randomLevel(self): 
        lvl = 0
        while random.random()<self.P and lvl<self.levelcap:lvl += 1
        return lvl 

    def searchElement(self, content):  
        current = self.header 
  
        for i in range(self.level, -1, -1): 
            while(current.pointer[i] and current.pointer[i].content < content): 
                current = current.pointer[i] 
  
        current = current.pointer[0] 
        if current and current.content == content: 
            print("found content") 

        else:
            print("doesn't exist")
  
    def insertElement(self, content): 
        update = [None]*(self.levelcap+1) 
        current = self.header 

        for i in range(self.level, -1, -1): 
            while current.pointer[i] and current.pointer[i].content < content: 
                current = current.pointer[i] 
            update[i] = current 
        current = current.pointer[0] 

        if current == None or current.content != content: 
            rlevel = self.randomLevel() 
  
            if rlevel > self.level: 
                for i in range(self.level+1, rlevel+1): 
                    update[i] = self.header 
                self.level = rlevel 
  
            n = self.createNode(rlevel, content) 
  
            for i in range(rlevel+1): 
                n.pointer[i] = update[i].pointer[i] 
                update[i].pointer[i] = n 
  
    def deleteElement(self, search_content): 
  
        update = [None]*(self.levelcap+1) 
        current = self.header 
  
        for i in range(self.level, -1, -1): 
            while(current.pointer[i] and current.pointer[i].content < search_content): 
                current = current.pointer[i] 
            update[i] = current 
  
        current = current.pointer[0] 
  
        if current != None and current.content == search_content: 
  
            for i in range(self.level+1): 
  
                if update[i].pointer[i] != current: 
                    break
                update[i].pointer[i] = current.pointer[i] 
  
            while(self.level>0 and self.header.pointer[self.level] == None): 
                self.level -= 1
    
        print("successfully deleted")   
  
    def printList(self): 
        print("\nlist for level:") 
        head = self.header 
        for lvl in range(self.level+1): 
            print("{}-> ".format(lvl), end=" ") 
            node = head.pointer[lvl] 
            while(node != None): 
                print(node.content, end=" ") 
                node = node.pointer[lvl] 
            print("") 

def main(): 
    list = SkipList(3, 0.5) 
    list.insertElement(15) 
    list.insertElement(2) 
    list.insertElement(55) 
    list.insertElement(22) 
    list.insertElement(1) 
    list.insertElement(9) 
    list.insertElement(7) 
    list.insertElement(6) 
    list.insertElement(12) 
    list.insertElement(25) 
    list.printList() 
  
    list.searchElement(19) 
    list.searchElement(22)
  
    list.deleteElement(25) 
    list.printList() 
  
main() 