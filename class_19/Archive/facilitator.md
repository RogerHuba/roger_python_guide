# Lecture NOTES: Automation

## Warm Up (10 Min)

> There are multiple warmups to pick from depending on the level of your class.
> Lambda Exercise
> Random error with random file

## Go over Previous Projects (20 Min)

## Whiteboard Challenge

- Depending on class schedule may or may not be doing a challenge.

## Review Lab for the Day (45 Min to 1 hour)

> Open up the 'potential-contacts' and sort through it.
> Look at a few numbers and emails.
> I want to talk about generating data.
> QUESTION: If I asked you to populate some content on a web page, what would you use to do that?
> ANSWER: Lipsum Generator of some sort.
> Makes perfect sense. Gives you a way to get data in a form that will mimic the real content.
> Bring up an ipsum. I like star wars. There is a bacon ipsum.  A Pirate ipsum. What is your fav?
> Today I want to reverse engineer this 'potential-contacts' file that is being provided for lab.

- Ask for some ways we could generate this file.

> I could use an ipsum generator to fill this document that I created to fill in some data.
> But there will be a few key pieces of information that are missing.  Phone numbers, emails.
> Once I got the bulk of the "junk" data I could probably find a site that will generate random emails and probably generate that will generate random phone numbers.
> I could also look for some iupsum with API's.
> Search hipster api
> There are other things I could do.  Maybe fire up beautiful soup, scrape some data off the internet.
> After going through a few ideas.  Lets talk about how what information is generated in this file.
> So you all know as developers, we are lazy (some prefer efficient). In any case we want to do things quicker, so we have more time for the things we want to do.
> I am going to use a library called Faker.  This will help to generate some data for us.

- Navigate to [Faker Documentation](https://faker.readthedocs.io/en/master/)

> We won't be using this for today's lab but this may come in handy for you later in the
> class for populating some data.

- Fake Name
- Fake Address
- Fake Text

> Point out that there is some integration with Pytest to generate some data.
> Lets generate some fake data.
> Will get a folder going and get a fake.py

```bash
poetry init -n
touch fake.py
poetry add faker
poetry shell

charm .
```

```python
from faker import Faker
# Faker requires us to select a language.
fake = Faker('en_US')
# We created an instance of Faker.  Lets print it and see what we get

```

> We got our self an object instance.
> What things are avaliable on this instance.  What are some things we can do to look at methods
> available to us?

```python
print(dir(fake))
```

> Scroll through some faker methods we have available to us.
> What are some things we see.  email. phone number. sentence. word words, paragraph.
> We can even simulate some credit cards and credit card providers and codes.

- Time to make a fake word.

```python
fake_word = fake.word()
print(fake_word)
```

> This gives us a single word which is just a string.
> We can copy this and make some fake words. With this we get a list of words.

```python
fake_words = fake.words()
print(fake_words)
```

> This gives us some data, but still not what I want. I still have to work to make this work for me. I want easier.  Lets take a look at the paragraph and paragraphs methods.

```python
fake_paragraph = fake.paragraph()
print(fake_paragraph)

fake_paragraphs = fake.paragraphs()
print(fake_paragraph)
```

> I have general 'filler' data, now I need to start filling in some other information.
> lets check some e-mails and some phone_numbers

```python
fake_email = fake.email()
print(fake_email)

fake_phone_number = fake.phone_number()
print(fake_phone_number)
```

> Generate a few items and talk about what the data looks like and what it need to end up looking.

- Full document time

> I think we are at a point where we can generate our own data file.
> I know I want to have a variable for the data. i can use an empty string.

```python
content = ''
```

> Ultimately I want to write this to a file. for now, just going to populate content.

```python
for _ in range(100):
```

> QUESTION: What is this loop doing?
> ANSWER going from 0 to 100
> Great. Now inside our loop, we can start adding some data.

```python
content = ''

for _ in range(100):
    content += fake.paragraph()
print(content)
```

> Great start.  I could do something like this:

```python
content = ''

for _ in range(100):
    content += fake.paragraph()
    content += fake.email()
    content += fake.address()
    content += fake.phone_number()
    content += fake.word()
print(content)
```

> As seen with the date right here, think through how difficult this may be to seperate out
> with regex. There are logs of things here that may be easier than others. Point out a few.
> The asset that you will be using for tomorrows lab, is not this difficult. In face we have
> spaced out the file for you already.
> Now that I have my content variable full of date. I need to save the date somewhere.

```python
with open('content.txt', 'w+') as f:
    f.write(content)
```

> Lets go BACK in TIME to mad libs.  Tell me what is going on in this line?
> We run it and BOOM.  We now have our content in a content.txt
> I created this notes file, but it dropped it right here in my fake folder.
> I don't want it here.  I want to add this to the assets folder that is off of the class 19 folder.  (Show where the folder is and what is there now.)
> We are going to something called. shutil. This is one of the standard libraries so there is no need to add it to poetry

```python
shutil.copy('content.txt', '../assets')
```

> Next bring up regex101.com
> Any PTSD from 301 code challenges?
> paste the data we made into the the test string

```regex
\d\d\d-\d\d\-\d\d\d\d
```

> Scroll through the data. I can see we targed some, but we missed others.
> I don't want to re-create the regex wheel. I don't have time to play around with regex and find the right combo.  Boss has me on a time limit to get this done.  In comes our google-fu. Find a reg-ex search that works. Remmeber to add where you found it to your notes.  And remember it may need to be tweaked a little still.
> Do a search for the longest regex email.
> I do not want you to do this.  I want you to balance efficiency vs time spent.
> Re-review lab
