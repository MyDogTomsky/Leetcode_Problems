# Leetcode 380
# Implement Randomised Class
# There are 3 methods: *to insert value/*to remove value/*to get the random value
# insert/remove method --> boolean / get a random value --> int
import random

class RandomisedSet:

    def __init__(self):
        self.container = dict()
        self.randomy = []
        self.outcome = [None]

    def insert(self, val: int) -> bool:
        
        if val not in self.container:
            self.randomy.append(val)
            self.container[val] = len(self.randomy)-1
            self.outcome.append(True)
            return True
        else:
            self.outcome.append(False) 
            return False
        

    def remove(self, val: int) -> bool:

        if val in self.container:
            current_idx = self.container[val]
            last_idx = len(self.randomy) - 1
            last_val = self.randomy[-1]
            #last_val = self.randomy[last_val]
            self.randomy[current_idx], self.randomy[last_idx] = self.randomy[last_idx], self.randomy[current_idx]
            #self.container[val] = last_idx
            self.container[last_val] = current_idx 

            self.randomy.pop()
            self.container.pop(val)
            self.outcome.append(True)
            return True
        else:
            self.outcome.append(False) 
            return False

    def getRandom(self) -> int:

        get_one = random.choice(self.randomy)
        self.outcome.append(get_one)
        return get_one


method_list = ["RandomisedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
parameter_list = [[], [1], [2], [2], [], [1], [2], []]

random_bot = RandomisedSet(*parameter_list[0])
for idx, method in enumerate(method_list[1:],start = 1):
    each_method = getattr(random_bot,method,None)
    if each_method:
        each_method(*parameter_list[idx])

print(random_bot.outcome)    