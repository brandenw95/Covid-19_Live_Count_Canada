import csv
import requests
from datetime import datetime
import os

def download_file():

    #Download live data from the official candian government website
    url = 'https://health-infobase.canada.ca/src/data/covidLive/covid19.csv'
    r = requests.get(url, allow_redirects=True)
    open('covid19.csv', 'wb').write(r.content)

def grab_time():
    
    #Grab todays date
    CurrentDate_original = datetime.now()
    new_time = CurrentDate_original.strftime("%d-%m-%Y")
    final_time = str(new_time)

    return final_time


def main():

    #download current csv file from canada.ca
    download_file()

    os.system('color 0a')
    os.system('mode con: cols=55 lines=35')

    #Open  CSV file and create a reader object 
    file_in = open('covid19.csv', 'r')
    reader = csv.reader(file_in)

    #Grab header from csv file and advance the iterator
    header = next(reader)

    #Sort list
    sortedlist = sorted(reader, key=lambda row: row[4], reverse=False)
    bc_sorted = []

    #Refine the list of provinces
    for items in sortedlist:
        if items[3] == grab_time():
            bc_sorted.append(items)
        else:
            pass

    #Sort by largest first 
    bc_sorted = sorted(bc_sorted, key=lambda row: row[4], reverse=True)

    print("LIVE - Cases of Covid through the country")
    print("-----------------------------")
    print('')
    
    #Print all provences with total daily confirmed cases
    for x in bc_sorted:
        
        print(x[1] + ': ', end='')
        print(x[4])
        print('')
    
    #Closing maintenance
    file_in.close()
    os.remove('covid19.csv')
    os.system('pause')


if __name__ == "__main__":
    main()