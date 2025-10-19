class Node:
    def __init__(self, key = -1, val = -1, prv = None, nxt = None):
        self.val = val
        self.key = key
        self.prv = prv
        self.nxt = nxt
class LRUCache:
    def __init__(self, capacity: int):
        self.hm = {}
        self.cap = capacity
        self.head = Node()
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.hm:
            # move the node and put to front
            prev = self.hm[key].prv
            nxt = self.hm[key].nxt
            if prev:
                prev.nxt = self.hm[key].nxt
            if nxt:
                nxt.prv = self.hm[key].prv
            self.head.nxt = self.hm[key]
            self.hm[key].prv = self.head
            self.head = self.hm[key]

            return self.hm[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.get(key)
            self.hm[key].val = value
            return
        # add new key        
        # self.tail.nxt always least used
        print(f"{self.hm.keys()}, {self.tail.val}, {-100 if not self.tail.nxt else self.tail.nxt.val}")
        if len(self.hm) == self.cap:
            least = self.tail.nxt
            newleast = least.nxt
            self.tail.nxt = newleast
            newleast.prv = self.tail
            del self.hm[least.key]
        
        self.hm[key] = Node(key, value, prv = self.head)
        self.head.nxt = self.hm[key]

        self.head = self.hm[key]
        if self.tail.nxt:
            print(f"{self.tail.nxt.key} - {self.tail.nxt.val}")
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)