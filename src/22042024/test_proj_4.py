# import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
# @pytest.mark.smoke
@allure.title("Open url https://www.ebay.com/")
@allure.description("TC#1 - Search for the 16 gb")
def test_mini_project4():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='gh-ac']").send_keys("16gb")
    driver.find_element(By.XPATH,"// input[ @ value = 'Search']").click()
    # allure.attach(driver.get_screenshot_as_png(), name='Product_Page_Screenshot', attachment_type=AttachmentType.PNG)
    time.sleep(1)
    list_element = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for item in list_element:
        product_name = item.text
    price_of_elements = driver.find_elements(By.XPATH,"//span[@class='s-item__price']")
    price = []
    for item in price_of_elements:
        text = item.text
        x = text.replace("$", "").strip()
        price.append(x)
    price.sort()
    print(f"Product having: {price[1]}")
    time.sleep(1)



