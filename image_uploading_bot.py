

# The objective of this code is to automatically upload images on igem server and store it in a csv (watch naming of your files)

# This code need to download a webdriver in order to work, 
# you can download the one for google chrome here https://chromedriver.chromium.org/downloads

import time
import os
import pandas as pd
import csv
from zipfile import ZipFile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException   


path = "C://Users//example//path//document_to_pload"  # put your folder path here
igem_password = "password"
igem_id = "id"

os.chdir(path)

# # # make a dict of the files to upload
extensions = ['png', 'gif', 'jpg', 'jpeg', 'pdf', 'ppt', 'txt', 'zip', 'mp3', 'mp4', 'webm', 'mov', 'swf', 'xls', 'xlsx', 'docx', 'pptx', 'csv', 'm', 'ogg', 'gb', 'tif', 'tiff', 'fcs', 'otf', 'eot', 'ttf', 'woff', 'svg']
listdir = os.listdir()
print(listdir)
files = []
for file in listdir:
   for extension in extensions:
      if file.endswith(extension) == True:
         files.append(file)
         break
files = { file : os.path.abspath(file) for file in files }
try:
   os.mkdir('database')
except FileExistsError:
   print()
os.chdir('database')



# # # sign in in igem server

# go to igem upload
driver = webdriver.Chrome("---path//to//webdriver//webdriverdriver.exe---")  #add your webdriver path here
driver.maximize_window() # For maximizing window
driver.implicitly_wait(10) # gives an implicit wait for 20 seconds
driver.get("https://2021.igem.org/Special:Upload")

# open login bar
login = driver.find_elements_by_id('user_item')
actions = ActionChains(driver)
actions.move_to_element(login[0]).click().perform()
iframe = driver.find_element_by_id('nlogin_iframe')
driver.switch_to.frame(iframe)
# enter id
igem_id = driver.find_element_by_xpath('/html/body/form/div[1]/input[1]')
igem_id.send_keys(igem_id)
# enter password
igem_password = driver.find_element_by_name('password')
igem_password.send_keys(igem_password)
# Find login button
login_button = driver.find_element_by_name('Login')
# Click login
login_button.click()
# close and reload
driver.switch_to.default_content() #back to main
close_button = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[1]/a')
actions.move_to_element(close_button).click().perform()

# open the database table
with open('uploaded_images_database.csv', 'w', newline='') as csvfile:
   datafile = csv.writer(csvfile, delimiter=',')

   for file in files:

      # test for warning message before each iteration
      try:
         warning = driver.find_element_by_class_name('warning')
      except NoSuchElementException:      
         warning = False
      if warning != False:
         driver.back()     # if warning just return to previous tab
      
      time.sleep(2)
      # upload the file from local folder
      choose_file_box = driver.find_element_by_name('wpUploadFile')
      choose_file_box.send_keys(files[file])
      # write the correct file name
      id_box = driver.find_element_by_name('wpDestFile')
      id_box.clear()
      id_box.send_keys('T--Paris_Bettencourt--'+str(file))
      time.sleep(2)
      # scroll down
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      # click upload button
      upload_box = driver.find_element_by_name('wpUpload')
      upload_box.click()
      # test for warning message of already uploaded files

      try:
         warning = driver.find_element_by_class_name('warning')
      except NoSuchElementException:      
         warning = False
      # ignore the warning
      if warning != False:
         skip_button = driver.find_element_by_name('wpUploadIgnoreWarning')
         skip_button.click() 
         
      image_url = driver.find_element_by_class_name('filehistory-selected')
      actions = ActionChains(driver)
      actions.move_to_element(image_url).click().perform()
      files[file] = driver.current_url
      driver.back()
      driver.back()
      row = (str(file), str(files[file]))
      datafile.writerow(row)

driver.quit()

