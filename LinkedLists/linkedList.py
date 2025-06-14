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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index,value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            pre = self.get(index - 1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True


        

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

print("Get a node from the linked list")
print(my_ll.get(2))

print("Set a node from the linked list")
print(my_ll.set_value(2, 3))
my_ll.printList()

print("Insert a node at an index in the linked list")
print(my_ll.insert(2, 6))
my_ll.printList()

print("Remove a node at an index in the linked list")
print(my_ll.remove(1))
my_ll.printList()

print("Reversing the linked list")
print(my_ll.reverse())
my_ll.printList()