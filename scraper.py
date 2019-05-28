from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import json

def storeData(userResponse , containerData): #user response takes 1 or 0
	data_scraped = []
	if userResponse == "1": #this block prints only first instance
		data_scraped.append(containerData[0])
		print(data_scraped)
		print("Done! All instances have been appended!")
		userResponse = input("ready to write data to a txt file! press enter to write")
		#writes data to txt file
		writeData(data_scraped)
	else:
		for container in containerData:
			data_scraped.append(container)
			print(data_scraped)
		print("Done! All instances have been appended!")
		userResponse = input("ready to write data to a txt file! press enter to write")
		#writes data to txt file
		writeData(data_scraped)

#Takes data in form of an array
def writeData(scrapeList):
	data = {}
	data['Scraped_Data'] = []

	for htmlScraped in scrapeList:
		print(htmlScraped)  #delete
		print("----------") #delete
		data['Scraped_Data'].append({  
			'DATA': '{}'.format(htmlScraped)
		})
		
	with open('data.json', 'w') as outfile:  
    		json.dump(data, outfile, sort_keys=True,indent=4) #json formatting
    		# json.dumps(data, sort_keys=True,indent=4)
		

	print("Your json file has been created! Look in the directory")
	input("Press enter to exit program.")

	exit()
	#finish program by making writing the scraped data to a txt that
	#the user will be able to then extract from file location

#html parser for getting a webpage
def getweb():
	worked = False
	while worked == False:
		try:
			hdr = {'User-Agent': 'Mozilla/5.0'}
			userinput = input('What website would you like to scrape?(full link): ')
			my_url = userinput
			#Opens and closes page, stores it into a variable before dump.
			page = Request(my_url, headers=hdr)
			uClient = urlopen(page)
			page_html = uClient.read()
			uClient.close()
			worked = True
			return page_html
		except Exception as e:
			print(e)
			print("could not find website, retry")

#tested link
#'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'


#this does the html parsing
page_soup = soup(getweb(), "html.parser")

user_atr = input("what would you like to look for? i.e: div, a...\n: ")
userinput = input("Whould you like to look for an object associated with that?\ni.e class='stuff', class being object, stuff being identification\n(1)yes\n(2)no\n: ")

if userinput == "1":
	user_object = input("object?: ")
	user_id = input("object identification: ")
	containers = page_soup.find_all(user_atr,{user_object:user_id})
elif(userinput =="2"):
	containers = page_soup.find_all(user_atr)
else:
	containers = page_soup.find_all(user_atr)

print(containers)
# "class":"item-container"
#grabs all the products with the specific class and div (all products)
# containers = page_soup.find_all(user_atr,{"class":"item-container"})
container = containers[0]
# print(container.text)
print(container.find("href"))
# for container in containers:
# 	print(container.a.img["title"])

# print(container, "\n-------")

userinput = input("Continue searching?(1)yes(2)no:")
if userinput == "1":
	pass
else:
	userinput = input("Would you like to append this instance? or all occuring instances?\n(1)this only(2)all instances : ")
	storeData(userinput, containers)



user_atr = input("what would you like to look for? i.e: div, a...\n: ")
userinput = input("Whould you like to look for an object associated with that?\ni.e class='stuff', class being object, stuff being identification\n(1)yes\n(2)no\n: ")

subcontainers = []

if userinput == "1":
	user_object = input("object?: ")
	user_id = input("object identification: ")
	for container in containers:
		sub = container.find(user_atr,{user_object:user_id})
		subcontainers.append(sub)
elif(userinput =="2"):
	for container in containers:
		sub = container.find(user_atr)
		subcontainers.append(sub)
else:
	for container in containers:
		sub = container.find(user_atr)
		subcontainers.append(sub)
for containers in subcontainers:
	print(containers,"\n---")
userinput = input("Would you like to append this instance? or all occuring instances?\n(1)this only(2)all instances : ")
storeData(userinput, subcontainers)

# isdone = ""

# while isdone != "done":
# 	try:
# 		route = "container"
# 		userinput = input("what extensions would you like to search for?\n seperate each denotion with a space \n ex: div div img[\"title\"]\n: ")
# 		inputRoute = userinput.split(' ')
# 		for i in range(len(inputRoute)):
# 			route += "." + inputRoute[i]
# 		# print(container.find_all())
# 		newContainer = eval(route)
# 		print("---\n"+route+"\n---")
# 		print("Current Route ^\n---")
# 		print("output:\n", newContainer,"\n---")

# 		isdone = input("are you happy with these extensions? \n type 'done' when happy\n or enter to change extension\n: ")	
# 	except Exception as e:
# 		print(e)
# 		input("Make sure their is no leftover spaces\npress enter to continue")
# userinput = input("Would you like to append this instance? or all occuring instances?\n(1)this only(2)all instances : ")
# storeData(userinput, newContainer)
