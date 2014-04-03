from selenium import webdriver
import unittest

class SearchGoogle(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_Google(self):
		self.driver.get("https://www.google.com")
		#Now I will be looking for google's search box by selecting it using xpath. 
		searchbox = self.driver.find_element_by_xpath("//input[@id = 'gbqfq']")
		searchbox.send_keys("Take the bridge to the Jersey Side")
		#Looking now for the search button to click and run the search
		button = self.driver.find_element_by_xpath("//div[@id = 'gbqfbw']/button[@id = 'gbqfb']/span")
		button.click()

	def tearDown(self):
		self.driver.close()
		self.driver.quit()


if __name__ == "__main__":
	#verbostiy indicates the explanation amount required in case an error occurs
	unittest.main(verbosity = 2)
	
