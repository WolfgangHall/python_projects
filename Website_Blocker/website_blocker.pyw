import time
from datetime import datetime as dt

HOST_TEMP = "hosts"
HOST_PATH = r'C:\Windows\System32\drivers\etc'
REDIRECT = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working Hours...')
        # use r+ to read and write
        with open(HOST_TEMP, 'r+') as file:
            content = file.read()
            # if the website is there already during work hours, do nothing
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(REDIRECT + " " + website + "\n")
    else:
        with open(HOST_TEMP, 'r+') as file:
            # use readlines to grab line by line
            content = file.readlines()
            # want to append the lines before the existing block
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            # remove the repeated text
            file.truncate()
        print("fun hours")

    time.sleep(100)
