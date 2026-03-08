import requests
from concurrent.futures import ThreadPoolExecutor

START = 474
END = 1000

def scan_page(num):
    url = f"https://offertopup.com/topup/{num}/%20%2010120%20%F0%9F%92%8E"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            if "monthly" in r.text.lower():
                print("FOUND:", url)
    except:
        pass

with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(scan_page, range(START, END+1))
