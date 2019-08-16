import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# source_code = requests.get('http://fantasy.espn.com/basketball/league/standings?leagueId=633975')

options = webdriver.ChromeOptions()
options.add_argument('headless')
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
# driver = webdriver.Chrome(chrome_options=options, desired_capabilities=capa)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1440,900)
driver.get('http://d.rip/discover')
time.sleep(5)

#plain_text = driver.page_source
#soup = BeautifulSoup(plain_text, 'lxml')

#soup.select('.Table2__header-row') # Returns full results.

#len(soup.select('.Table2__header-row')) # 8

for i in range(11):
    button = driver.find_elements_by_tag_name('button')[1]
    button.click()
    time.sleep(3)

#num_artists = len(driver.find_elements_by_class_name('text-truncate'))

#print(num_artists)

soup = BeautifulSoup(driver.page_source, 'html.parser')
artist_soup = soup.find_all('div', attrs={'class': 'text-truncate'})
artist_array = [i.getText() for i in artist_soup]

genre_soup = soup.find_all('div', attrs={'class': 'pitch-bold type-14 text-uppercase h4 drip-light-gray'})
genre_array = [i.getText() for i in genre_soup]

subs_soup = soup.find_all('p', attrs={'class': 'drip-light-gray'})
subs_array = [i.getText() for i in subs_soup]

big_array = [artist_array, genre_array, subs_array]

transposed_array = zip(*big_array)

####

import csv

with open('dripData.csv','w+') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=';')
    csvWriter.writerows(transposed_array)
