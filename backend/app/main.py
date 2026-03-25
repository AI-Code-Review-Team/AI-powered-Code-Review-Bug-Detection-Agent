from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import json

from .db import engine, SessionLocal
from .models import Base, PullRequestEvent
from .github_utils import fetch_pr_diff

load_dotenv()

app = FastAPI(title="PR Review AI - Basic Pipeline")

# Create table automatically
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "PR Review AI backend is running 🚀"}

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    event = request.headers.get("X-GitHub-Event")

    print("\n==============================")
    print("📩 Webhook received!")
    print("GitHub Event:", event)

    if event == "pull_request":
        action = payload.get("action")
        pr = payload.get("pull_request", {})
        repo = payload.get("repository", {})

        pr_number = pr.get("number")
        pr_title = pr.get("title")
        repo_name = repo.get("full_name")
        diff_url = pr.get("diff_url")

        print(f"🔹 Action: {action}")
        print(f"🔹 Repo: {repo_name}")
        print(f"🔹 PR Number: {pr_number}")
        print(f"🔹 PR Title: {pr_title}")
        print(f"🔹 Diff URL: {diff_url}")

        if repo_name and pr_number:
            owner, repo_only = repo_name.split("/")

            # Fetch raw PR diff
            raw_diff = fetch_pr_diff(owner, repo_only, pr_number)

            if raw_diff:
                print("\n📄 RAW PR DIFF START")
                print(raw_diff[:3000])   # show first 3000 chars
                print("📄 RAW PR DIFF END\n")

        # Save basic PR event in PostgreSQL
        db = SessionLocal()
        try:
            event_data = PullRequestEvent(
                repo_name=repo_name,
                pr_number=pr_number,
                pr_title=pr_title,
                action=action,
                diff_url=diff_url,
                raw_payload=json.dumps(payload)
            )
            db.add(event_data)
            db.commit()
        finally:
            db.close()

    return JSONResponse(content={"status": "received"})