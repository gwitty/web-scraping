import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# Random option stuff
options = webdriver.ChromeOptions()
options.add_argument('headless')
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open window
driver.set_window_size(1440,900)

# Go to drip website
driver.get('http://d.rip/discover')
time.sleep(5)

# Click the "Show more" button to get the entire list of creators
for i in range(11):
    button = driver.find_elements_by_tag_name('button')[1]
    button.click()
    time.sleep(3)

# Get the info for the site
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the artist names and put then in an array
artist_soup = soup.find_all('div', attrs={'class': 'text-truncate'})
artist_array = [i.getText() for i in artist_soup]

# Find the genres and put them in an array
genre_soup = soup.find_all('div', attrs={'class': 'pitch-bold type-14 text-uppercase h4 drip-light-gray'})
genre_array = [i.getText() for i in genre_soup]

# Find the number of subscribers and put them in an array
subs_soup = soup.find_all('p', attrs={'class': 'drip-light-gray'})
subs_array = [i.getText() for i in subs_soup]

# Smash all the arrays together
big_array = [artist_array, genre_array, subs_array]

# Transpose the array because I've done it the wrong way round
transposed_array = zip(*big_array)

# Now create a csv

import csv

with open('dripData.csv','w+') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=';')
    csvWriter.writerows(transposed_array)
