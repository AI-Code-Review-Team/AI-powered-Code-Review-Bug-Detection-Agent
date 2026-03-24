"""
Intentionally bad performance code.
Used to demonstrate the Performance Agent catching N+1 queries and O(n²) patterns.
"""


# PERF ISSUE 1: N+1 query pattern
def get_all_posts_with_authors(db_session):
    posts = db_session.query(Post).all()   # Query 1: fetch all posts
    result = []
    for post in posts:
        # BAD: fires a new DB query for EVERY post — N+1 problem
        author = db_session.query(User).filter_by(id=post.author_id).first()
        result.append({"title": post.title, "author": author.name})
    return result


# PERF ISSUE 2: O(n²) nested loop
def find_duplicates(items: list) -> list:
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):   # BAD: O(n²) — use a set instead
            if i != j and items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates


# PERF ISSUE 3: Blocking I/O inside async function
import requests
import asyncio

async def fetch_user_data(user_id: int):
    # BAD: requests.get is blocking — freezes the entire event loop
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()


# PERF ISSUE 4: Repeated expensive computation inside loop
import re

def process_logs(log_lines: list[str]) -> list[str]:
    results = []
    for line in log_lines:
        # BAD: re.compile called on every iteration — compile once outside loop
        pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
        match = pattern.search(line)
        if match:
            results.append(match.group())
    return results


# PERF ISSUE 5: Loading entire table into memory
def get_active_user_emails(db_session):
    # BAD: fetches ALL users then filters in Python — use .filter() in the query
    all_users = db_session.query(User).all()
    return [u.email for u in all_users if u.is_active]
