# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:38:44 2023

@author: jainil
"""

import pymongo
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import json
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['spotify']
mycol = mydb['spotify_scrapped']


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
driver = webdriver.Chrome("./chromedriver", options=chrome_options)
songs_to_json = []

cookie1 = {
    'name': 'sp_dc',
    'value': 'AQBqJuap4H0W3qcDH9ml6wNn9KbxS9Z0ts5tNJbXp4kKycJNRqj-fL-BDFomE0zDy-wjIAhGT4i9UESNucdPC87pIE0L1HVTLkT5fmuWRIL2zQFsJU9bRo13zGKA2boGOiio8IBc-aAT5hpVNglA01GARlr5ZX8',
    'domain': '.spotify.com',
    'path': '/'
    }

cookie2 = {
    'name': 'sp_gaid',
    'value': '0088fcc086a60e2c69cf4ec62b7eb7398c9798f0c1dbc3439c7568',
    'domain': '.spotify.com',
    'path': '/'
    }

cookie3 = {
    'name': 'sp_key',
    'value': '0ecab4e2-405b-4524-b874-4ab156b159ae',
    'domain': '.spotify.com',
    'path': '/'
    }


cookie4 = {
    'name': 'sp_landing',
    'value': 'https%3A%2F%2Fopen.spotify.com%2F%3Fsp_cid%3D3e46c1d8346dd262bd267fe4ebd63a93%26device%3Ddesktop',
    'domain': '.spotify.com',
    'path': '/'
    }

cookie5 = {
    'name': 'sp_last_utm',
    'value': '%7B%22utm_campaign%22%3A%22Spotify%2BNotification%2B-%2BWeb%2B%2526%2BDesktop%22%2C%22utm_medium%22%3A%22in_app%22%2C%22utm_content%22%3A%22IN_85626%22%2C%22utm_source%22%3A%22spotify%22%7D',
    'domain': '.spotify.com',
    'path': '/'
    }

cookie6 = {
    'name': 'sp_t',
    'value': '3e46c1d8346dd262bd267fe4ebd63a93',
    'domain': '.spotify.com',
    'path': '/'
    }


driver.get('https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF')

driver.add_cookie(cookie1)
driver.add_cookie(cookie2)
driver.add_cookie(cookie3)
driver.add_cookie(cookie4)
driver.add_cookie(cookie5)
driver.add_cookie(cookie6)
time.sleep(3)
body = driver.find_element(By.CSS_SELECTOR, '.Type__TypeElement-sc-goli3j-0')
actions = ActionChains(driver)
actions.click(body)
actions.key_down(Keys.DOWN).perform()

time.sleep(3)
for i in range(80):
    actions.key_down(Keys.DOWN).perform()
    time.sleep(0.01)
time.sleep(3)
soup = BeautifulSoup(driver.page_source ,'html.parser')
song_capsules = soup.find_all('div', class_='h4HgbO_Uu1JYg5UGANeQ wTUruPetkKdWAR1dd6w4')
for song_capsule in song_capsules:
    song_name = song_capsule.find('div', class_='Type__TypeElement-sc-goli3j-0 fZDcWX t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line').get_text()
    song_artist_name = [i.get_text() for i in song_capsule.find('span', class_='Type__TypeElement-sc-goli3j-0 bDHxRN rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line').find_all('a')]
    song_added_time_ago = song_capsule.find('div', class_='Type__TypeElement-sc-goli3j-0 bDHxRN Btg2qHSuepFGBG6X0yEN').get_text()
    song_album_name = song_capsule.find('a', class_='standalone-ellipsis-one-line').get_text()
    song_play_time = song_capsule.find('div', class_="Type__TypeElement-sc-goli3j-0 bDHxRN Btg2qHSuepFGBG6X0yEN").get_text()
    song_image = song_capsule.find('img', class_='mMx2LUixlnN_Fu45JpFB rkw8BWQi3miXqtlJhKg0 Yn2Ei5QZn19gria6LjZj')['src']
    print(song_capsules[0])
    song_href = song_capsule.find('a', class_='t_yrXoUO3qGsJS4Y6iXX')['href']
    
    temp_dict = {
     'song_name': song_name,
     'song_artist_name': song_artist_name,
     'song_added_time_ago': song_added_time_ago,
     'song_album_name': song_album_name,
     'song_play_time': song_play_time,
     'song_image': song_image,
     'song_href': song_href
     }    
    songs_to_json.append(temp_dict)

mycol.drop()    
mycol.insert_many(songs_to_json)

driver.quit()