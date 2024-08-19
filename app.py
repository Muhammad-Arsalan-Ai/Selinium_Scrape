# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time

# # Set up Chrome options to change the default language to English
# chrome_options = Options()
# chrome_options.add_argument("--lang=en")

# # Initialize the webdriver with the specified options
# driver = webdriver.Chrome(options=chrome_options)

# # List of URLs to scrape
# urls = [
#     "https://smartstore.naver.com/f-market/category/7520bfc7be3c4d89bdff269c38df0918?st=RECENT&dt=LIST&page=1&size=40",
#     "https://smartstore.naver.com/lure-s/category/1c9a0e66cb9041568191da10cd28ab37?st=RECENT&dt=LIST&page=1&size=40",
#     "https://smartstore.naver.com/f-market/category/7520bfc7be3c4d89bdff269c38df0918?st=RECENT&dt=LIST&page=1&size=40",
#     "https://smartstore.naver.com/bigyellowtail/category/76e2515393d740c5b4c214707228d1bc?st=RECENT&dt=LIST&page=1&size=40",
# ]

# # Loop through each URL
# for url in urls:
#     # Open the website
#     driver.get(url)

#     # Allow time for the page to load
#     time.sleep(5)  # Adjust sleep time if necessary

#     # Locate the product element (assuming you want the first product in the list)
#     product = driver.find_element(By.CSS_SELECTOR, "li._3S7Ho5J2Ql")

#     # Scrape the required details
#     title = product.find_element(By.CSS_SELECTOR, "strong._1Zvjahn0GA").text
#     price = product.find_element(By.CSS_SELECTOR, "strong._22XUYkkUGJ").text
#     desc = product.find_element(By.CSS_SELECTOR, "p._1jGpq7xfIB").text
#     image_url = product.find_element(By.CSS_SELECTOR, "div._2JNWBGd-04 img").get_attribute("src")
#     product_date = product.find_element(By.CSS_SELECTOR, "div._1eB0tn9wSc").text

#     # Print the scraped details
#     print("URL:", url)
#     print("Title:", title)
#     print("Price:", price)
#     print("Description:", desc)
#     print("Image URL:", image_url)
#     print("Product Date:", product_date)
#     print("-" * 40)

# # Close the browser
# driver.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Initialize the webdriver
# driver = webdriver.Chrome()

# # URL to scrape
# url = "https://smartstore.naver.com/dasolfishing2/category/f09b0e0d24014eeda4389be72efa9e6b?st=RECENT&dt=LIST&page=1&size=40"

# # Open the website
# driver.get(url)

# # Allow time for the page to load
# time.sleep(5)  # Adjust sleep time if necessary

# # Locate the first product element
# product = driver.find_element(By.CSS_SELECTOR, "li.flu7YgFW2k._2v9tkJjlmr.SQUARE.qrPMh20xCW")

# # Scrape the required details
# title = product.find_element(By.CSS_SELECTOR, "strong._26YxgX-Nu5").text
# price = product.find_element(By.CSS_SELECTOR, "span._2DywKu0J_8").text
# desc = product.find_element(By.CSS_SELECTOR, "p._1enCFJskWo").text
# image_url = product.find_element(By.CSS_SELECTOR, "div._2JNWBGd-04 img").get_attribute("src")
# product_date = product.find_element(By.CSS_SELECTOR, "div._1GFEfXrfT_").text

# # Print the scraped details
# print("URL:", url)
# print("Title:", title)
# print("Price:", price)
# print("Description:", desc)
# print("Image URL:", image_url)
# print("Product Date:", product_date)
# print("-" * 40)

# # Close the browser
# driver.quit()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Initialize the webdriver with the specified options
driver = webdriver.Chrome()

# URLs with common CSS selectors
common_urls = [
    "https://smartstore.naver.com/f-market/category/7520bfc7be3c4d89bdff269c38df0918?st=RECENT&dt=LIST&page=1&size=40",
    "https://smartstore.naver.com/lure-s/category/1c9a0e66cb9041568191da10cd28ab37?st=RECENT&dt=LIST&page=1&size=40",
    "https://smartstore.naver.com/bigyellowtail/category/76e2515393d740c5b4c214707228d1bc?st=RECENT&dt=LIST&page=1&size=40",
]

# URL with different CSS selectors
special_url = "https://smartstore.naver.com/dasolfishing2/category/f09b0e0d24014eeda4389be72efa9e6b?st=RECENT&dt=LIST&page=1&size=40"

# Combine all URLs into a single list
all_urls = common_urls + [special_url]

# Loop through each URL
for url in all_urls:
    # Open the website
    driver.get(url)

    # Allow time for the page to load
    time.sleep(5)  # Adjust sleep time if necessary

    try:
        if url == special_url:
            # Selectors for the special URL
            product_selector = "li.flu7YgFW2k"
            title_selector = "strong._26YxgX-Nu5"
            price_selector = "span._2DywKu0J_8"
            desc_selector = "p._1enCFJskWo"
            image_selector = "div._2JNWBGd-04 img"
            date_selector = "div._1GFEfXrfT_"
        else:
            # Selectors for common URLs
            product_selector = "li._3S7Ho5J2Ql"
            title_selector = "strong._1Zvjahn0GA"
            price_selector = "strong._22XUYkkUGJ"
            desc_selector = "p._1jGpq7xfIB"
            image_selector = "div._2JNWBGd-04 img"
            date_selector = "div._1eB0tn9wSc"

        # Locate the first product element
        product = driver.find_element(By.CSS_SELECTOR, product_selector)

        # Scrape the required details
        title = product.find_element(By.CSS_SELECTOR, title_selector).text
        price = product.find_element(By.CSS_SELECTOR, price_selector).text
        desc = product.find_element(By.CSS_SELECTOR, desc_selector).text
        image_url = product.find_element(By.CSS_SELECTOR, image_selector).get_attribute("src")
        product_date = product.find_element(By.CSS_SELECTOR, date_selector).text

        # Print the scraped details
        print("URL:", url)
        print("Title:", title)
        print("Price:", price)
        print("Description:", desc)
        print("Image URL:", image_url)
        print("Product Date:", product_date)
        print("-" * 80)
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")
        print("-" * 80)

# Close the browser
driver.quit()
