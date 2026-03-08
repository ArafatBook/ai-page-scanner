import requests
from concurrent.futures import ThreadPoolExecutor

# 🔹 CONFIGURATION
URL_PATTERN = "https://offertopup.com/topup/{NUMBER}/%20%2010120%20%F0%9F%92%8E"
START = 1
END = 200
KEYWORDS = ["weekly", "99"]  # search keywords

found = []

def scan_page(num):
    url = URL_PATTERN.format(NUMBER=num)
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

# 🔹 Multi-threaded scan
with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(scan_page, range(START, END + 1))

# 🔹 Save result
with open("result.txt", "w") as f:
    if found:
        for u in found:
            f.write(u + "\n")
    else:
        f.write("No 99tk weekly page found\n")

print("\nScan Finished!")
