from fastapi import FastAPI

app = FastAPI()

# Temporary database
findings_db = []

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.post("/webhook")
def webhook():
    return {"status": "received"}

@app.get("/findings/{pr_id}")
def get_findings(pr_id: int):
    return [f for f in findings_db if f["pr_id"] == pr_id]

@app.get("/dashboard/stats")
def stats():
    return {
        "total_findings": len(findings_db),
        "high": sum(1 for f in findings_db if f.get("severity") == "HIGH"),
        "medium": sum(1 for f in findings_db if f.get("severity") == "MEDIUM"),
        "low": sum(1 for f in findings_db if f.get("severity") == "LOW"),
    }
