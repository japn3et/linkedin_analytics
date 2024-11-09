from .data_generator import LinkedInProfileGenerator
from .kafka_simulator import KafkaQueueSimulator
from .crawler import LinkedInCrawler
from .database import DatabaseHandler

def main():
    
    kafka_queue = KafkaQueueSimulator()
    profile_generator = LinkedInProfileGenerator()
    crawler = LinkedInCrawler(kafka_queue, profile_generator)
    db_handler = DatabaseHandler()
    
    # Start crawling
    initial_url = "linkedin.com/in/starting-profile"
    posts = crawler.start_crawling(initial_url, target_posts=500)
    
    # Store results
    db_handler.store_posts(posts)
    
    print(f"Successfully collected and stored {len(posts)} posts")

if __name__ == "__main__":
    main()
