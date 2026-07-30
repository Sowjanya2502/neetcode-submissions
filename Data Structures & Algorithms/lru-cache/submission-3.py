class doublelinkedList:
    def __init__(self,  key:int,val:int):
        self.key=key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map1={}
        self.head=doublelinkedList(-1,-1)
        self.tail = doublelinkedList(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def remove(self,Node: doublelinkedList):
        # Node = map1[key]
        later = Node.next
        before = Node.prev
        if Node.prev:
            Node.prev.next = later
        if Node.next:
            Node.next.prev = before
    def insert(self,Node: doublelinkedList)->None:
        prev1 = self.tail.prev
        prev1.next = Node
        Node.prev = prev1
        Node.next = self.tail
        self.tail.prev = Node

    def get(self, key: int) -> int:
        if key in self.map1:
            Node = self.map1[key]
            self.remove(Node)
            self.insert(Node)
            return Node.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.map1:
            k1 = self.map1[key]
            self.remove(k1)
        Node = doublelinkedList(key,value)
        self.map1[key]=Node
        self.insert(Node)
        if  len(list(self.map1.keys()))>self.capacity:
            del self.map1[self.head.next.key]
            self.remove(self.head.next)
        
