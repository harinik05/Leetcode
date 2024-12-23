import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = collections.OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1 
        self.hashmap.move_to_end(key)
        return self.hashmap[key]
        

    def put(self, key: int, value: int) -> None:
        #1. if the key is in dictionary 
        if key in self.hashmap:
            self.hashmap.move_to_end(key)
        self.hashmap[key]=value
        #2. check capacity 
        if len(self.hashmap) > self.capacity:
            self.hashmap.popitem(last=False)
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)