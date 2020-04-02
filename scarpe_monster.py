import requests
from bs4 import BeautifulSoup

url = "https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="ResultsContainer")

job_elements = results.find_all('section', class_= "card-content")

for job in job_elements:
    title_ele = job.find('h2', class_="title")
    company = job.find('div', class_='company')
    location = job.find('div', class_="location")
    if None in (title_ele, company, location):
        continue
    print(title_ele.text)
    print(company.text)
    print(location.text)
    print("=====================")