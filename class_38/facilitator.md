# Lecture NOTES: React II

## Jokes

- Why did the orange stop? It ran out of Juice
- What happens to grapes when you step on them?  They wine.
- A cheese factory exploded in France. Da brie is everywhere!
- A friend of mine doesn’t pay his exorcist. He got repossessed.
- I begin to read a horror novel in Braille. Something bad is about to happen, I can feel it.

## Career Coaching

- Next Sat is your final career coaching. This is your 5-7 min pitch. There are a couple of prep assignments to take note of before Sat. There is not a lecture on Sat because the presentations take up most of the day. When we do finish with Presentations there will a small "something" to do.
- The weeks after on code-challenge night there will be intervie challenges. I have them hidden right now but will publish them every monday / thursday.

## Mock Interviews

- [Geeks for Geeks Question](https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/)

```text
Given an list of linked-lists with values of single, positive integers, create a function to traverse the list and convert the list to a number, add the lists together and return the total value of all lists.

The lists will be passed as parameters.

ll1: [5]->[9]->[9] = 599
ll2: [2]->[1]->[1] = 211
ll3: [1]->[4]->[1] = 141

Should return 951
```

```python
def add_ll(lists):
    if len(lists) == 0:
        return 0
    total_sum = 0
    
    for ll in lists:
        list_number = ''
        current = ll.head
        while current:
            list_number += str(current.value)
            current = current.next
        total_sum += int(list_number)
    return total_sum
```

### Code Challenge 38 Review

```python
def depth_first_search(self, vertex):
    if vertex not in self.get_nodes():
        return []
    result, stack, visited = [], Stack(), set()
    stack.push(vertex)
    while stack:
        top = stack.peek()
        if top not in visited:
            result.append(top.value)
        visited.add(top)
        has_unvisited = False
        children = [edge.vertex for edge in self.get_neighbors(top)]
        for child in children:
            if child not in visited:
                has_unvisited = True
                stack.push(child)
                break
        if not has_unvisited:
            stack.pop()
    return result
```

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
export default function Footer() {
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


















### React State and Props

> During our last class we had a slightly used State.  Today we are going to bring in props. There may be some shudders out there as you remember what a pain props was.  Lets do a quick refresher for some of you and a little teaching for others.

- State and Props are ways that we pass data in React.
- Lets look at state first.
- State is an instance of a React componet class. (IE the state object is where your store property values that belong to the componet)
- When the state of a component changes, the component will automatically re-render and update the DOM if there are any layer or visual changes. If there are no changes, the DOM will NOT be re-rendered. React will manage a virtual DOM for you. When changes are detected, it will only render the updated components on the DOM.  IE if the state of data displayed at body>main>section>p changes, only that component will be re-rendered.  Nothing else gets changed. State is managed within the component itself.

- State is best used when you have a componet that has an interternal value that only affects that component and does not affect the rest of the app. State can be accessed through useState hook in functional components, and through this.state in class based components.

```js
 const [question, setQuestion] = useState('Your Question Will Go Here!')
 ```

- In our example from class 37, our component will bind to the value of question.
- The only want to mutate the state and it's binding is to call the function setQuestion.
We use the const keyword to protect the state from direct mutation.

- Props get passed to a component as a function argument.  Props are immutable in the child component. The parent component own the props and therefore that is the only place they can be modified. In functional components, it can be accessed through props, in class based componenets, it is accessed through this.props (You got this in 301).

### Look the lab for today

- We are adding in some additional functionality:
  - The table is now working
  - The table is also alternate coloring
  - Note the hard coded of hourly sales.  This will be similar to the 8 ball answers.
- There is also this thing about thing in files in the Components folder.
- They are also imported in index.js
- > NOTE: Be sure to complete version 1 before moving on to version 2.

### Demo

- Some of this functionality you have already seen. The table for example. That was in our last demo so you have access to that already. There is some very unique stylying though.

- Go to the tailwinds documentation and look up odd or even
- [Tailwinds](https://tailwindcss.com/)

Do something like this

```javascript
return(<tr className="odd:rotate-180">
```

- This is definately NOT what we wanted to do here but this shows us how much easier things can be.
- Add in the even rotation if you did not already.
  
After that we can look at just changing the BG color:

```javascript
return(<tr className="odd:bg-gray-300">
```

- In our next update, we are going to move each of the items in returning DIV to their own file and pass information using props.
- We will start by making a components folder

```bash
mkdir components
```

- I am going to start with the footer because there is nothing to pass to the footer.
- make the header.js
- add the following:

```javascript
export default function Footer() {
    return (

    )
}
```

- Next we can grab the footer info from index. Will look like this:

```javascript
export default function Footer() {
    return (
        <footer className="p-4 bg-gray-500 text-gray-100">
        <nav className="flex items-center justify-left space-x-10">
          <Link href="/careers">
            <a className="text-xl" href="careers">Careers</a>
          </Link>
          <Link href="/aboutus">
            <a className="text-xl" href="careers">About Us</a>
          </Link>
        </nav>
      </footer>
    )
}
```

- Then we need to update the area where the foote was and call the footer component

```html
<Footer />
```

- Then  we need to import Footer in index

```javascript
import Footer from '../components/footer'
```

- Finally we see in our index that `Link` is grayed out. We can remove it from here, but will need it in the footer component. Test that everything is working.

- Next we will move with the header.
  - make a header.js in the components folder.
  - add the following to the file:

```javascript
export default function Header(props) {
    return (

    )
}
```

- I am going to move all of the header information into the header.js in components
We have this answeredQuestions.length.  Where is this information comming from?  The index. How do we get it to the header? Props. I am going to take of the .length. You will understand that in a min.
- Header will look like this now:

```javascript
export default function Header(props) {
    return (
        <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-100">
            <h1 className="text-4xl">Magic 8 Ball</h1>
            <p className="text-xl">{ props } Question Answered</p>
        </header>
    )
}
```

- Next we import `Header` into the index

```javascript
import Header from '../components/header'
```

- Then we can update the return in the index to call the Header and pass in the information we want to send it.

```javascript
// answer count is what we are passing with props so we update props in the header
<Header answerCount={answeredQuestions.length} />
```

- Next we will move on to the QuestionForm.
- Start by creating the question-form.js
- Add in the following:

```javascript
export default function QuestionForm(props) {

    return (

    );
}
```

- Lets get the History/Table going.
- Will end up something close to this:
  
```javascript
export default function History(props) {
    return (
        <table className="w-1/2 mx-auto my-4">
          <thead>
            <tr>
              <th className="border border-gray-700">No.</th>
              <th className="border border-gray-700">Question</th>
              <th className="border border-gray-700">Response</th>
            </tr>
          </thead>
          <tbody>

            {props.answeredQuestions.map(item => (
            <tr className="odd:bg-gray-300">
                <td className="border border-gray-700">{item.id +1}</td>
                <td className="border border-gray-700">{item.question}</td>
                <td className="border border-gray-700">{item.reply}</td>
               </tr>
    ))}

        </tbody>
        </table>
    )
}
```

- Last is the 8 ball.
- Will look like this:

```javascript
export default function EightBall(props) {
     return (
        <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
          <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
            <p className="text-xl text-center">{ props.answeredQuestion ? props.answeredQuestion.reply : 'Ask Me Anything' }</p>
          </div>  
        </div>
    )
}
```

- The index will end up looking like this:

```javascript
import Head from 'next/head'
import { replies } from '../data'
import { useState } from 'react'
import Footer from '../components/footer'
import Header from '../components/header'
import QuestionForm from '../components/question-form'
import EightBall from '../components/eight-ball'
import History from '../components/history'

export default function Home() {

  const [answeredQuestions, setAnsweredQuestions] = useState([])

  function questionAskedHandler(event){
    event.preventDefault();

    const randomReply = replies[Math.floor(Math.random() * replies.length)];

    const answeredQuestion = {
      question: event.target.question.value,
      reply: randomReply,
      id: answeredQuestions.length
    }

    setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
  }

  // function getLastReply(){
  //   if (answeredQuestions.length == 0) {
  //     return 'Ask me anything';
  //   }

  //   return answeredQuestions[answeredQuestions.length -1].reply;

  // }

  return (
    <div>
      <Head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header answerCount={answeredQuestions.length} />
      <QuestionForm questionAsked = {questionAskedHandler} />
      <EightBall answeredQuestion={ answeredQuestions[answeredQuestions.length -1] } />
      <History answeredQuestions = { answeredQuestions } />
      <Footer />
    </div>
  )
}
```