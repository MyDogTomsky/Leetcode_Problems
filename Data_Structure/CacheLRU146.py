# Leetcode 146
# 3 methods --> **to initialise/**to get the Key/**to put the key-value pair
# There is fixed capacity of LRU cache.==> capacity
# When getting the KEY, if there is no key, return -1
#                       if there is a KEY, return the value
# When putting the KEY & VALUE,
# UPDATING the value of the key
# ADDING the pair(key:value)
# If the number of keys exceeds the capacity, evict(=pop) the least recently used key!

from collections import OrderedDict
import time

class LRUCache:

    
    def __init__(self,capacity: int):

        self.capacity = capacity
        self.lru = OrderedDict()
        self.result = [None]


    def get(self, key : int) -> int:

        if key not in self.lru: 
            self.result.append(-1)
            return -1
        else: 
            self.lru.move_to_end(key)
            # end --> Recent / First --> Last(old)
            self.result.append(self.lru[key])
            return self.lru[key]
        

    def put(self, key: int, value: int) -> None:
        
        self.lru[key] = value
        self.lru.move_to_end(key)
        
        if len(self.lru) > self.capacity:
            self.lru.popitem(last = False)
        
        self.result.append(None)


command_list = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
spec = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

start = time.time()
new_bot = LRUCache(*spec[0])

for idx,command in enumerate(command_list[1:],start = 1):
    obj_command = getattr(new_bot, command, None)
    if obj_command:
        obj_command(*spec[idx])

print(new_bot.result)      

end = time.time()

print(f'\n\nTotal time: {end - start:.4f} seconds')