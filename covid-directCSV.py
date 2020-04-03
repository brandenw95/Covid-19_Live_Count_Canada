import csv
import requests
from datetime import datetime
import os

def download_file():
    url = 'https://health-infobase.canada.ca/src/data/covidLive/covid19.csv'
    r = requests.get(url, allow_redirects=True)
    open('covid19.csv', 'wb').write(r.content)

def grab_time():
    
    #Current time in 12-hour time (ex. 12:34 AM)
    CurrentDate_original = datetime.now()
    new_time = CurrentDate_original.strftime("%d-%m-%Y")
    final_time = str(new_time)

    return final_time


def main():

    download_file()

    grab_time()
    os.system('color 0a')
    os.system('mode con: cols=55 lines=35')
    file_in = open('covid19.csv', 'r')
    reader = csv.reader(file_in)

    header = next(reader)

    sortedlist = sorted(reader, key=lambda row: row[4], reverse=False)
    bc_sorted = []

    #print(header)
    for items in sortedlist:

        if items[3] == grab_time():
            bc_sorted.append(items)
        else:
            pass

    bc_sorted = sorted(bc_sorted, key=lambda row: row[4], reverse=True)

    print("LIVE - Cases of Covid through the country")
    print("-----------------------------")
    print('')
    for x in bc_sorted:
        
        print(x[1] + ': ', end='')
        print(x[4])
        print('')
    
    
    file_in.close()
    
    os.remove('covid19.csv')

    os.system('pause')


if __name__ == "__main__":
    main()