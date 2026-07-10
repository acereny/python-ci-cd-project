from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_example_page_loads():
    options = Options()

    # Tarayıcı penceresini göstermeden çalıştırır.
    options.add_argument("--headless=new")

    # GitHub Actions gibi Linux ortamlarında daha sorunsuz çalışmasını sağlar.
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://example.com")

        assert driver.title == "Example Domain"

    finally:
        driver.quit()