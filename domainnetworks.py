import json

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver as wiredriver

# Path to your Chrome driver executable
# chrome_driver_path = 'path/to/chromedriver'

# Create a new instance of the Chrome driver with Selenium Wire
service = Service()
driver = wiredriver.Chrome(service=service)

# Navigate to the desired website
driver.get("https://domainnetworks.com/search")

# Wait for the page to load (you may need to adjust the time)
input("please select state....")
data=[]

# Function to scroll down the page
def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# prev_page_height = driver.execute_script("return document.body.scrollHeight")


# Scroll down every 1 second for a total of 5 times (adjust as needed)
count=1
target_value=20
while True:
    scroll_down()
    count=count+1
    if count>=target_value:
        value = input("please enter.")
        if value == '1':
            break
        else:
            target_value=target_value+target_value
    # current_page_height = driver.execute_script("return document.body.scrollHeight")
    # Check if page height has changed
    # if current_page_height == prev_page_height:
    #     break  # Exit loop if page height no longer increases
    # prev_page_height = current_page_height

# Access captured requests
for request in driver.requests:
    if 'domainnetworks.com/elasticsearch/search' in request.url:
        # Print the request payload
        print("Request payload:")
        print(request.body.decode('utf-8'))
        data.append(request.body.decode('utf-8'))

# Close the driver

input("Press Enter to colse driver...")
with open("Michigan.json","w") as f:
    json.dump(data,f)
driver.quit()
