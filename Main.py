from selenium import webdriver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username
        self.password = password
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    
my_bot = InstaBot('HereWeGo.SIK','kis@164264')


 