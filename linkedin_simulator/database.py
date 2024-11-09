# linkedin_simulator/database.py
import sqlite3
from datetime import datetime
from typing import List
from .data_generator import LinkedInPost

class DatabaseHandler:
    def __init__(self, db_path: str = "linkedin_posts.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS posts
            (post_id TEXT PRIMARY KEY,
             profile_url TEXT,
             content TEXT,
             timestamp TEXT,
             likes INTEGER,
             comments INTEGER,
             has_image BOOLEAN,
             has_video BOOLEAN,
             media_type TEXT)
        ''')
        conn.commit()
        conn.close()
    
    def store_posts(self, posts: List[LinkedInPost]):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        for post in posts:
            c.execute('''
                INSERT OR REPLACE INTO posts
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                post.post_id,
                post.profile_url,
                post.content,
                post.timestamp.isoformat(),
                post.likes,
                post.comments,
                post.has_image,
                post.has_video,
                post.media_type
            ))
        conn.commit()
        conn.close()

    def get_all_posts(self) -> List[LinkedInPost]:
        """Retrieve all posts from the database"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT * FROM posts')
        rows = c.fetchall()
        conn.close()
        
        posts = []
        for row in rows:
            post = LinkedInPost(
                post_id=row[0],
                profile_url=row[1],
                content=row[2],
                timestamp=datetime.fromisoformat(row[3]),
                likes=row[4],
                comments=row[5],
                has_image=bool(row[6]),
                has_video=bool(row[7]),
                media_type=row[8]
            )
            posts.append(post)
        return posts

    def clear_database(self):
        """Clear all data from the database"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('DELETE FROM posts')
        conn.commit()
        conn.close()
