from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    print("🔥 PR detected!")

    if "pull_request" in payload:
        pr = payload["pull_request"]
        diff_url = pr["diff_url"]

        print("📎 Diff URL:", diff_url)

        headers = {
            "Accept": "application/vnd.github.v3.diff"
        }

        response = requests.get(diff_url, headers=headers)

        print("\n===== RAW DIFF =====\n")
        print(response.text[:1000])  # show first 1000 chars

    return {"status": "ok"}
