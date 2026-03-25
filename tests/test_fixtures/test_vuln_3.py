import os

def ping_host(hostname):
    # BAD: user input passed directly to shell
    os.system(f"ping {hostname}")

def read_file(filename):
    # BAD: path traversal vulnerability
    with open(f"/var/data/{filename}") as f:
        return f.read()
```

Commit message:
```
test: add command injection vulnerable fixture
