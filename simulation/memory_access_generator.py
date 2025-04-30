# simulation/memory_access_generator.py

import random

class MemoryAccessGenerator:
    def __init__(self, total_pages=20, stream_length=1000, locality_factor=0.7, locality_range=5):
        """
        :param total_pages: Number of unique pages in virtual memory.
        :param stream_length: Total length of access stream.
        :param locality_factor: Probability of accessing nearby pages (0 to 1).
        :param locality_range: How close the 'nearby' pages are.
        """
        self.total_pages = total_pages
        self.stream_length = stream_length
        self.locality_factor = locality_factor
        self.locality_range = locality_range

    def generate(self):
        access_stream = []
        current_page = random.randint(0, self.total_pages - 1)

        for _ in range(self.stream_length):
            if random.random() < self.locality_factor:
                # Access nearby page
                low = max(0, current_page - self.locality_range)
                high = min(self.total_pages - 1, current_page + self.locality_range)
                current_page = random.randint(low, high)
            else:
                # Access random page
                current_page = random.randint(0, self.total_pages - 1)
            access_stream.append(current_page)

        return access_stream
