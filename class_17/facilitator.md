# Web Scraping

- Let's scrape Code Fellows site to get a quick feel for what's covered in 401 Python Course.

> - **Big Note**: I checked with owners of the web site about scraping. That's not legally required (there was even a Supreme Court case about it!) but it's a best practice.

In this case I was steered toward the staging site vs. live one so our experemints didn't confuse their analytics.

```python
URL = "https://testing-www.codefellows.org/courses/code-400/"
```

- Go this this website and explain what we want to try and accomplish. We want to get to the course calendar
- Then look at all of the Python courses that are available.
- When we get to that point, copy the website to use.
- ```https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401```
- Yesterday we got a little experience with the requests library. We are going to use it again.
- It is a very popular library, but it does have some key limitations.
- We will address those limitations a little later today, but for now lets proceed.

## Create requests_parser.py
- touch scraper.py.py
- Get into Virtual Environment
  - pip install requests

Add the following code explaining along the way.

```python
# This will import the request library.
import requests

# Set a URL variable to the web address we want to use.
URL = 'https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401`

# The requests librry has a method called get. We will use that method to grab the URL.
# We also want to store that requiest into a variable.
req = request.get(URL)
```

- What did we do and does it work?  Well lets give it a little test.
- add `print(req) to the file and execute the script.

- We got something. It didn't blow up on us whcih is a great thing.
- This makes sense. We did a request, we got a response. 200 being a great code for us.
- What if we want to see some text? 
- add ```print(req.text)```
- Woah.  We see a nuch of text.  Where is this coming from?
- If we navigate over tou our page here and we inspect the source, we can see this is where it came from.
- We could have copied all of the info from the raw data and put it into a file. We could do that.
- There may be reasons to do that like to keep from pinging the server.
- Looking at all of this test can we tell where the information is in this data to find the python data we are
- looking for.
- It would be really awesome if there was a way to proccess this "markup" and get down to the details that we are looking for.
- Any ideas on how we might acomplish this? Any tools come to mind, like from our readings? BS?
- Lets install BS. It has been around for a while. Lets see if there are any gotcha's to look at.
- search for beatiful soup. Should end up on crummy.com/software/BeautifulSoup/bs4/doc
- Notice the great context of 90's style fonts, the 90's style side menu.
- Lets find the installer
- > NOTE: Be usre to point out that BeatifulSoup is not what is wanted, we want BeatifulSoup4.
- ```pip install beatifulsoup4```
- Lets see what we can do with beautiful soup?
- Lets install it
- ```from bs4 import BeautifulSoup```
- What you normall do, which comes from thier docs is create an instance and it is looking for some markup.
- Turns we have some markup already.
- change the print to assign a variable to req.text
- ```soup = BeautifulSoup(markup)```
- Go ahead and run the code. Look at the warning. It is looking for some parsing information.
- ```soup = BeautifulSoup(markup, 'html.parser')```
- ```print(soup)
- Great. We got the same mumbo jumbo that we had before. I thought this was suppose to be easier.
- It actually does. We can make it look a little nicer by runnign the .prettiyf() method.
- When we run that it does look a little nice. What we are seeing is that beautiful soup is undederstanding.
- We can change from .pretify() to find_all("h1").  Or we could run the first h1 we could run .find("h1").
- We could also look just at the text. .find("h1").text
- Go to the page and ask how we can look at the actual structire of the page. Looking to get to inspect.
- As we dig through all of the code we are looking for css selector .calendar-event.
- add ```courses = soup.select(".calendar-event")```
- We we can just through some python at it.
- ```for course in courses: -> print(course)
- See that it is hard to read.  Add the .prettify() method.
- As we scroll up and find the spacting se can see that everything looks to be in an article.
- But upon a deeper inspection we can see h1's and h2's. Lets update our code

```python
for course in courses:
    print(course.h1.text)
    print(course.h2.text)
```

- Now we see somehting that we are trying to get to.
- Course titles, and even some dates.
- Point out that on the web page we dont see ops and 201, 301.  The info is there but probably hidden.
  - This is something to take into account that there may be info you can't see on the site, but the text is there.
- We are making some assumptions here but we have to. We did not create this code, we didn't write the site.
- Assumptions will have to be made often.
- Make Code look like this:

```python
for course in courses:
    if "Python" in course.h1.text:
        print(course.h1.text)
        print(course.h2.text)
```

- Didn't take a whole buch of work. Not a ton of code.
- But it did take some digging around in the code to figure out some things.
- We want to take this to the next level. We want to be able to automate the selection of python on the page.
  
## Playright

 - Navigate to https://playwright.dev/python/
 - We would like to automate the proccess of doing the think we did with beautiful sooup with with more functionality.
 - This tool is owned by Microsoft but it is open source.  Written in multiple languages but Python is one of the main.
 - Click get started
 - Go through the proccess of getting started
 - Primary use case is for testing websites. Test it in ways that humans would do.
 - Turns out the way that it tests in ways thatare similar to what we are looking for today by doing some scraping. 
 - Using testing as scraping.
 - Run a ```pip install pytest-playwright```
 - Might want to do a pip freeze as well.
 - Then it says to install browsers.
 - We will be installing a headless browser.
 - It will be more funning behind the scenes.
 - run playwright install -h
 - We can identify the specific browser to save some downloading time.
 - playright install chromium is what I am going to use.
 - There are some test examples here. No tests are required for today but this might come in handy in the future.
 - There is this thing called a sync_api I am going to grab that.