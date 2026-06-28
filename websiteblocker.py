import time
from datetime import datetime

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = [
    "www.facebook.com",
    "facebook.com",
    "www.instagram.com",
    "instagram.com",
    "www.youtube.com",
    "youtube.com"
]

while True:
    if 9 <= datetime.now().hour < 18:
        print("Working hours... Blocking websites.")

        with open(hosts_path, "r+") as file:
            content = file.read()

            for website in websites:
                if website not in content:
                    file.write(redirect + " " + website + "\n")

    else:
        print("Free time... Unblocking websites.")

        with open(hosts_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)

            for line in lines:
                if not any(website in line for website in websites):
                    file.write(line)

            file.truncate()

    time.sleep(10)