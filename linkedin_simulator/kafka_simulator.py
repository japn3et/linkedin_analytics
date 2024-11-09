from collections import deque
from typing import Optional

class KafkaQueueSimulator:
    def __init__(self):
        self.queue = deque()
        
    def push(self, url: str):
        self.queue.append(url)
        
    def poll(self) -> Optional[str]:
        return self.queue.popleft() if self.queue else None
    
    def queue_size(self) -> int:
        return len(self.queue)
