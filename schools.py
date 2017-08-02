from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time

import datetime
starttime=datetime.datetime.now()
print(starttime)


csv_file = open('school.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(sorted(['school','date', 'reputation', 'location', 'internet', 'food', 'facilities', 'social', 'happiness', 'opportunities','clubs', 'helpful', 'unhelpful','rank']))
chop.add_extension('Adblock-Plus_v.crx')
driver = webdriver.Chrome(chrome_options = chop)


with open('forbeslistmatch.csv', 'r') as f:
    reader = csv.reader(f)
    school_list = list(reader)
    url_list=[]
    for row in school_list:
    	url_list.append(row[1])

url_list=['http://www.ratemyprofessors.com/campusRatings.jsp?sid=709']#,'http://www.ratemyprofessors.com/campusRatings.jsp?sid=1100', 
#'http://www.ratemyprofessors.com/campusRatings.jsp?sid=474',
#'http://www.ratemyprofessors.com/campusRatings.jsp?sid=1085', 'http://www.ratemyprofessors.com/campusRatings.jsp?sid=1270','http://www.ratemyprofessors.com/campusRatings.jsp?sid=1161']

counter=0
for url in url_list: #right now this is set to go to one specific page
	review_dict = {}
	try:
		try:
			#driver.get("http://www.ratemyprofessors.com/ShowRatings.jsp?tid=172245")
			driver.get(url) 
			counter+=1

		except:
			pass

		try:
			close = driver.find_element_by_link_text('Close')
			close.click()
			print('succesful close cookies window')
		except:
			pass

		# last=driver.find_element_by_xpath('*//span[@class="plname"]').text
		# first=driver.find_element_by_xpath('*//span[@class="pfname"]').text
		# school = driver.find_element_by_xpath('*//a[@class="school"]').text
		# subject = driver.find_element_by_xpath('*//div[@class="result-title"]').text.split('\n')[0] #multiple rows of text.
		# number = driver.find_element_by_xpath('*//div[@class="table-toggle rating-count active"]').text
		# number = int(number.split(' ')[0])
		# print(number)

		# rows = driver.find_elements_by_xpath('//table[@class="tftable"]//tr')
		# #we see the number of rows initially and decide if we need to load more pages
		# print(len(rows))

		school = driver.find_element_by_xpath('//div[@class="top-info-block"]//span').text
		print('-'*50)
		print(counter, school)
		#print(i, school)
		number = driver.find_element_by_xpath('//div[@class="table-toggle rating-count active h1"]').text
		number = int(number.split(' ')[0])
		

		loadmore_counter = 1 #for debugging purposes
		stop=0 #we have a stopper to avoid infinite while loop
		ad_number=0 
		rows = driver.find_elements_by_xpath('//table[@class="school-ratings"]//tr')
		try: #This will continue to click load more until there's no more.
			while (loadmore_counter < 10 and stop<50):
			#while ((len(rows)-ad_number)<number and stop<20): 
				try:
					loadmore=driver.find_element_by_xpath('//*[@id="loadMore"]')
					driver.find_element_by_xpath('//*[@id="loadMore"]').click()
					print('load:', loadmore_counter) #for debugging
					loadmore_counter +=1
					time.sleep(1)
					rows = driver.find_elements_by_xpath('//table[@class="school-ratings"]//tr')
					stop +=1
					try:
						ads = driver.find_elements_by_xpath('//tr/td[@class="ad-placement"]') #this is called ad-placement-container in profs
						ad_number=len(ads)
						true_number = len(rows)-ad_number
						#print(true_number, number)
						if true_number>number:
							break
						#print('true number', len(rows)-len(ads)) #this is the true number of entries
					except:
						pass
				except:
					stop +=1
					print('stopping')

		except:
			pass



		rows = driver.find_elements_by_xpath('//table[@class="school-ratings"]//tr')

		for x in range(0,len(rows)):
			#review_dict = {}
			row = rows[x]
			try:
				entry=row.text.split('\n')
				review_dict['rank'] = counter
				review_dict['school']=school
				review_dict['date'] = entry[0]
				review_dict['reputation'] = entry[1]
				review_dict['location'] = entry[3]
				review_dict['internet']= entry[5]
				review_dict['food'] = entry[7]
				review_dict['facilities']= entry[9]
				review_dict['social'] = entry[11]
				review_dict['happiness'] = entry[13]
				review_dict['opportunities'] = entry[15]
				review_dict['clubs'] = entry[17]
				meta = entry[-2]
				metalist = [s for s in meta.split(' ') if s.isdigit()]
				helpful = int(metalist[0])
				unhelpful = int(metalist[1])
				review_dict['helpful'] = helpful
				review_dict['unhelpful']=unhelpful

				keys_sorted = sorted(review_dict.keys())

				values_sorted = [review_dict[key] for key in keys_sorted]
				# review_dict['grade'] = grade
				#print(review_dict.keys())
				writer.writerow(values_sorted) #PUT THIS BACK IN!
				# print(review_dict)
				#print(row.find_element_by_xpathpr('td[1]/div[2]/div[2]/div[1]/div/span[1]').text)
				#print (x)


				
				
			except:
				pass
	except:
		print('there has been an error!!!!')
		print(url)
csv_file.close()
endtime=datetime.datetime.now()
print(endtime)
print(endtime-starttime)

