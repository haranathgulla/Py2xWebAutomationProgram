# import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
# @pytest.mark.smoke
@allure.title("Open url https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
@allure.description("TC#1 - Verify Error Message-UserName")
def test_mini_project3():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='result']"))

    email = driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@gmail.com")
    # email.send_keys("test@gmail.com")

    password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
    # password.send_keys("123456")

    confirm_password = driver.find_element(By.XPATH, "//input[@id='password2']").send_keys("123456")
    # confirm_password.send_keys("123456")

    submitbtn = driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    # submitbtn.click()

    time.sleep(5)

    msgtitle = driver.find_element(By.XPATH, "//div/small")
    print(msgtitle.text)
    assert msgtitle.text == "Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(),name="Error msg", attachment_type=AttachmentType.PNG)