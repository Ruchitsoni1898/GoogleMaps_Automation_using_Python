import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")
sleep(2)

def search_places():
    place = driver.find_element(By.CLASS_NAME,"searchboxinput.xiQnY")
    place.send_keys("Gujarat")
    submit = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input')
    submit.click()
search_places()

def directions():
    sleep(10)
    directions = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
    directions.click()
directions()
def find():
    sleep(6)
    find = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
    find.send_keys("Mumbai")
    sleep(6)
    search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
    search.click()
find()

def Kilometers():
    sleep(3)
    kilometers = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[1]')
    print("total kilometers:",kilometers.text)
    sleep(5)
    bus = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[1]')
    print("Bus travel:",bus.text)
kilometers()