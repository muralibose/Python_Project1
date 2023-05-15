import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with

def TC_Login_01():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
    driver.maximize_window();
    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("Admin");
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123");
    driver.find_element(By.TAG_NAME, "button").click();

def TC_Login_02():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
    driver.maximize_window();
    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("Admin");
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin");
    driver.find_element(By.TAG_NAME, "button").click();
    time.sleep(5)
    invalid = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")
    invalid_msg = invalid.text
    print("Error Message is: ",invalid_msg)

def TC_Login_03():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
    driver.maximize_window();
    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("Admin");
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123");
    driver.find_element(By.TAG_NAME, "button").click();
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "PIM").click();
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Add Employee").click();
    time.sleep(3)
    driver.find_element(By.NAME, "firstName").send_keys("Mahendra");
    driver.find_element(By.NAME, "middleName").send_keys("Singh");
    driver.find_element(By.NAME, "lastName").send_keys("Dhoni");
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click();
    time.sleep(8)
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("Mr.Cool");
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input").send_keys("TN448383883");
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").send_keys("2028-05-20");
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input").send_keys("9575757");
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input").send_keys("7575757");
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i").click();
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]").click();
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i").click();
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i").click();
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input").send_keys("1981-07-07");
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span").click();
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input").send_keys("No");
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click();

def TC_Login_04():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
    driver.maximize_window();
    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("Admin");
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123");
    driver.find_element(By.TAG_NAME, "button").click();
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "PIM").click();
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click();
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i").click();

TC_Login_01();
TC_Login_02();
TC_Login_03();
TC_Login_04();

