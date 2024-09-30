#This was made for the updated README.md. I wanted to have a complete checklist of all the 
#problems, as well as a link, but writing it all would have been very tedious. This was also
#a good opportunity to practice web scraping.

import requests
from bs4 import BeautifulSoup as bs
from requests.auth import HTTPBasicAuth

#Following a guide fromm https://realpython.com/beautiful-soup-web-scraper-python/

url = "https://projecteuler.net/archives;page=" #The page number will be added to the end of the url using a for loop
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101     Firefox/108.0"} #https://stackoverflow.com/questions/74868953/beautifulsoup-returning-none-when-element-exists

basic = HTTPBasicAuth("scraper", "scraper1") #https://docs.python-requests.org/en/latest/user/authentication/

problems = []

for i in range (1, 19): #There are 18 pages of problems
    page = requests.get(url+str(i), headers=headers, auth=basic)

    soup = bs(page.content, "html.parser")

    results = soup.find(id="problems_table")
    
    problemLinks = results.find_all("a")

    for problemLink in problemLinks:
        problemName = problemLink.text
        problemURL = f"https://projecteuler.net/{problemLink['href']}"
        
        #We now need to format it to use in the markdown file

        problemFormated = f"- [ ] [{problemName}]({problemURL})"

        problems.append(problemFormated)

for i in problems: 
    print(i)
