# BAD: secrets hardcoded directly in source code
API_KEY = "sk-prod-abc123supersecret"
DB_PASSWORD = "admin123"

def connect_to_api():
    return {"key": API_KEY, "db": DB_PASSWORD}
```

Commit message:
```
test: add hardcoded secret vulnerable fixture
