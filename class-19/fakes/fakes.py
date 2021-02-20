# Open the Lab and review todays lab
# Our goal today is to make the garbage text that our "disgruntal" employee left behind
# We are going to need some junk or random text.
    # We could use something pirate ipsum or star wars ipsum to generate some junk data
    # would do this by generating data and copy paste the data.
    # Could generate a page ans scrape the data.  We know how to do that.
    # Some "ipsum's" have api.  hipster has this
    # But I am lazy. Like super lazy.  SO I want to use a tool that already exists
    # I am going to use something called faker.
    # go to https://faker.readthedocs.io/en/stable/

    # not as cute as pirates or as cool as starwars ipsum
    # But it gives us things like address, and maybe a few other things

    # lets take a look at how it works

    # TODO: 'SET TASK need to generate some ipsum and save to a file'
    # TODO: 'Need to have emails and phone numebrs sprinkled in'

from faker import Faker

fake = Faker('en_US')

print(fake)

# When we run this we get an object which validates we are getting something.
# I happen to know one that we can use
print(fake.name())
# What if we want to look at all of the methods available to us to use?
# print(dir(fake))

# Now we can do something like the following:

print(fake.words())

print(fake.text())

print(fake.paragraph())

# lets try an email

print(fake.email())

# How about a phone number
print(fake.phone_number())

# Lets see if we can generate some content

content = ''

# When you are using something where you don't necessarily need a var _ is the contention
for _ in range(100):
    content += fake.paragraph()
    content += fake.email()
    content += fake.paragraph()
    content += fake.phone_number()
    content += fake.paragraph()

content += '\n'

print(content)
print()
# now I want to write this to a file
# Check with students to see if they remember how to open (or create) a file

with open('notes.txt', 'w+') as f:
    f.write(content)

# What if I wanted to save this elsewhere, or better yet copy it?
# from your reading you may remember this nice utility called shutil.  Lets import that
import shutil

# Check that notes is not in the asset folder.  delete the existing file

# push to asset folder in class19
shutil.copy('notes.txt', '../')

# Talk about the lab again
# Talk about how to find a phone number
# Mention regex
# go to regex101.com

# start by looking for numbers (3) in a row
# add in the \d\d\d-\d\d\d\d
# There are lots of help options on the site, but lets think
# if we were on the job do we have the time to spend figuring this out?  NO
# Lets run through some google.
# http://phoneregex.com/

