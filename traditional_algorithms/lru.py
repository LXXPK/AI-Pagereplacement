# traditional_algorithms/lru.py

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.frames = []
        self.page_faults = 0
        self.page_hits = 0

    def process(self, page_stream):
        self.frames = []
        self.page_faults = 0
        self.page_hits = 0

        for page in page_stream:
            if page in self.frames:
                self.page_hits += 1
                self.frames.remove(page)
                self.frames.append(page)
            else:
                self.page_faults += 1
                if len(self.frames) < self.capacity:
                    self.frames.append(page)
                else:
                    self.frames.pop(0)
                    self.frames.append(page)

        return self.page_hits, self.page_faults
