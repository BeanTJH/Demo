class DNode:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None 


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insert(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1
    def insert_at(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
        while current:
            if count < index:
                print('The lsit has less number of elements.')
            elif index == 1:
                node.next = current
                self.head = node
                print(count)
                self.size += 1
                return
            elif index == count:
                node.next = current
                prev.next = node
                self.size += 1
                return
            else: 
                count += 1
                prev = current
                current = current.next

    def insert_bef(self, data):
        current = self.head
        prev = self.head
        node = Node(data)
        while current:
            if current.data == data:
                node.next = current
                prev.next = node
            prev = current
            current = current.next
        self.size += 1
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False
    def get_at(self, index):
        count = 1
        current = self.head
        if self.size < index:
            print('The list has less number of elements.')
        else:
            while current:
                if index == count:
                    return current.data
                else:
                    count += 1
                    current = current.next

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def delete_of(self, data):
        # delete specified data on linked list
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -=1
                return
            prev = current
            current = current.next

    def clear(self):
        self.tail = None
        self.head = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_first(self, data):
        new_node = DNode(data, None, None)
        
        if self.head is None:
            self.tail = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
    def insert_last(self, data):
        new_node = DNode(data, None, None)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.head.next = new_node
            self.tail = new_node
        self.count += 1
    def insert_bef(self, data):
        current = self.head
        prev = self.head
        new_node = DNode(data, None, None)
        while current:
            if current.data == data:
                new_node.prev = prev
                new_node.next = current
                prev.next = new_node
                current.prev = new_node
                self.count += 1

            prev = current
            current = current.next

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print("Data item is present in the list. ")
                return
        print("Data item is not present in the list. ")
        return
    def delete_of(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            print("List is empty")
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
            
        elif self.tail.data == data:
            self.tail = self.tail.prev
            node_deleted = True
            self.tail.next = None
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
            if node_deleted == False:
                print("Item not found")
            if node_deleted:
                self.count -=1

class Stack:
    """Can just use deque from collections as it is generalized stack/queue"""
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
            
        else:
            self.top = node
        self.size += 1
    def pop(self):
        """ Delete and return the top node"""
        
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        
        else:
            print("Stack is empty. ")


    def peek(self):
        if self.top:
            return self.top.data
    
        else:
            print("Stack is empty. ")

class Queue:
    """Can use deque from collections as it is generalized stack/queue"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def enqueue(self, data):
        """Add an item to the back of the queue"""
        new_node = DNode(data, None, None)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    def dequeue(self, data):
        """ Remove the front item and return its value"""
        if self.count == 1:
            data = self.head.data
            self.count -= 1
            self.head = None
            self.tail = None
            return data
        elif self.count < 1:
            print("Queue is empty")
        else:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return data