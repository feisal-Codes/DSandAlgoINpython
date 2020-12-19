# stacks represent a ds such that data is piled on top of each other
# it follows the concept first in,last out
# elements that go last are retrived first (LIFO)
# operations include Push , pop and peek
# peek doesnt change the stacks , it merely returns the elements
# lets implement stacks in python


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def getStack(self):
        return self.items

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]




if __name__=="__main__":
 
 mystack=Stack()
 testlist=['A','B','C','D']
 for item in testlist:
    mystack.push(item)
 print(mystack.getStack())

 mystack.pop()
 mystack.pop()


 print(mystack.getStack())
 print(mystack.peek())


    

