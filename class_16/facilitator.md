# Serverless

This is a new topic. Lot of new talking points.

## Jokes
I asked my friend, “Hey, did you read that article about a social media platform that has some very toxic people, very questionable virtual communities, and people that come together to do amazing things?”

He replies: “Yeah, I Reddit.”


## Look at Lab for this class

As deployment practices evolve `Serverless` computing has emerged as an efficient (in terms of time and money) solution for many projects.

That is a very simple sentence but there is a lot to unpack there.

Deployment can be lots of things.

What was the old way?  
FTP - this was the way. Big companies did this.
Then came more complexity and more costs.

- When I was doing server deployments the average cost was close to 25,000.

Tons of distributed Servers - There is a lot of power with this but there is a lot of overhead.

The online service came in to simplify things: GitHub -> Heroku -> AWS -> Digital Ocean -> Vercel -> Netlify

What do you do when a service does not meet your requirements.  Think back to Kaggle. What version of python were they runnning?  3.7 something.  What if you needed some functionality from python 3.10.  Well, there is not much you can do there. You try your best with what they give you but ultimately they are the boss and you use what they give you, or you find another service to try.  (HINT: We will address this more in the second half of class with Docker, but for now this is what we will go with)

At some point you determine that you need more control.  There will be this balance between balance and convenience. You are always looking for that balance. You pay for this.

If you had a hello world app that you wanted to host somewhere public. Something that responds to http requests and presestents some info, returns a restful api.  This is not as simple as a GH deploymnet. You need to find somewhere that can host this, build the api.  Essentially you need to build yourself an entire webserver for hosting, you need to build your own house because the premades ones out there are just not cutting it.  All you need is to drop the welcome mat, but you need the house to host the mat.

Welcome to serverless. This is where we can have the house already provided, we can drop the welcome mat, but we have full control over what size, color, and image on the welcome mat.  We maintain the control we need.

Serverless is an entirely UNTRUE statment through. Great buzz word, had had a lot of success but it is a big lie. It is not truly serverless. There is a house. You just didn't have to think about the house, you don't have to think about the server or services. You don't care if it is Django or react, pyramid, express, flask. Whatever, you don't care.

Still need some sort of http request.  We are going to build that out and it can be a single function.

We are not going to pay someone to host our server, but we are going to pay someone to host our function. There is a big cost savings that will scale very well and we can even let it sleep and wait for connections.  IE spin up and spin down.  The lights are not always on but only when someone comes to our front door.  THis is when we are paying for compute time and traffic.

Let get ourselves a serverless function up and running. I am going to follow the example from Vercel this this demo.

## Create Project Skeleton

- > mkdir serverless
- > cd serverless
- > git init
- > mkdir api
- > touch api/date.py
- Follow the code from <https://vercel.com/docs/concepts/functions/supported-languages#python>.
- Type into `/api/date.py`
  - Explain each line of file.
- Add & commit changes.
- To push we need a Github repo.
  - Create EMPTY one at Github.
  - Make sure to skip adding README, etc steps.
  - Follow steps to push an existing repository from the command line.

## Vercel Dashboard

- Talk through process to Sign Up for Vercel Account at <https://vercel.com>
- Open browser at <https://vercel.com>
- Click `New Project` with GitHub as provider.
  - First timers will require an authorization step.
- In `Import Git Repository` click import button for `serverless`
  - Briefly mention how organization can be used, but it requires a paid plan.
- Leave default settings as is and click `Deploy` button.
- After a bit (30 seconds or so, usually) you'll see a success screen.
- Click `Go to Dashboard` button.
- Then the `Visit` button.
- At first you'll get a 404.
- But add `/api/date` to end of path and...
- Victory, the date shows!

## Add Another Function

- > touch api/howdy.py
- Follow the code from reference `api/hello_world.py` and add it line by line with explanations.
- If we want to see it work then ACP.
- Now browse to dashboard for `serverless` project and note that project is rebuilding.
  - E.g. <https://vercel.com/your-github-name/serverless>
- Once done rebuilding browse to site + `/api/howdy` and should get "howdy"

## Add a Function that (optionally) parses query string

- > touch api/aloha.py
- Follow the code from reference `api/aloha.py` and add it line by line with explanations.
- Even though ACP + rebuild goes really fast all things considered, it's still too slow when early in development. We need something that shows our current work in a few seconds at most.
- It is possible to run a simple Python server to host our functions, but that would be pretty differerent from how it will run when hosted by Vercel.
- Thankfully, Vercel has a CLI client.
  - <https://vercel.com/cli>
  - > npm install --global vercel
  - From root of project...
  - > vercel
  - Then follow prompts entering `y` when asked.
  - This will trigger a remote build.
  - But you can also preview on a local server.
  - > vercel dev
  - Browse to <http://localhost:3000/api/aloha?name=Guido>.
  - If you make local changes and things looks good then ACP which will trigger build.

## Add a function with Dependencies

- So far we've been using standard library, no external dependencies.
- But often that won't be the case.
- For our next function we're going to build a handy word definer that makes use of `Requests` library.
- First let's initialize the project the usual way:
- Follow Lab Submission steps.
- Then let's add `requests` library
  - > pip install requests
- Record the addition in requirements
  - > pip freeze > requirements.txt
- > touch api/define.py
  - Copy code from reference `/api/define.py` and add line by line with explanations.
  - Run locally to make sure everything works.
    - E.g. <http://localhost:3000/api/define?word=python>
  - ACP and bask in glory of several serverless functions deployed to the cloud.
