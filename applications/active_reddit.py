from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


browser = None


def get_reddit(amount):
    global browser
    num_full_pages = int(amount//10)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(5)

    browser.get('https://www.reddit.com/r/memes/')
    time.sleep(random.randrange(1, 2))

    if num_full_pages != 0:
        for _ in range(0, num_full_pages):
            browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3, 5))

    result = []

    hrefs = browser.find_elements_by_tag_name('a')

    urls = []
    for item in hrefs:
        if "/r/memes/comments/" in item.get_attribute('href'):
            urls.append(item.get_attribute('href'))

    for url in urls[:amount+6]:
        browser.get(url)
        time.sleep(random.randrange(2, 5))

        try:
            description = browser.find_element(
                By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[3]/div[1]/div/h1").text
        except:
            description = 'Description not found'

        try:
            image = browser.find_element(
                By.XPATH,  '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[5]/div/a').get_attribute('href')
        except:
            image = 'Picture not found'

        try:
            reviews = browser.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[6]/div[1]/a/span').text
        except:
            reviews = "No comments found"

        if image != "Picture not found":
            result.append({
                'description': description,
                'image': image,
                'link': url,
                'statistics': reviews
            })
            if len(result) == amount:
                break

    return result[:amount]


def close_browser():
    global browser
    browser.quit()
