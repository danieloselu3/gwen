# # imports
# import requests

# # target url
# url = "https://api.betika.com/v1/uo/matches?.json"

# # get our url
# games = requests.get(url).json()

# # todays games
# games_container = games['data']

# # loop and display the games
# for game in games_container:
#     home_team = game['home_team']
#     away_team = game['away_team']
#     print('{} vs {}'.format(home_team, away_team))

# implementation using Selenium
# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

# chrome execution path
exe = '/home/daniel/chromedriver'

# create our driver
driver = webdriver.Chrome(exe)

# declare our url
url = 'https://www.betika.com/'

# get our page
driver.get(url)

# implicitly wait for the page to load
driver.implicitly_wait(10)

# find critical target buttons
# log_in_button = driver.find_element_by_class_name('login__button')
# user_name = driver.find_element_by_name('phone')
# pass_word = driver.find_element_by_name('password')
# submit_button = driver.find_element_by_class_name('modal__button')
game_highlights = driver.find_element_by_class_name('home__matches__items')

# get our maatches
while True:
    # declare our action chain
    action_chain = ActionChains(driver)
    # move to our element
    action_chain.move_to_element(game_highlights)
    # click to give it focus
    action_chain.click()
    # scroll down 5 times to load all games
    action_chain.send_keys([Keys.PAGE_DOWN for i in range(5)])
    # perform these actions
    action_chain.perform()

# display a text
input("Press enter to close automated page!")

# close chrome
driver.quit()



