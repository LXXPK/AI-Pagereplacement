# test_algorithms.py

from simulation.memory_access_generator import MemoryAccessGenerator
from traditional_algorithms.fifo import FIFO
from traditional_algorithms.lru import LRU
from traditional_algorithms.optimal import Optimal

# Generate page stream
gen = MemoryAccessGenerator(total_pages=20, stream_length=100, locality_factor=0.75)
stream = gen.generate()

frame_size = 4  # number of physical memory frames

# Test FIFO
fifo = FIFO(frame_size)
fifo_hits, fifo_faults = fifo.process(stream)

# Test LRU
lru = LRU(frame_size)
lru_hits, lru_faults = lru.process(stream)

# Test Optimal
opt = Optimal(frame_size)
opt_hits, opt_faults = opt.process(stream)

print(f"FIFO => Hits: {fifo_hits}, Faults: {fifo_faults}")
print(f"LRU  => Hits: {lru_hits}, Faults: {lru_faults}")
print(f"OPT  => Hits: {opt_hits}, Faults: {opt_faults}")
