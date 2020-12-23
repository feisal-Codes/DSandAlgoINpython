
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_after(self,prev_node,data):
        if not prev_node:
            print("previous node does not exist")
            return
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def delete_node(self,key):
        #deleting head 
        #get the current head node(first node)
        cur_node=self.head
        #check if the data  to be deleted matches the current node's data(head node)
        if cur_node and cur_node.data==key:
            #point to the next node and set it as the header
            #set the current node to be none
            self.head=cur_node.next
            cur_node=None
            return
        prev_node =None
        while cur_node and cur_node.data != key:
            prev_node=cur_node #get the previous node to the node we want to delete as ones the node's data matches the key we exit the loop and prev node
                               #remains 
            cur_node=cur_node.next #sets the cur_node to the next node #while loop depends on this to exit  
        if cur_node is None:
            return
        prev_node.next=cur_node.next
        cur_node=None
    def delete_node_at_position(self,pos):
        #deleting head 
        #get the current head node(first node)
        cur_node=self.head
        #check if the data of the node to be deleted matches the current node(head node)
        if pos==0:
            #point to the next node and set it as the header
            #set the current node to be none
            self.head=cur_node.next
            cur_node=None
            return
        prev_node =None
        count=0
        while cur_node and count !=0 :
            prev_node=cur_node
            cur_node=cur_node.next  
            count+=1
        if cur_node is None:
            return
        prev_node.next=cur_node.next
        cur_node=None
        
    def getLengthIterative(self):
        count=0
        cur_node=self.head
        while cur_node:
            count+=1
            cur_node=cur_node.next
        return count
    def getLengthRecursively(self,node):
        if node==None:
            return 0
        return 1 + self.getLengthRecursively(node.next)
            

mylist = Linkedlist()
for i in "eisal":
    mylist.append(i)
mylist.print_list()
print('..............')
mylist.prepend('F')
print('..............')
mylist.print_list()
mylist.insert_after(mylist.head.next,'y')
print('..............')
mylist.print_list()
print('..............')
mylist.delete_node('l')
mylist.print_list()
print(mylist.getLengthIterative())
print(mylist.getLengthRecursively(mylist.head))

