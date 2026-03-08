import requests
from concurrent.futures import ThreadPoolExecutor

# 🔹 CONFIGURATION
BASE_NUMBER = 474        # URL মধ্যে যা constant থাকবে
START = 1                # প্রথম page
END = 200                # শেষ page
KEYWORDS = ["monthly", "9"]  # যেই keywords খুঁজবেন

found = []

def scan_page(num):
    # URL বানানো
    url = f"https://offertopup.com/{num}/{BASE_NUMBER}/%20%2010120%20%F0%9F%92%8E"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            text = r.text.lower()
            if all(k in text for k in KEYWORDS):
                found.append(url)
                print(f"[FOUND] {url}")
            else:
                print(f"[Checked] {url}")
        else:
            print(f"[Dead] {url}")
    except Exception as e:
        print(f"[Error] {url} - {e}")

# 🔹 Multi-threaded scan (speed up)
with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(scan_page, range(START, END + 1))

# 🔹 Save results
with open("result.txt", "w") as f:
    if found:
        for u in found:
            f.write(u + "\n")
    else:
        f.write("No matching pages found\n")

print("\nScan Finished!")
