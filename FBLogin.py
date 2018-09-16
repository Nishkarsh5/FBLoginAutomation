from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait

class FBlogin(unittest.TestCase):
	
	def setUp(self):
		
		self.WebDriverWait	=	webdriver.Chrome(r"C:\Users\Nishkarsh\AppData\Local\Programs\Python\Python36-32\Scripts\chromedriver.exe")
		self.driver.get("http:://www.facebook.com")
		self.driver.maximize_window()

	def test_login(self):
		
		driver = self.driver
		facebookUsermane	=	'usermane'	#Replacec it with your username.
		facebookPassword	=	'password'	#Replace it with your password.
		
		emailFieldID		=	"email"
		passFieldID			=	"pass"
		loginButtonXpath	=	'//input[@value="Log In"]'
		fbLogoXpath			=	'//a(contains[@href, "logo"])[1]'

		emailFieldElement	= 	WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
		passFieldElement	=	WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
		loginButtonElement	=	WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
		
		emailFieldElement.clear()
		emailFieldElement.send_keys(facebookUsermane)
		passFieldElement.clear()
		passFieldElement.send_keys(facebookPassword)
		loginButtonElement.clear()
		loginButtonElement.click()
		
		WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

	def tearDown(self):
		
		self.driver.close()

if __name__ == '__main__':
		
		unittest.main()		

