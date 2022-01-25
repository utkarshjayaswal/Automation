from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

username = input('Enter Your Username:')  # Input your email address of facebook in the terminal
password = input('Enter Your Password:')  # Input your password of facebook in the terminal
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print("Opened facebook")
sleep(2)
username_box = driver.find_element_by_id('email')
username_box.send_keys(username)
print("Your user name has been entered")
sleep(1)
password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)
print("you password has been entered")
login_box = driver.find_element_by_name('login')
login_box.click()
print("Done")
input('You can type quit to exit from the program')
driver.quit()
print("Finished")
