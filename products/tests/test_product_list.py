import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestProductList:

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # для работы в headless режиме
        chrome_options.add_argument("--no-sandbox") #для работы внутри контейнера
        chrome_options.add_argument('--disable-dev-shm-usage')

        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
        cls.driver.get('http://localhost:8000/')

    @pytest.mark.django_db
    def test_product_card_exists(self):
        product_cards = self.driver.find_elements(By.CLASS_NAME, 'product-container')
        assert len(product_cards) > 0, 'No product cards found.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()