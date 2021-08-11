import requests
from bs4 import BeautifulSoup

URL = "https://testing-www.codefellows.org/courses/code-400/"
page = requests.get(URL)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

results = soup.find(class_='course-details')

print(results.__dir__(self))