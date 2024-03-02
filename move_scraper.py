from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time
start_time = time.time()
move_dict={}

driver = webdriver.Chrome()
driver.get("https://www.serebii.net/attackdex-rby/")
ac=ActionChains(driver)
#There are no ID or specifing name attributes for these dropdowns so you have to
#find the location and move there manually
dropdowns = driver.find_elements(By.TAG_NAME, "select")


select = Select(dropdowns[0])
options = select.options

for index in range(1,len(options) - 1):
    select.select_by_index(index)
    #grabs the move name from the url and converts it to a string
    link = driver.current_url.split('/')[4].split('.')[0]
    link = "'" + link + "'"
    link = link.replace('-','_')
    move_dict[link] = None


    #refinds options after you move back
    dropdowns = driver.find_elements(By.TAG_NAME, "select")
    select = Select(dropdowns[0])

dropdowns = driver.find_elements(By.TAG_NAME, "select")
select = Select(dropdowns[1])
options = select.options

for index in range(1,len(options) - 1):
    select.select_by_index(index)
    #grabs the move name from the url
    link = driver.current_url.split('/')[4].split('.')[0]
    link = '"' + link + '"'
    link = link.replace('-','_')
    move_dict[link] = None

    #refinds options after you move back
    dropdowns = driver.find_elements(By.TAG_NAME, "select")
    select = Select(dropdowns[1])

    dropdowns = driver.find_elements(By.TAG_NAME, "select")


select = Select(dropdowns[2])
options = select.options

for index in range(1,len(options) - 1):
    select.select_by_index(index)
    #grabs the move name from the url
    link = driver.current_url.split('/')[4].split('.')[0]
    link = '"' + link + '"'
    link = link.replace('-','_')
    move_dict[link] = None

    #refinds options after you move back
    dropdowns = driver.find_elements(By.TAG_NAME, "select")
    select = Select(dropdowns[2])

#creates then outputs to a file
if(os.path.isfile("move_dict.py") == False):
    f = open("move_dict.py",'x')
    f.close()

with open("move_dict.py",'w') as f:
    f.write("move_dict = {\n")
    for key,value in move_dict.items():
        f.write('%s:%s\n' % (key, value ))
        f.write(",")
    f.write("}")

print (move_dict)
print("--- %s seconds ---" % (time.time() - start_time))