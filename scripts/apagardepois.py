from selenium import webdriver

from flask import Flask, jsonify
import asyncio
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


import os

import time

chrome_options = webdriver.ChromeOptions()

# Configurar opções para aceitar cookies
chrome_options.add_argument("--enable-automation")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")

driver = webdriver.Remote(command_executor='http://84.247.187.208:4444/wd/hub', options=chrome_options)

driver.get("https://youtube.com.br")
