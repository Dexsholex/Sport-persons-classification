import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Change to your desired working directory
desired_directory = r"C:\Users\USER\Desktop\Projects\Image Classification\scrape_images"
os.makedirs(desired_directory, exist_ok=True)  # Create the directory if it doesn't exist
os.chdir(desired_directory)  # Change the current working directory

# Function to download image from a URL
def download_image(url, folder_name, image_name):
    try:
        img_data = requests.get(url).content
        with open(f"{folder_name}/{image_name}.jpg", 'wb') as img_file:
            img_file.write(img_data)
        print(f"Downloaded {image_name}.jpg")
    except Exception as e:
        print(f"Failed to download {url} - {e}")

# Function to scrape images using Selenium from DuckDuckGo
def scrape_images(query, num_images=10):
    # Set up Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"https://duckduckgo.com/?q={query}&iar=images&iax=images&ia=images")

    # Allow time for images to load
    time.sleep(2)

    # Scroll to load more images
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Find image elements
    image_elements = driver.find_elements(By.CSS_SELECTOR, "img.tile--img__img")

    if not os.path.exists(query):
        os.makedirs(query)

    count = 0
    for img_element in image_elements[:num_images]:
        try:
            img_url = img_element.get_attribute("src") or img_element.get_attribute("data-src")
            if img_url:
                download_image(img_url, query, f"{query}_{count + 1}")
                count += 1
            if count >= num_images:
                break
        except Exception as e:
            print(f"Error fetching image: {e}")

    driver.quit()

# List of sports personalities to scrape images for
athletes = ['Serena Williams', 'LeBron James', 'Cristiano Ronaldo', 'Usain Bolt', 'Muhammad Ali']

for athlete in athletes:
    print(f"Scraping images for {athlete}...")
    scrape_images(athlete, num_images=300)
