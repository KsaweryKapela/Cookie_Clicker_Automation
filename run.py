from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os

from gameplay_class import GamePlay
from start_game import start_game

service = Service("C:\Devs\chromedriver.exe")
driver = webdriver.Chrome(service=service)
start_game(driver)
gameplay = GamePlay(driver)
gameplay.gameplay()
