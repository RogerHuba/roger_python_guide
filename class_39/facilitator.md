# Cookie Stand Connect Front End to Back End Demo
- Be sure that there are 3 versions uploaded to the class repo. 
  - Admin Demo (Working)
  - API Demo (Working)
  - Admin Starter

## Review Lab Requirements
- In Canvas go over the upcomming Lab for the day

## Cookie Stand API Container
- In the api folder, start up the dgango application.
  - Ensure the .env.sample is copied to a .env file
  - depending on what is in the database may need to:
    - ```docker compose run web python manage.py makemigrations```
    - ```docker compose run web python manage.py migrate```
    - ```docker compose run web python manage.py createsuperuser```
      - admin:admin for ease of use
  - ```docker compose up```
  - navigate to localhost:8000 or 0.0.0.0:8000
  - Check that you can see routes at / route

## Cookie Stand Admin Page
- Open a new terminal windows (Don't close API)
- Navigate to Cookie Stand Admin Page
- run ```npm run dev`` and see that it starts or check for errors
  - Delete the node_modules folder, run npm i fixes most issues.
  - Default demo should be working, if not troubleshoot.
- At the main page of the Cookie Stand Admin, login.
  - If nothing there, add some values.
    - Need to add:
      - Location Name
      - Minimum
      - Maximum
      - Average
      - Press Create button.
  - Add a 2nd, and and maybe a third
  - Delete one of the entries to see that it works.
NOTE: Be sure to point out the lack of styling here.
This is for them to figure out in lab.

## Cooie Stand Starter Page
- Shutdown the running Cookie Stand Admin in terminal.
- Navigate to the the Cookie Stand Starter Page.
- If node_module folders exists, delete.
- run ```npm i```
- ```npm run dev```
NOTE:  This Page will have 1 line of Data already.

## Update the Page Demo
- Now that we have a starting place, lets see what needs changing
- This is not what we want (based off the working demo we saw)
  - No login
  - Delete not working
  - Create not working
    - Think about why create is not working right now.
    - In Django's model, what were some of the required fields?
      - That's right, the usermodel to set the owner. 
  - Data showing without being logged in.
- The information with out being logged in, let's resolve that issue first.
- Navigate to pages->index.js
  - We can see right now we are rendinering the <CookieStandAdmin />
  - This is not what we want as our default behavior.
  - We want some conditions.  We want to show this if we have a user loged in, if not show the login page.
- Update this:

```JavaScript
<CookieStandAdmin />
```

to this:

```JavaScript
// If we have a user then show CookieStandAdmin
{user ?
<CookieStandAdmin />
: // Otherwise we show this.
<h2>Login Form Comming Soon</h2>
}
```

- Based on this it will not work just yet.  Why not?
- user has not been defined in our ternary expression.
- Show the Web Page
- Lets make one really quick for the purposes of testing:

Add this above the return

```JavaScript
const user = null;
```

- What I expect to happen here is because user is null, or falsy, we should render the Login Form Comming Soon.
- Now looking at our page, that is exaclty what we get.
- Lets change that to something truthy and see if something else renders.

```JavaScript
const user = true;
```

- Now we see our CookieStandAdmin data.
- Great. Our handling of the admin data is working, but not entirely like we want. We want to be actually able to login.
- We are going to save a little time here and grab the code from the "finished" demo that is in the class repo.

Add the following to the bottom of index.js

```JavaScript
function LoginForm({ onLogin }) {

    async function handleSubmit(event) {
        event.preventDefault();
        onLogin(event.target.username.value, event.target.password.value);
    }

    return (
        <form onSubmit={handleSubmit}>
            <fieldset autoComplete='off'>
                <legend>Log In</legend>
                <label htmlFor="username">Username</label>
                <input name="username" />
                <label htmlFor="password">Password</label>
                <input type="password" name="password" />
                <button>Log In</button>
            </fieldset>
        </form>
    );
}
```

- Lets walk through this code. If we just focus on this, it is small enough that we should be able to understand everything here.
- The onLogin here is called using object destructuring. 
- This is a concept that can make code more readable and clear, especially when passing down props.
- Imagine we have a movie object

```JavaScript
  const movie = {
    name: "Star Wars",
    year: 1978,
    director: "George Lucas
  };
```

-   Before destructuring, you would need to access each property individually
    -   movie.name
    -   movie.year
    -   movie.director


- Destructing lets us streamline the code

```Java Script
const { name, year, director } = movie;
```

- is the same as

```JavaScript
const name = movie.firstName
const year = movie.year
const city = movie.director
```

```JavaScript
// Object Destructuring
const movie = {
    name: "Star Wars",
    year: 1978,
    director: "George Lucas"
};

console.log(movie.name);
console.log(movie.year);
console.log(movie.director);

const { name, year, director } = movie;

console.log(name);
console.log(year);
console.log(director);
```

- This lets us access the properties without the 'movie'
- That is a general overview, there is a little more to that.  
- If you want more info, add that to your lookup list.
- We see that the function starts with a capital letter, indicating that this is a component. This is a React rule, not a JavaScript rule.

- Next we look at the handleSumbit(event)
- We have our prevent default to prevent the page from reloading itself.
- It is going to call the passed in onLogin and we are going to pass values by position. 
- We're going to pass it in the username fields value, and the password fields value.
- So onLogin is not an event handler in the same sense, it's a function that just get gets called, and then expects a username and a password.
- All of the form submission event stuff happens inside of this component.

- Then we see the jsx here. It has a single top level return in <form>. This is html here. Nothing that needs explaining.
- Let's head back up and get this to render.
- In the default return, in place of:

```html
<h2>Login Form Comming Soon</h2>
```

- Replace it with:

```JavaScript
<LoginForm onLogin={loginHandler} />
```

Now we need a function to handle the loginHandler:

```JavaScript
function loginHandler(username, password) {
    alert(username);
}
```

- We head to the page and try to login and see if it is wired up correctly.  There is out alert.
- No login, need to update our user to null.  Try again.
- Success. Now we want to wire this up to something that has "real" information.
- Where is our "real" information?
  - Django API, the backend of this application.
- Time to login there. We are not creating a user, or sign up, just verifying that a user is valid (username, passoword) from Django.
- We are going to introduce some front-end authentication into our application. We will do this via "Context", something that was in your reading last tuesday.
- Context is a way of providing data and functionality across components.
- To get this started we need to create a few things.
  - A folder called contents
  - a file called auth.js
- What will auth.js's main responsibility.
- The main thing it will do is define a hook.
- This hook will allow us to, in the same way we used State as a hook, it is going to allow us to do auth stuff in a hook.
- If anyone asks about what is a hook:

```text
In React, a hook is a special function that allows you to use state and other React features in function components. Hooks were introduced as a way to provide stateful logic to function components, which previously could only be achieved with class components.

React provides several built-in hooks that can be used to manage state, handle side effects, and control the rendering of your components. Some of the most commonly used hooks include:

useState - Allows you to manage state in a functional component.
useEffect - Allows you to perform side effects, such as fetching data or updating the DOM, in response to changes in state or props.
useContext - Allows you to access context data from a parent component in a functional component.
useRef - Allows you to create a mutable reference that persists across component renders.
useCallback - Allows you to memoize a function so that it only changes when its dependencies change.
Hooks are an essential part of modern React development and can greatly simplify the management of complex state and logic in your components.
```

- As a convention, hooks always start with 'use'. So are going to create a useAuth hook. 
- We also want to make this so that other parts of our application have access to this hook. 
- We will do this through something called an authProvider.
- So we're going to need to define some stuff, create a context, we're going to need to to interact with that context in our useAuth hook, and we're going to need to provide it. 
- So there is a lot going on here.
- I'm going to start typing. 
- Today, you are going to be using this hook, you won't need to create it from scratch, just use it. 
- This is not a shortcut. 
- It is to prepare you for what you will be doing on the job. 
- You will often be taked to use something that you did not create. 
- You just need to know how to integrate it.

We are going to start with some imports. 2 hooks (they start with use, and another function.)

```JavaScript
import { createContext, useContext, useState } from 'react';
```

- Because our api is using json web tokens, we need 

```JavaScript
import jwt from 'jsonwebtoken';
```

- Right now, it does not exist. Run:
- ```npm in jsonwebtoken``` in terminal
- We need this because this is how we communicate with our API to authenticate.
- We are going to need to know, where is, or what is the URL that we are talking to.  Add:

```JavaScript
const baseUrl = process.env.NEXT_PUBLIC_API_URL;
```

- We are not hard coding the url, we are going to set it up in a .env to protect it. Notice the naming contvention "NEXT_PUBLIC". 
- This is a NextJS thing that will allow you to use a .env without any additonal installs. (remember back to djangoenviron). 
- This will grab it out of your environment. 
- At the top level we are going to create a .env.local. We have a sample sitting here for us to use. 
- I am just going to rename it.

- Next we need to create context, we are going to all it AuthContext. Add:

```JavaScript
const AuthContext = createContext();
```

- You will see how we interact with this in just a moment.
- Next we need to define a hook via a functiont hat will be made avaliable outside of this module. So it will need to be exported. Add:

```JavaScript
export function useAuth() {
    const auth = useContext(AuthContext);
    if (!auth) {
        throw new Error('You forgot AuthProvider!');
    }
    return auth;
}
```

- This makes a local variable inside the function, called auth, which is the return value of calling useContext imported on line 1, and passing in that authContext.
- There is a lot going on behind the scenes, but essentialy this is some of the plumbing that is required to be able to use this AuthHook across our application. 
- It gives us a warning if we forget the auth provider.
- The next thing to add, has a LOT going on it it. We are going to create an new export. Add:

```JavaScript
export function AuthProvider(props) {

}
```

- The long story short here is this is going to return us a provider. 
- Remember when I said that you do not need to know the ins and outs of this, just how to implement it. 
- This is one of those cases. Add this into the function. Lets bring this in a little at a time. Add:

```JavaScript
    const [state, setState] = useState({
        tokens: null,
        user: null,
        login,
        logout,
    });
```

- The first thing it does is the provider is going to keep track of state using the useState hook to keep track of things. 
- It will pay attention to who the current user is, but it will also pay attention to tokens, wich is import because we want to get tokens back. 
- If you remember back to JWT in Django, we created the token pair that we accessed from the API, this will allow us to maintain the tokens in state, as well as the ability to login and logout.
- Notice the syntax of login, logout inside the object. Does anyone know what this means. Ultimately it means the key:value is the same name, so this is the same as ```login:login, logout:logout```. 
- Like pythonistas, JS devs love removing and simplifying code as much as possible.
- Now it is time to handle the login. Add (inside AuthProvider):

```JavaScript
async function login(username, password) {

        // const response = await axios.post(tokenUrl, { username, password });

        const options = {
            method: "POST",
            body: JSON.stringify({username, password}),
            headers: {'Content-Type': 'application/json'},
        };

        const response = await fetch(tokenUrl, options);

        const data = await response.json();

        const decodedAccess = jwt.decode(data.access);

        const newState = {
            tokens: data,
            user: {
                username: decodedAccess.username,
                email: decodedAccess.email,
                id: decodedAccess.user_id
            },
        };

        setState(prevState => ({ ...prevState, ...newState }));
    }
```

- This takes in a user name and a password that does some things. 
- Particularly it calls out to a url ```see await fetch(tokenUrl, options)```. 
- What is a tokenUrl, well it should be a combination of the baseurl, and the remaining portion of the path that gets you to the token.
- Where do we get this token? If we remember back to Django, we get this from localhost:8000/api/token. We are not specifying that anywhere here in our auth.js.  
- Lets add that in. Add:

```JavaScript
const tokenUrl = baseUrl + '/api/token/';
```

- The breakdown after this is: We fetch some data, get a json response, decode the data to break it down into an object, which we create a newState and update the state of our app. 
- If you want to dig into this one a little more, feel free but that gives you the overview of the rest of login.
- Logout is a little simpler. 
- We set user and tokens to null, then update State. Add: 

```JavaScript
    function logout() {
        const newState = {
            tokens: null,
            user: null,
        };
        setState(prevState => ({ ...prevState, ...newState }));
    }
```

- You could be a little more sopfistacted and force a logout on the back end, but for our purposes by removing the user and tokens from state, we force the logout.
- We are alomst done here. 
- Tiny bit left. 
- The authprovider is suppose to return a provider. Right now that is not doing that. Let's fix that. 
- Add:

```JavaScript
    return (
        <AuthContext.Provider value={state}>
            {props.children}
        </AuthContext.Provider>
    );
```

- This means that Auth context provider is going to wrap around
some other components. 
Those other components are called the children, and so anything else gets thrown in there, gets wraped. 
If I've got some children, then i'll refer to that with props.children. 

- This should be done now. 
- BUT we can't test it yet and we can't use it yet. 
- We need to head over to our pages folder and look at **```_app.js```**. 
- This is where all our components live that can be extended within your app. 
- We want every component to have the ability to deal with Auth.
-  We do that by importing the provider, and wraping that provider around the <Component />
- First we import AuthProvider.  
- Add:

```JavaScript
import { AuthProvider } from '../contexts/auth';
```

- Now I want to wrap component with AuthProvider. Add:

```JavaScript
export default function App({
    Component,
    pageProps
}) {
    return (
        <AuthProvider>
            <Component {...pageProps} />
        </AuthProvider>
    );
}
```

- That finished the plumbing. 
- Now how do we use it? 
- Well you use it where you want to use it. 
- We want to use it back where we originally hardcoded our user and now have it tie into our authentication system.
- Head back to **```index.js```**
- First we need to import useAuth.  Add:

```JavaScript
import { useAuth } from '../contexts/auth';
```

- Then we need to use it. 
- We want our user and the ability to login. Add:

```JavaScript
// Replace this
//   const user = null;
// with
    const { user, login } = useAuth();
```

- We also had this alert to show we were logged in. 
- We can get rid of that. 
- Then we just have to update our loginHandler to what we want to use, which is login. 
- Then down in the cookie standform add:

```JavaScript
    const { user } = useAuth();
```

- We login and we are now looking at our "hardcoded" cookie stand. 
- Login works, handling of our data does now. 
- We are going to add in another hook, a useResrouce hook. 
- I am going to quickly update the code with the use resource "stuff". 
- My page is going to break while I update this.
- Import useResoruce (Needs to be created) Add:

```JavaScript
import useResource from '../hooks/useResource';
```

- This does not exist so I need to create that. 
- Add **``` hooks folder```** and **```useResource.js file```**. 
- There is a lot to this file. Add:

```JavaScript
import useSWR from 'swr';

export const apiUrl = process.env.NEXT_PUBLIC_RESOURCE_URL;
import { useAuth } from '../contexts/auth';

export default function useResource() {

    const { tokens, logout } = useAuth();

    const { data, error, mutate } = useSWR([apiUrl, tokens], fetchResource);

    async function fetchResource(url) {

        if (!tokens) {
            return;
        }

        try {
            const response = await fetch(apiUrl, config());

            const responseJSON = await response.json();

            return responseJSON;

        } catch (err) {
            handleError(err);
        }
    }

    async function createResource(info) {

        try {
            const options = config();
            options.method = "POST",
            options.body = JSON.stringify(info);
            await fetch(apiUrl, options);
            mutate(); // mutate causes complete collection to be refetched
        } catch (err) {
            handleError(err);
        }
    }

    async function deleteResource(id) {

        try {
            const url = apiUrl + id;
            const options = config();
            options.method = "DELETE";
            await fetch(url, options);
            mutate(); // mutate causes complete collection to be refetched
        } catch (err) {
            handleError(err);
        }
    }

    async function updateResource(resource) {
        // STRETCH
        // Add ability for user to update an existing resource
    }


    // helper function to handle getting Authorization headers EXACTLY right
    function config() {

        return {
            headers: {
                'Authorization': 'Bearer ' + tokens.access,
                'Content-Type': 'application/json',
            }
        };
    }

    function handleError(err) {
        console.error(err);
        // currently just log out on error
        // but a common error will be short lived token expiring
        // STRETCH: refresh the access token when it has expired
        logout();
    }

    return {
        resources: data,
        error,
        loading: tokens && !error && !data,
        createResource,
        deleteResource,
        updateResource,
    };
}

/* STRETCH
This approach works, but it's not very snappy for the user.
Check the SWR docs to see if you can "optomistically" render updated state while the API response is pending.
*/
```

- In this file there is a dependency for swr. 
- We will need to add that with ```npm i swr```

- Then we are going to replace our CookieStandAdmin().  Replace:

```JavaScript
function CookieStandAdmin() {

    const { resources, deleteResource } = useResource();

    return (
        <>
            <CookieStandForm />
            <CookieStandTable stands={resources || []} deleteStand={deleteResource} />
        </>
    );
}
```

- After that add in CookieStandForm Add:

```JavaScript
const { createResource } = useResource();
```

- add after console.log ```createResource(info)```
- Should be able to run the page and do the things.
