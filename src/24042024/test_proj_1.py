# import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# @pytest.mark.smoke
@allure.title("Open url katalon-demo-cura.herokuapp.com website")
@allure.description("TC#1 - Check Make Appointment text on Webpage.")
def test_miniProject1():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(By.ID,"btn-make-appointment").click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)
    driver.find_element(By.NAME,"username").send_keys("John Doe")
    driver.find_element(By.NAME, "password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID,"btn-login").click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    verify_app_text = driver.find_element(By.XPATH,"//div//h2")
    assert verify_app_text.text == "Make Appointment"
    time.sleep(20)





    # <input type="text" class="form-control" id="txt-username" name="username" placeholder="Username" value="" autocomplete="off">
# <input type="password" class="form-control" id="txt-password" name="password" placeholder="Password" value="" autocomplete="off">
# <button id="btn-login" type="submit" class="btn btn-default">Login</button>
# <h2>Make Appointment</h2>