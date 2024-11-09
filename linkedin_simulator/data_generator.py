
from datetime import datetime, timedelta
import random
from dataclasses import dataclass
from typing import List, Optional
import numpy as np

@dataclass
class LinkedInPost:
    post_id: str
    profile_url: str
    content: str
    timestamp: datetime
    likes: int
    comments: int
    has_image: bool
    has_video: bool
    media_type: Optional[str] = None

class LinkedInProfileGenerator:
    def __init__(self):
        self.company_suffixes = ['Inc', 'LLC', 'Corp', 'Technologies', 'Solutions']
        self.domains = ['tech', 'consulting', 'software', 'data', 'ai', 'cloud']
        
    def generate_profile_url(self) -> str:
        name = f"linkedin.com/in/user-{random.randint(1000, 9999)}"
        return name

    def generate_content(self) -> str:
        topics = [
            "Excited to announce my new role",
            "Just completed an amazing project",
            "Great insights from today's conference",
            "Proud to share our team's achievement",
            "Looking forward to this new opportunity"
        ]
        base_content = random.choice(topics)
        words = random.randint(20, 200)
        return f"{base_content} " + " ".join([f"word{i}" for i in range(words)])

    def generate_post(self) -> LinkedInPost:
        has_image = random.random() < 0.3
        has_video = random.random() < 0.2 if not has_image else False
        
        if has_image:
            media_type = 'image'
        elif has_video:
            media_type = 'video'
        else:
            media_type = None

        return LinkedInPost(
            post_id=f"post_{random.randint(10000, 99999)}",
            profile_url=self.generate_profile_url(),
            content=self.generate_content(),
            timestamp=datetime.now() - timedelta(days=random.randint(0, 365)),
            likes=int(np.random.lognormal(4, 1)),
            comments=int(np.random.lognormal(2, 1)),
            has_image=has_image,
            has_video=has_video,
            media_type=media_type
        )