# Deployment

## Jokes

- What do you get when you cross a vampire with a snowman?  Frostbite.
- What is it like to be kissed by a vampire?  Pain in the neck
- WHy did vampire read newspaper?  Heard it had great circulation
- What do you cann 2 witches that live together.  Broom-mates
- How do you get rid of demons.  Exercise a lot.

## Warmup
# Given a list of objects, with an age property, and a target age, find the age that is closest in age to the target age
# Input:
# 	{age:47,...}, {age:23,...}, {age: 17}
# 	29
# Output: 23
# Feature Tasks
# Iterate through collection of objects finding the one with the closest age.
#
# Expected function with a return of the age

# Round 2 of warmup, instead of a list, they get a LL of objects.

```python
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

def find_age_list(people, target_age):
    closest_age_so_far = people[0]["age"]

    for peeps in people:
      candidate_age = peeps["age"]
      candidate_distance = abs(candidate_age - target_age)
      closest_distance_so_far = abs(closest_age_so_far - target_age)
      if candidate_distance < closest_distance_so_far:
        closest_age_so_far = candidate_age
    return closest_age_so_far


def find_age_ll(ll, target_age):
    current = ll.head
    closest_age_so_far = current.value["age"]

    while current:
      candidate_age = current.value["age"]
      candidate_distance = abs(candidate_age - target_age)
      closest_distance_so_far = abs(closest_age_so_far - target_age)
      if candidate_distance < closest_distance_so_far:
        closest_age_so_far= candidate_age
      current = current.next
    return closest_age_so_far

if __name__ == '__main__':
    folks = [{"age": 47}, {"age": 23}, {"age": 17}]
    age = 20
    print(f'The closest age to {age} is : {find_age_list(folks, age)}')

    node1 = Node({"age": 17})
    node2 = Node({"age": 23}, node1)
    node3 = Node({"age": 47}, node1)
    ll1 = LinkedList(node3)
    age = 99
    print(f'The closest age to {age} is : {find_age_ll(ll1, age)}')
```

## Review lab

- Review lab requirments
- Lecture demo is really quick. 
  - Today you will have some extra time to work on previous labs, DSA's etc.
- Why so light. There are a lot of you that are taking WB exams today.

## Deployment Steps


### Back End

#### Research

- Refer to [Next.js + Django Hello World](https://vercel.com/templates/python/django-hello-world)
  - Note that this approach is running with a `serverless` approach just like project earlier in course.
    - This makes it cheaper because we're not paying for a bunch of unneccessary uptime.
  - Note that the supplied directions there are insufficient.
  - It is necessary to inspect the linked repo to notice two key additions.
    - `vercel.json`
      - Note that project directory name must match.

```JSON
{
    "builds": [
      {
        "src": "project/wsgi.py",
        "use": "@vercel/python"
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "project/wsgi.py"
      }
    ]
  }
```

    - Updated `project/wsgi.py`
      - Add ```app = application``` to end of file in order to meet Vercel requirements.

#### Run Locally

- Step through conversion of demo from class 39.
  - Copy `class-39/demo/cookie-stand-api` folder into a local `repos` folder.
    - Create local git project with `git init`
    - Add and commit files.
  - Create GitHub Repo
  - Link local with remote
  - Push changes to GitHub.
- On Vercel Dashboard
  - Create new Project - Import GitHub project
  - Set env vars
    - NOTE: copy .env contents to clipboard and paste into dashboard
  ##### Deploy
  - It's not working, yet :(
  - Needs `app = application` in `project/wsgi.py`
  - Needs vercel.json with correct project folder name
  - ACP and view site once deployment complete.
    - Deployment is triggered by pushing to main on GitHub.
- We get a new error now...
- Disallowed host error
    - Edit ALLOWED_HOSTS variable in Vercel via `Settings: Environment Variables` panel.
      - NOTE: do not include trailing slash or scheme prefix.
        - aka only want something like `cookie-stand-api-python.vercel.app` to match site url.
      - Easiest for now is add `.vercel.app` which will handle all urls ending that way.
    - Trigger redeployment via `Deployments: (Current) ` and select `Redeploy from pop-up on right.
- Back end deployed!

### Front End

#### Research

One of the nice things about using Vercel is that it's the same folks that created Next.js so the integration is **really** smooth.

In fact, they promise **zero configuration**. Let's see about that.
#### First run locally

- Copy over `class-39/demo/cookie-stand-admin`
- Update `.env.local` with correct values. E.g.
    - NEXT_PUBLIC_API_URL=https://cookie-stand-api.vercel.app
    - NEXT_PUBLIC_RESOURCE_URL=https://cookie-stand-api.vercel.app/api/v1/cookie-stands/
- Confirm front end is running locally with remote api before moving on to next steps.
- Yep, that's zero configuration!

#### Deploy Front End

- Students should have Vercel accounts, with Github integration, from earlier in course.
- Create local git repo with `git init`
- Add and commit local files.
- Create GitHub Repo
- Link local and remote repositories.
- Push local changes.
- Create new Vercel project - Import newly created repo.
- Set env vars
- Once deployment done then give test run
- CREATE/READ/DELETE working? Yippee!

#### Final Checks

- Typically we run with DEBUG off in production.
- Update `Settings: Environment Variables: DEBUG` to `False`
- Trigger redeployment via `Deployments: (Current) ` and select `Redeploy from pop-up on right.
- Confirm in live site that navigating to missing page on API gets the minimal 404 messaging.
- Confirm that deployed front end still work with deployed API.
- Success! Or time to debug ;)