from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .db import Base

class PullRequestEvent(Base):
    __tablename__ = "pull_request_events"

    id = Column(Integer, primary_key=True, index=True)
    repo_name = Column(String, nullable=False)
    pr_number = Column(Integer, nullable=False)
    pr_title = Column(String, nullable=False)
    action = Column(String, nullable=False)
    diff_url = Column(String, nullable=True)
    raw_payload = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)