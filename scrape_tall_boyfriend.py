from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np
from time import sleep

# initiate selenium web driver
browser = webdriver.Safari()
url = 'https://www.webtoons.com/en/slice-of-life/my-giant-nerd-boyfriend/001-introduction/viewer?title_no=958&episode_no=1'
# open url
browser.get(url)

# empty lists to store comments and dates from comment section
comments = []
dates = []

while True:
    # iterate through the pages in the page number box
    # (for ex. pages 1-10 is the first page number box, pages 11-20 is the second page number box, etc.)
    for i in range(0, len(browser.find_elements_by_class_name('u_cbox_page'))):
        # find all comment boxes
        comment_li = BeautifulSoup(browser.page_source, 'html.parser').find_all('li', class_='u_cbox_comment')
        for container in comment_li:
            # for each comment box
            # extract comment
            comment = container.find('span', class_='u_cbox_contents').text if container.find('span', class_='u_cbox_contents') else '-'
            # extract date
            date = container.find('span', class_='u_cbox_date').text if container.find('span', class_='u_cbox_date') else '-'
            # add comment to the comments list
            comments.append(comment)
            # add date to the dates list
            dates.append(date)
        # click page i in the page box
        browser.find_elements_by_class_name('u_cbox_page')[i].click()
        # wait 5 seconds before clicking the next page
        sleep(5)

    try:
        # after all the pages in the current page number box are clicked (for ex. pages 1-10),
        # click the 'next' button to navigate to the next page number box (ex. cont. pages 11-21)
        browser.find_element_by_class_name('u_cbox_next').click()
    except ElementNotInteractableException:
        # if the current page number box is the last one, end the loop
        break
    # wait 5 seconds before clicking the next page number box
    sleep(5)

# create pandas dataframe containing the comments and their corresponding post dates
tall_boyfriend_comments = pd.DataFrame({
    'comment': comments,
    'date': dates})

# export the dataframe as a .csv file
tall_boyfriend_comments.to_csv('tall_boyfriend_comments.csv')

# close the selenium browser
browser.quit()
