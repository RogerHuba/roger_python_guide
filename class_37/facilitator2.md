# Class 37 React - NextJS - Tailwind

## Jokes

- What did the parent Math Problem say to the child math problem?
  - grow up and solve your own problems."
  
- "Why can't you hear a psychiatrist using the bathroom? Because the 'P' is silent."

## Whiteboarding

 > We are getting really close to students whiteboard interview.  Is a good time to have a student whiteboard in front of everyone.  Use the codefellows generator.
 [Random Question Generator](https://codefellows.github.io/dsa-practice/)

## Demo: React, Next.js & Tailwind

There is a LOT of new syntax today. While there are less than 100 lines of code it is full of JSX, ES6 and Tailwind classes.

Plan on explaining each step as you go.

## Tease Project

- [Pending State](pending.jpg)
- [Asked State](asked.jpg)

## Create Project

- [Next + Tailwind Template](https://github.com/vercel/next.js/tree/canary/examples/with-tailwindcss)
- > npx create-next-app magic-eight-ball
- > Follow this [tailwindcss](https://tailwindcss.com/docs/guides/nextjs)
- > NOTE: Make sure students are up to date with NPX
- > This may take a min or 2 depending on internet speed and computer proccessing.
- > cd magic-eight-ball
- > code .
- > Point out the .Next dir and node_modules.  Need .gitignore
- > npm run dev
- Walk around the example a bit

## Customize Project

- With Django all we did was add some things, for Nextjs there are a few things we will add as we go through, but there are also a few things we need to remove that we will not need.
- Strip out the code/files we won't be using
  - `pages/api` folder
  - `public/vercel.svg`
  - Remove most of code inside `pages/index.js`
    - Keep outmost div, `<Head>` and empty `<main>` with blank className attributes.
    - Update `<Head>` title

```javascript
import Head from 'next/head'

export default function Home() {
    return (
        <div className="">
            <Head>
                <title>Expert Eight Ball</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="">
            </main>
        </div>
    )
}
```

## Match the Spec

Take a look at screenshot/spec and work (roughly) from top to bottom, hitting footer sooner.

### Header

```javascript
<header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
    <h1 className="text-4xl">Magic 8 Ball</h1>
    <p>1 questions answered</p>
</header>
```

Discuss use of Tailwind. The syntax is new but it maps directly to CSS concepts they should be familiar with.
[tailwind](https://tailwindcss.com/)

### Footer

Let's jump to Footer next

```javascript
<footer className="p-4 mt-8 bg-gray-500 text-gray-50 ">
    <nav>
        {/* will build out careers page soon */}
        <a href="careers">Careers</a>
    </nav>
</footer>
```

- Note the funny comment syntax
- Click on Careers link, should go to 404 page

### Question Form

Just doing the visuals for now, will take another pass and wire it up later.

Inside `<main>` add the form

```javascript
{/* Question Form */}
<form className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
  <input name="question" className="flex-auto pl-1" />
  <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
</form>
```

### Eight Ball

Now let's create the graphics for 8 ball, we'll add interactivity soon.
Add below the form

```javascript
{/* Eight Ball */}
<div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
    <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
        <p className="text-xl text-center">Ask me anything</p>
    </div>
</div>
```

### Question Form Input

Now let's wire up the form.

There are a couple ways to do this, the "react" way and the "controlled" way.

Most of the time we'll go the "react" way, but for small cases it is acceptable to do it the older fashioned way for now.

Create a "handler" function that is triggered when form is submitted.

It should be placed **inside** the Home function body, normally at the top.

```javascript
export default function Home() {

    function questionAskedHandler(event) {
        event.preventDefault();
        alert(event.target.question.value);
    }
    ...
```

Add a reference to the function on the form element in the HTML

``` javascript
<form onSubmit={questionAskedHandler} ...
```

Note the curly braces instead of quotation marks.

Type some text into form then click Ask button.

So now we've got the ability to capture user input. But we need to do something with it.

Note: make sure `data.js` is handy.

You can find it in built out demo.

The file should be in root of project.

## Generate a reply

- > Add to index.js at top
- import { replies } from '../data'

- Next update `questionAskedHandler`

```javascript
function questionAskedHandler(event) {
    event.preventDefault();

    // get a random reply from data
    const randomReply = replies[Math.floor(Math.random() * replies.length)];

    alert(randomReply);
}
```

Click on `Ask` button a few times, marvel at the random responses.

But it's no fun just to alert the reply, let's get it to show in the 8 ball!

## State

In order to do that the React way we need to think about `state`

- State is a plain JavaScript object used by React to represent information about the component's current situation. It's managed in the component.

We want the `state` of our app to include the generated response after a question is asked. The concept of `state` is extremely important in React and it needs to be handled in a particular way.

There are actually 2 supported ways of doing this. The older (but still supported) is to use classes. The newer (and recommended) way is to use a `hook`

- > Add to index.js

```javascript
import { useState } from 'react'
```

At top of `Home` before other functions add a line to work with `useState` hook.

```javascript
const [reply, setReply] = useState('Ask me anything');
```

The `useState` takes in an optional argument which represents the initial value.

It returns an array. The first item in array is the current value, the second is a function to update the value.

Now change `questionAskedHandler` to update state instead of doing an alert.

```javascript
setReply(randomReply);
```

We're almost there, now we need to remove the hard coded "Ask me anything" from the 8 Ball.

Update the inner `<p>` tag to use `{reply}` Inside the form.

```javascript
<p className="text-xl text-center">{reply}</p>
```

Now, whenever `reply` is changed (via setReply function) then every place that renders `reply` will update as well.

Run the app and click `Ask` button a few times. See how 8 Ball updates without us needing to explicitly tell it to?

In React, components will re-render whenever it's dependent state changes.

## Stepping Back / Requirements

We're making progress. Let's see how things stand.

See the hard coded `1 questions answered` in upper right?

That's not gonna work. It should start at zero then increment as questions are answered.

In other words, the number of questions answered should be part of our app's `state`

So let's step back and think about our app's state.

Currently we keep track of the latest reply, which works ok for rendering the 8 Ball.

But it works less well for tracking the number of questions answered. And it won't work at all for the table at bottom which tracks the complete history of questions and replies.

## Track Answered Questions

So how about instead of tracking a single reply, we keep track of a list of `answered questions`

Replace

```javascript
const [reply, setReply] = useState('Ask me anything');
```

with

```javascript
const [answeredQuestions, setAnsweredQuestions] = useState([]);
// It says “from the returned array store first item in local variable named question, and store the second item in variable named setQuestion reply is the current value, setReply is a function to call when updating the value.that way React can efficiently know when a re-render may be needed.
```

Now were storing a more complete data set in `state`.

Notice that we are now passing in an empty array as initial value.

Modify `questionAskedHandler` to construct an Object representing the answered question, and update state with it.

```javascript
function questionAskedHandler(event) {
    event.preventDefault();

    // get a random reply from data
    const randomReply = replies[Math.floor(Math.random() * replies.length)];

    const answeredQuestion = {
        question: event.target.question.value,
        reply: randomReply,
        id: answeredQuestions.length,
    }

    console.log('answeredQuestion', answeredQuestion);

    setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
}
```

Note: we're adding an `id` property as well. This will help us when rendering Table as well as be a better simulation of data coming from an API, hint hint.

Also note the way `setAnsweredQuestions` requires a **new** array. So we used the `spread` operator to grab all the existing items, then added the new one at the end.

Now create a `getReply` function that will get the latest reply in a safe way.

```javascript
function getLatestReply() {

    if (answeredQuestions.length === 0) {
        return 'Ask me anything';
    }

    return answeredQuestions[answeredQuestions.length - 1].reply;

    // or fancy one liner
    // answeredQuestions[answeredQuestions.length - 1]?.reply || 'Ask me anything'
}
```

Almost there. Now we need to modify the 8 Ball Component to use `getLatestReply` function instead of just `reply`

Update innermost `<p>` tag

```javascript
<p className="text-xl text-center">{getLatestReply()}</p>
```

Run the app and make sure still works.

## Questions Answered Count

It does? Great! Let's get back to the `X questions answered` feature.

Currently it always says 1. Armed with our new app state how could we remove that hard coding?

Update header component's `<p>` tag

```javascript
<p>{answeredQuestions.length} questions answered</p>
```

See what's different? The hard coded 1 has been changed to be whatever is the length of `answeredQuestions`

That's exactly what we want, and React will take care of re-rendering the header whenever that value changes.

## Report Table Component

This approach will really payoff when we add the `Report Table`

In order to make this dynamic we need one small, but fundamental, change to the table's `<tbody>`.

```javascript
<tbody>
    {/* Before - hard coded
    <tr>
        <td className="pl-2 border border-gray-700">1</td>
        <td className="pl-2 border border-gray-700">Is Falcon and the Winter Soldier worth watching?</td>
        <td className="pl-2 border border-gray-700">Yes.</td>
    </tr>
    */}

    {/* Now - dynamic */}
    {answeredQuestions.map(item => {
        return (<tr>
            <td className="pl-2 border border-gray-700">{item.id + 1}</td>
            <td className="pl-2 border border-gray-700">{item.question}</td>
            <td className="pl-2 border border-gray-700">{item.reply}</td>
        </tr>);
    })}
</tbody>
```

## Components

Lets do one as an example.  Lets update the header.

create folder called components.
add a header.js

in Header.js

```react
export default function Header(props) {
    return (
        <header className = "flex items-center justify-between p-4 bg-gray-500 text-gray-50">
        <h1 className="text-4xl">Magic 8 Ball</h1>
        <p>{answeredQuestions.length} questions answered</p>
      </header>
    )
}
```

in index.js

```html
import Header from '../components/Header';


<Header count={answeredQuestions.length} />
```

## Recap

Phew, we're done!

Ask some questions, get some magical answers. This React app totally works.

Granted, it's not quite 100% the `React` way. Don't worry about that yet though, making it that way won't take too much work and your code will be easier to read, maintain and reuse. But that's for next class.

For now, have fun and make a mess!
