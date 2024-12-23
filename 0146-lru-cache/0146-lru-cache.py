#Step 1: Create the list node class
class ListNode():
    def __init__(self, value):
        self.value = value 
        self.prev = None 
        self.next = None 

# Step2: This is your linked list class for the double linked list
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity 
        self.head = ListNode((-1,-1)) # Put your LRUs
        self.tail = ListNode((-1,-1)) # Put your MRUs
        
        # establish basic connection
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {} # initialize the key value pair store 
        self.currCap = 0
    
    
    # Add to the tail 
    def addNode(self, node):
        tempNode = node 
        prevNode = self.tail.prev 
        prevNode.next = tempNode 
        tempNode.prev = prevNode 
        tempNode.next = self.tail 
        self.tail.prev = tempNode 
        
    
    #Remove from wherever it is (may not even be head )
    def removeNode(self, node):
        tempNode = node 
        prevNode = tempNode.prev
        nextNode = tempNode.next 
        prevNode.next = nextNode 
        nextNode.prev = prevNode
        
    
    def reassignHead(self):
        headNode = self.head.next 
        
        self.removeNode(headNode)
        k, v = headNode.value
        del self.hashmap[k]
        
        
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # get operation 
        if key not in self.hashmap:
            return -1
        
        # How to retrieve the value 
        k, v = self.hashmap[key].value
        
        # delete this value 
        self.removeNode(self.hashmap[key])
        
        # add to most recently used 
        self.addNode(self.hashmap[key])
        
        # return the value of the key 
        return v
    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap :
            currentNode = self.hashmap[key]
            # remove
            self.removeNode(currentNode)
            
            # add
            self.hashmap[key] = ListNode((key,value))
            
            self.addNode(self.hashmap[key])
            return 
        
        if self.currCap == self.capacity:
            # remove the head 
            self.reassignHead()
            self.currCap-=1
        
        # add the new node 
        nodeToAdd = ListNode((key, value))
        self.addNode(nodeToAdd)
        self.hashmap[key] = nodeToAdd

        # increment the counter 
        self.currCap+=1
        
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)