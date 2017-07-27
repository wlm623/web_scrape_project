from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_page_load_timeout(4) 

for x in range(453805, 453806): #right now this is set to go to one specific page
	try:
		#driver.get("http://www.ratemyprofessors.com/ShowRatings.jsp?tid=172245")
		driver.get("http://www.ratemyprofessors.com/ShowRatings.jsp?tid="+str(x))
	except:
		pass

	try:
		close = driver.find_element_by_link_text('Close')
		close.click()
		print('succesful close cookies window')
	except:
		pass


	rows = driver.find_elements_by_xpath('//table[@class="tftable"]//tr')
	print(len(rows))

	loadmore_counter = 1

	# for x in range(0,5): #this part of the code is to test before loading lots
	# 	row=rows[x]
	# 	try:
	# 		print(row.find_element_by_xpath('*//div[@class="date"]').text)
	# 		print(row.find_element_by_xpath('*//span[@class="grade"]').text)
	# 	except:
	# 		print('fail')



	try: #This will continue to click load more until there's no more.
		# loadmore= driver.find_element_by_link_text('LOAD MORE')
		# loadmore=driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div[7]/a')
		while True:
			loadmore=driver.find_element_by_xpath('//*[@id="loadMore"]')
			driver.find_element_by_xpath('//*[@id="loadMore"]').send_keys('\n') #send_keys works better than click here
			print('clicking')
			print(loadmore_counter)
			time.sleep(4)
			loadmore_counter +=1
	except:
		pass

	rows = driver.find_elements_by_xpath('//table[@class="tftable"]//tr')
	print(len(rows))
	datecount=1
	for x in range(0,len(rows)):
		row = rows[x]
		try:
			print(row.find_element_by_xpath('*//div[@class="date"]').text)
			print(row.find_element_by_xpath('*//span[@class="grade"]').text)
			print(datecount)
			datecount+=1
			print(row.find_element_by_xpath('td[1]/div[2]/div[2]/div[1]/div/span[1]').text)
			print (x)
		except:
			print('bad x')
			#print (row) 
