# Review Lab 39 

## Setup

```bash
npx create-next-app --example with-tailwindcss cookie-fetcher
```

- > Start By showing how an external component gets wired in.
- > Wire in CookieStandAdmin

```js
export default function Home() {

  return(
    <CookieStandAdmin />
  )
}
```

- > Create `cookie-fetcher/components/cookiestandadmin.js`.  In `cookiestandadmin.js`

```js
export default function CookieStandAdmin(){
    return(
        <h1>Logged into Cookie Stand Admin</h1>
    )
}
```

- > In `index.js` import `cookiestandadmin`

```js
import CookieStandAdmin from "../components/cookiestandadmin"
```

- > We can see that we have a file level component wired up and working.  

- > Create `cookie-fetcher/components/login.js`.  In `login.js`

```js
export default function Login(){
    return(
        <h2>Login</h2>
    )
}
```

- > In `index.js` import `cookiestandadmin`

```js
import CookieStandAdmin from "../components/cookiestandadmin"
import CookieStandAdmin from "../components/cookiestandadmin"

export default function Home() {

  return(
    <CookieStandAdmin />
    <Login />
 )
}
```

- > We should see both items on our page now.