import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import itertools
from datetime import datetime
from collections import OrderedDict
from operator import itemgetter

def grab_time():
    
    #Current time in 12-hour time (ex. 12:34 AM)
    CurrentDate_original = datetime.now()
    new_time = CurrentDate_original.strftime("%I:%M %p")
    current_date = CurrentDate_original.strftime('%B %d %Y')
    final_time = 'Last Updated on ' +  str(current_date) + ' at ' +  str(new_time)

    return final_time

def grab_data(driver):

    Canada_Total = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[1]/span[2]').text
    British_Columbia = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[4]/span[2]').text
    Alberta = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[5]/span[2]').text
    Saskatchewan = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[6]/span[2]').text
    Manitoba = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[10]/span[2]').text
    PEI = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[12]/span[2]').text
    Ontario = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[3]/span[2]').text
    Quebec = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[2]/span[2]').text
    Nova_Scotia = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[8]/span[2]').text
    New_Brunswick =  driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[9]/span[2]').text
    Newfoundland_and_labrador = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[7]/span[2]').text
    Yukon = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[13]/span[2]').text
    North_West_territories = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[14]/span[2]').text
    Nunavut = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/ul[2]/li[15]/span[2]').text

    provinces = [

        Canada_Total,
        British_Columbia,
        Alberta,
        Saskatchewan,
        Manitoba,
        PEI,
        Ontario,
        Quebec,
        Nova_Scotia,
        New_Brunswick,
        Newfoundland_and_labrador,
        Yukon,
        North_West_territories,
        Nunavut
    ]
    province_names = [

        'Canada Total',
        'British Columbia',
        'Alberta',
        'Saskatchewan',
        'Manitoba',
        'PEI',
        'Ontario',
        'Quebec',
        'Nova Scotia',
        'New Brunswick',
        'Newfoundland and labrador',
        'Yukon',
        'North West territories',
        'Nunavut'
    ]
    for provinces, infected in zip(province_names, provinces):
       print(provinces + ': ' + infected)
       print()



def main():

    clear = lambda: os.system('cls')
    os.system('color 0a')
    os.system('mode con: cols=55 lines=35')
    clear()

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--disable-gpu')
    options.add_argument('log-level=3')
    options.add_argument('--disable-extensions')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://ici.radio-canada.ca/info/2020/coronavirus-covid-19-pandemie-cas-carte-maladie-symptomes-propagation/')
    time.sleep(0.5)


    while True:

        clear()
        grab_data(driver)
        print('-----------------------')
        final_time = grab_time()
        print(final_time)
        time.sleep(60)

if __name__ == "__main__":
    main()