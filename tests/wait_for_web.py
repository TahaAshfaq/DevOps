import time, requests, sys

# Wait for the web app to be ready
for _ in range(30):
    try:
        r = requests.get("http://web:5173")
        if r.status_code == 200:
            print("Web app is up!")
            break
    except Exception:
        pass
    time.sleep(2)
else:
    print("Web app not ready!")
    sys.exit(1)

# Run the tests
import subprocess
result = subprocess.run(["python3", "test_homepage.py"])
sys.exit(result.returncode)
