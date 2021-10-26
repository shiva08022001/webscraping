import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import csv

def editcart(li2):
    editcart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "hlb-view-cart-announce")))
    editcart.click()
    pricee = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "a-spacing-small")))
    li2.append(pricee.text)
    editcart2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "a-autoid-0-announce")))
    editcart2.click()
    editcart3 = driver.find_element_by_id('dropdown1_10')
    editcart3.click()
    quantity = driver.find_element_by_name("quantityBox")
    quantity.click()
    quantity.send_keys(Keys.BACK_SPACE)
    quantity.send_keys("999")
    quantity.send_keys(Keys.RETURN)
    try:
        quantityLeft = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-alert-content")))
        li2.append(quantityLeft.text)
        deletecart = driver.find_element_by_class_name('a-color-link')
        deletecart.click()
    except:
        msg="999+ quantity left"
        li2.append(msg)
        deletecart = driver.find_element_by_class_name('a-color-link')
        deletecart.click()
    return li2
    

def cookie():
    try:
        cookies = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "sp-cc-accept")))
        cookies.click()
    except:
        print("No Cookies")


def products():
    product = driver.find_elements_by_class_name('a-section.a-spacing-none.aok-relative')  #div element for product
    leng = len(product)+2
    for i in range(leng):
        li=[]
        li2=[]
        product[i].click()
        if(i==0):
            cookie()
        productname = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "title")))
        li2.append(i+1)
        li2.append(productname.text)     
        try:
            try:
                addtocart1 = driver.find_element_by_xpath('//*[(@id ="add-to-cart-button")]')
                addtocart1.click() 
                li2 = editcart(li2)
                driver.back()
                driver.back()
                driver.back()
                product = driver.find_elements_by_class_name('a-section.a-spacing-none.aok-relative')
                li.append(li2)
                datascrap(li)
                if(i+3==leng):
                    try:
                        nextpage()
                    except:
                        li3=[]
                        li3.append("Last Page Reached")
                        datascrap(li3)
                        break               
            except:
                addtocart1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "See All Buying Options")))
                addtocart1.click() 
                time.sleep(5)
                addtocart2 = driver.find_element_by_name("submit.addToCart")
                addtocart2.click()
                li2 = editcart(li2)
                driver.back()
                driver.back()
                driver.back()
                driver.back()
                product = driver.find_elements_by_class_name('a-section.a-spacing-none.aok-relative')
                li.append(li2)
                datascrap(li)
                if(i+3==leng):
                    try:
                        nextpage()
                    except:
                        li3=[]
                        li3.append("Last Page Reached")
                        datascrap(li3)
                        break
                continue
        except:
            li2.append("Product Unavailable")
            li.append(li2)
            datascrap(li)
            driver.back()
            product = driver.find_elements_by_class_name('a-section.a-spacing-none.aok-relative')    
            if(i+2==leng):
                try:
                    nextpage()
                except:
                    li3=[]
                    li3.append("Last Page Reached")
                    datascrap(li3)
                    break
            continue

def nextpage():
    nextpage = driver.find_element_by_class_name('a-last')
    nextpage.click()
    product = driver.find_elements_by_class_name('a-section.a-spacing-none.aok-relative')
    i=0
    products()

def datascrap(li):
    os.chdir('C:\\Users\sanjay\Desktop\mbscrap')
    with open('pro.csv','a') as f:
        writer=csv.writer(f)
        writer.writerows(li)

path = r"C:\bin\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.amazon.co.uk/gp/bestsellers/baby/21731957031")

time.sleep(5)
cookie()
products()