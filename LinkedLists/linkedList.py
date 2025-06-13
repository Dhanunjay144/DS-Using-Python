class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def printList(self):
        tmp = self.head
        nodes = []
        while(tmp is not None):
            nodes.append(tmp.value)
            tmp = tmp.next
        print(" -> ".join(map(str, nodes)))
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        pre = self.head
        tmp = self.head
        while(tmp.next):
            pre = tmp
            tmp = tmp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return tmp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        self.head = self.head.next
        tmp.next=None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return tmp

print("Creating my first Linked List")
my_ll = LinkedList(4)
print("Linked list is :", my_ll.head.value)

print("Appending the linked list with some values")
my_ll.append(2)
my_ll.append(5)
my_ll.append(7)
my_ll.printList()

print("Popping the linked list")
print("Popped element is:", my_ll.pop())
my_ll.printList()

# print("Trying Popping of single element linked list")
# my_ll1 = LinkedList(1)
# my_ll1.append(10)
# my_ll1.append(15)
# print("Popped element is:", my_ll1.pop())
# my_ll1.printList()

print("Prependng the linked list")
my_ll.prepend(1)
my_ll.printList()

# # print("Trying Prepend of single element linked list")
# my_ll1 = LinkedList(1)

# # my_ll1.prepend(2)
# # my_ll1.printList()
# print("Trying Prepend on empty linked list")
# my_ll1.pop()
# my_ll1.prepend(5)
# my_ll1.printList()

print("Pop First from the linked list")
my_ll.pop_first()
my_ll.printList()

# # print("Trying Prepend of single element linked list")
# my_ll1 = LinkedList(1)

# # my_ll1.prepend(2)
# # my_ll1.printList()
# print("Trying Prepend on empty linked list")
# my_ll1.pop()
# my_ll1.prepend(5)
# my_ll1.printList()