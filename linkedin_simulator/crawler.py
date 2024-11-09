import threading
from typing import List
import random
import time
from .kafka_simulator import KafkaQueueSimulator
from .data_generator import LinkedInProfileGenerator, LinkedInPost

class LinkedInCrawler:
    def __init__(self, kafka_queue: KafkaQueueSimulator, profile_generator: LinkedInProfileGenerator):
        self.kafka_queue = kafka_queue
        self.profile_generator = profile_generator
        self.collected_posts: List[LinkedInPost] = []
        self.lock = threading.Lock()
        
    def discover_profiles(self, base_url: str) -> List[str]:
        # Simulates discovering new profiles
        return [self.profile_generator.generate_profile_url() 
                for _ in range(random.randint(1, 3))]
    
    def crawl_profile(self, url: str):
        #crawling delay added
        time.sleep(random.uniform(0.1, 0.5))
        
        # Generate 1-5 posts for profile
        posts = [self.profile_generator.generate_post() 
                for _ in range(random.randint(1, 5))]
        
        with self.lock:
            self.collected_posts.extend(posts)
        
        # Find and queue new profiles
        new_profiles = self.discover_profiles(url)
        for profile in new_profiles:
            self.kafka_queue.push(profile)
    
    def crawl_worker(self):
        while True:
            url = self.kafka_queue.poll()
            if not url:
                break
            self.crawl_profile(url)
    
    def start_crawling(self, initial_url: str, target_posts: int = 500):
        self.kafka_queue.push(initial_url)
        
        # Starts two worker threads
        workers = []
        for _ in range(2):
            worker = threading.Thread(target=self.crawl_worker)
            worker.start()
            workers.append(worker)
        
        
        while len(self.collected_posts) < target_posts:
            if self.kafka_queue.queue_size() == 0:
                self.kafka_queue.push(self.profile_generator.generate_profile_url())
            time.sleep(0.1)
        
        
        for _ in range(2):
            self.kafka_queue.push(None)  #stop workers
        
        for worker in workers:
            worker.join()
        
        return self.collected_posts