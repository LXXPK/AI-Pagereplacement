from collections import deque

def fifo_page_replacement(pages, frame_size):
    memory = deque()
    page_faults = 0
    page_hits = 0
    history = []

    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frame_size:
                memory.popleft()
            memory.append(page)
        history.append((list(memory), page, 'HIT' if page in memory else 'FAULT'))

    total_requests = len(pages)
    hit_rate = (page_hits / total_requests) * 100
    fault_rate = (page_faults / total_requests) * 100
    efficiency = hit_rate

    return {
        "hit_rate": hit_rate,
        "fault_rate": fault_rate,
        "efficiency": efficiency,
        "history": history
    }
