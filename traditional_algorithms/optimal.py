# traditional_algorithms/optimal.py

class Optimal:
    def __init__(self, capacity):
        self.capacity = capacity
        self.page_faults = 0
        self.page_hits = 0

    def process(self, page_stream):
        self.page_faults = 0
        self.page_hits = 0
        frames = []

        for i in range(len(page_stream)):
            page = page_stream[i]
            if page in frames:
                self.page_hits += 1
                continue

            self.page_faults += 1
            if len(frames) < self.capacity:
                frames.append(page)
            else:
                # Predict future use
                future = page_stream[i+1:]
                indexes = []
                for f in frames:
                    if f in future:
                        indexes.append(future.index(f))
                    else:
                        indexes.append(float('inf'))  # Not used again

                replace_index = indexes.index(max(indexes))
                frames[replace_index] = page

        return self.page_hits, self.page_faults
