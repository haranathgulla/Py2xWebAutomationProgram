# import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
# @pytest.mark.smoke
@allure.title("Open url https://www.idrive360.com/enterprise/login")
@allure.description("TC#1 - Verify that Trial is finished and current URL")
def test_mini_project2():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    email = driver.find_element(By.XPATH,"//input[@id='username']").send_keys("augtest_040823@idrive.com")
    password = driver.find_element(By.XPATH,"//input[@id='password']").send_keys("123456")
    sign_in = driver.find_element(By.ID,"frm-btn").click()
    time.sleep(40)
    allure.attach(driver.get_screenshot_as_png(), name="My Account-screenshot", attachment_type=AttachmentType.PNG)
    # allure.attach(driver.get_screenshot_as_png(), name="login_screenshot", attachment_type="upgradenow")
    print(driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true")
    verify_Text = driver.find_element(By.XPATH,"//h5[@class='id-card-title']")
    assert verify_Text.text == "Your free trial has expired"
    print(verify_Text)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    time.sleep(3)

    # verify_current_url = driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    # verify_Text = driver.find_element(By.XPATH,"//h5[@class='id-card-title']")
    # assert verify_Text.text == "Your free trial has expired"
    # assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    # print(verify_current_url)
    # print(verify_Text)
    # time.sleep(10)


    # time.sleep(5)
    # sigin = driver.find_element(By.ID,"frm-btn").click()
    # allure.attach(driver.get_screenshot_as_png(), name="login_screenshot", attachment_type="upgradenow")
    # print(driver.current_url)
    # assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    # verify_current_url = driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    # driver.find_element(By.XPATH,"//h5[@class='id-card-title']")
    # assert verify_Text.text == "Your free trial has expired"
    # assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    # time.sleep(10)



# <button _ngcontent-lbx-c4="" class="id-btn id-info-btn-frm" id="frm-btn" type="submit">Sign in</button>
# <h5 _ngcontent-beh-c10="" class="id-card-title">Your free trial has expired</h5>
