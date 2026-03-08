import requests

START = 474
END = 1000

found = []

for i in range(START, END + 1):
    url = f"https://offertopup.com/topup/{i}/%20%2010120%20%F0%9F%92%8E"

    try:
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            text = r.text.lower()

            if "monthly" in text and "9" in text:
                found.append(url)
                print(f"FOUND: {url}")
            else:
                print(f"Checked: {url}")

        else:
            print(f"Dead: {url}")

    except Exception as e:
        print(f"Error: {url}")

# result file save
with open("result.txt", "w") as f:
    if found:
        for u in found:
            f.write(u + "\n")
    else:
        f.write("No 9tk monthly page found\n")

print("\nScan Finished")
