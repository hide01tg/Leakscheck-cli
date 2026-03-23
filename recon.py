import requests
import time
import json
import sys

# --- OPERATOR CONFIGURATION ---
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "[https://leakscheck.com/api/v1](https://leakscheck.com/api/v1)"
QUERY = "targetdomain.com"  # Enter Target Domain or Identity here

print(f"[*] Initiating tactical search for: {QUERY}...")

# Step 1: Request the search task
payload = {"api_key": API_KEY, "query": QUERY, "type": "general"}
try:
    post_req = requests.post(f"{BASE_URL}/search", json=payload)
    post_data = post_req.json()
except Exception as e:
    print(f"[-] Connection to Command failed: {e}")
    sys.exit(1)

if "task_id" not in post_data:
    print("[-] Error allocating node:", post_data)
    sys.exit(1)

task_id = post_data["task_id"]
print(f"[*] Task queued successfully. Allocation ID: {task_id}")
print("[*] Polling for intelligence. This may take up to 40 seconds...\n")

partial_printed = False

# Step 2: Poll until data is fully compiled
while True:
    get_req = requests.get(f"{BASE_URL}/status/{task_id}?api_key={API_KEY}")
    get_data = get_req.json()
    state = get_data.get("state")
    
    if state == "SUCCESS":
        print("\n[+] TARGET RECON COMPLETE. FULL DATA DUMP:\n")
        print(json.dumps(get_data.get("result", {}), indent=4))
        break
    elif state == "PROCESSING":
        if not partial_printed:
            print("\n[+] FAST INTEL (DEEP WEB DB) ACQUIRED:\n")
            print(json.dumps(get_data.get("result", {}), indent=4))
            print("\n[*] Still polling Global Telegram nodes for additional data...\n")
            partial_printed = True
        else:
            print("[~] Waiting on Global Telegram nodes...")
        time.sleep(4)
    elif state == "PENDING":
        print("[~] Awaiting node allocation...")
        time.sleep(4)
    else:
        print(f"[-] Task failed or encountered an error: {get_data}")
        break
