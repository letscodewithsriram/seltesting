# This is a sample Python script.

# Press ` to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.airindia.com")
ddelement= Select(driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/flight-booking/div/div/div[3]/div[1]/app-desktop-search-flight/form/div/div[1]/div[1]/mat-form-field/div"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
