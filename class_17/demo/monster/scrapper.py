# Review Lab For the Day

# Go to a random website of something that you may want to search for.
# https://www.starwars.com/databank
# Talk about trying to gather information
# Talk about the legality of scraping a website
# This is a good project for your mid-term or even for the final project.

import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=software-engineer-&where=seattle&intcid=skr_navigation_nhpso_searchMain'
response = requests.get(URL)
# print(dir(response))
content = response.content

soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())


result = soup.find(id='SearchResults')


# print(result.prettify())

job_result = result.find_all('section', class_='card-content')
# print('\n**************************'*10)

# print(len(class_result))
# print(job_result[8])
# title8 = job_result[8].find('h2', class_='title').text.strip()
# location8 = job_result[8].find('div', class_='location').text.strip()
# company8 = job_result[8].find('div', class_='company').text.strip()

# print(title8)
# print(location8)
# print(company8)

final_results = []

for jobs in job_result:
    jobs_dict = {}
    if jobs.find('h2', class_='title'):
        title = jobs.find('h2', class_='title').text.strip()
        jobs_dict['title'] = title
        location = jobs.find('div', class_='location').text.strip()
        jobs_dict['location'] = location
        company = jobs.find('div', class_='company').text.strip()
        jobs_dict['company'] = company
        print(f'There is a position as a {title} wtih {company} is avaliable in {location}.')
        final_results.append(jobs_dict)

print(final_results)

