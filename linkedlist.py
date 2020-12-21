
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






