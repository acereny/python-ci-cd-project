from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_example_page_loads():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)

    try:
        driver.get("https://example.com")
        assert driver.title == "Example Domain"
    finally:
        driver.quit()
