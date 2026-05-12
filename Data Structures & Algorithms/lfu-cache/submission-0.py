class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vals = {}
        self.counts = {}
        self.lists = {}
        self.min_freq = 0

    def update(self, key):
        freq = self.counts[key]
        val = self.vals[key]

        del self.lists[freq][key]

        if not self.lists[freq]:
            del self.lists[freq]

            if freq == self.min_freq:
                self.min_freq += 1
        
        new_freq = freq + 1
        self.counts[key] = new_freq

        if new_freq not in self.lists:
            self.lists[new_freq] = OrderedDict()
        
        self.lists[new_freq][key] = val
    
    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        self.update(key)
        return self.vals[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.vals:
            self.vals[key] = value
            self.update(key)
        else:
            if len(self.vals) >= self.capacity:
                popped_key, _ = self.lists[self.min_freq].popitem(last=False)

                if not self.lists[self.min_freq]:
                    del self.lists[self.min_freq]
                
                del self.vals[popped_key]
                del self.counts[popped_key]
            
            self.vals[key] = value
            self.counts[key] = 1
            self.min_freq = 1

            if 1 not in self.lists:
                self.lists[1] = OrderedDict()
            
            self.lists[1][key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)