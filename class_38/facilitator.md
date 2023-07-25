# Lecture NOTES: React II

## Jokes

- Why did the orange stop? It ran out of Juice
- What happens to grapes when you step on them?  They wine.
- A cheese factory exploded in France. Da brie is everywhere!
- A friend of mine doesn’t pay his exorcist. He got repossessed.
- I begin to read a horror novel in Braille. Something bad is about to happen, I can feel it.

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
# This is defining a method called depth_first_search that takes a vertex parameter and belongs to a graph object.
def depth_first_search(self, vertex):
    # This line checks if the given vertex is a valid node in the graph using the get_nodes() method of the graph object. If the vertex is not found, it returns an empty list.
    if vertex not in self.get_nodes():
        return []
    # This line creates three variables: result, stack, and visited. result is an empty list that will contain the visited vertices in the order they were discovered. stack is initialized as an empty stack that will hold the nodes that still need to be visited. visited is an empty set that will contain the visited nodes so far.
    result, stack, visited = [], Stack(), set()
    # This line pushes the vertex onto the stack to start the search.
    stack.push(vertex)
    # This initiates a while loop that continues as long as the stack is not empty.
    while stack:
        # This line gets the top element of the stack without removing it using the peek() method.
        top = stack.peek()
        # If the top node has not been visited before, this line appends its value to the result list.
        if top not in visited:
            result.append(top.value)
        # This line adds the top node to the visited set.
        visited.add(top)
        # This loop checks if there are any unvisited child nodes of the top node. If so, it pushes the first unvisited child onto the stack and sets the has_unvisited flag to True.
        has_unvisited = False
        children = [edge.vertex for edge in self.get_neighbors(top)]
        for child in children:
            if child not in visited:
                has_unvisited = True
                stack.push(child)
                break
        # If there are no unvisited child nodes left for the top node, it removes the top node from the stack using the pop() method.        
        if not has_unvisited:
            stack.pop()
    # Finally, the result list containing the visited nodes in the order they were discovered is returned.
    return result
```

## Stepping Back / Requirements
- We're making progress. Let's see how things stand.
See the hard coded `1 questions answered` in upper right?
That's not gonna work. It should start at zero then increment as questions are answered.
In other words, the number of questions answered should be part of our app's `state`
So let's step back and think about our app's state.
Currently we keep track of the latest reply, which works ok for rendering the 8 Ball.

But it works less well for tracking the number of questions answered. And it won't work at all for the future table at bottom which tracks the complete history of questions and replies.

Let's put that to the back of our mind for the time being.  We will address this very shortly.

## Move Items to their own componenets

- Thinking in React was in readings. Use the demo as a chance to model this approach.

- Start in index and determine components needed.
  - Root component
    - Head (from Next)
    - Header
    - QuestionForm
    - EightBall
    - History (not yet created)
    - Footer

- First we need to create a components folder.
  - In here we will create .js files for each of the above (we will leave the Head in the index as that is a specific component from Next).
  -  Open up the Header.js file
     -  Add the following code
    
    ```JavaScript
      export default function Header() {
          return (
              <h1>Pass</h1>
          );
      }
    ```

  - With the Header file, lets copy the header from the index here.
    
    ```JavaScript
        <header className="flex items-center p-4 justify-between bg-gray-500 text-gray-50">
          <h1 className="text-4xl">Magic 8 Ball</h1>
          <p>0 questions answered</p>
        </header>
    ```

    - In the index.js comment out the old code and label it.
    - Add the following below it.
    
    ```JavaScript
    <Header />
    ```

    - When we save this we get an error on our Page.
    - ```Header not defined```
    - What's missing?
    - ```import Header from '../components/Header';

    - Now we come back to the hard coding of the our answer count
      - Determine required attributes.
        - E.g. Header needs a count of answered questions.
      - Don't worry about functionality yet, just focus on properly declaring attributes / receiving props.
        - Hard coded attribute values are fine to start with.
        - E.g. <Header answerCount={0} />


  - Once component is properly declared and wired up then style it.
    - Refer to completed demo for styling.
  - Once component is styled and functional then refactor to remove hard coding.
    - E.g. <Header answerCount={answeredQuestions.length} />
    - For Header this means storing answeredQuestions array via the useState hook.
  - Confirm that Header continues to render properly.
  - Repeat above steps for remaining components.
  - When you get to Footer it will be time to talk about navigation/routing.
    - Don't add Link just yet, will come back to that.

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
    const randomReply = replies[Math.floor(Math.random() * replies.length)];
    
    // This is the new stuff below
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
        } else {
            return answeredQuestions[answeredQuestions.length - 1].reply;
        }
    }
```

Almost there. Now we need to modify the 8 Ball Component to use `getLatestReply` function instead of just `reply`

Update innermost `<p>` tag

```javascript
<p className="text-xl text-center">{getLatestReply()}</p>
```
Run the app and make sure still works.

## QuestionForm
    - Next is the QuestionForm
      - Open the file and add the following:
      
      ```JavaScript
      export default function QuestionForm({ askedQuestion }){
        return(

        )
      }
      ```
    - This will give us our basic outline for the askedQuestion Form. Lets copy what we have from the index. We can go ahead and call the question from now too in the index
    - ```<QuestionForm askedQuestion - {QuestionAskedHandler} />```
    - There are is going to be a little change here. I want to handle the event here in the form, not in the index.  So a couple of small changes that need to happen
    - Add this function above the return()

    ```JavaScript
        function handleSubmit(event) {
        event.preventDefault();
        askedQuestion(event.target.question.value);
        event.target.reset();
    }
    ```

    - Now that we are handling the event here, we can change the event in the index to just handle the question, and the QuestionForm will handle the event.
    - Change ```function questionAskedHandler(event)```
    - to ```function questionAskedHandler(Question) ```
    - also comment out the event.prevenDefault
    - Will need to change the object to Question.value or Questionin place of the event.

## Questions Answered Count

It does? Great! Let's get back to the `X questions answered` feature.

Currently it always says 0. Armed with our new app state how could we remove that hard coding?

Update header component's `<p>` tag

```javascript
<p>{answeredQuestions.length} questions answered</p>
```

See what's different? The hard coded 1 has been changed to be whatever is the length of `answeredQuestions`

That's exactly what we want, and React will take care of re-rendering the header whenever that value changes.

## History

- Update the index to 
- ```<History questionList={ answeredQuestions } />```

- This will go in the History.js file
```JavaScript
export default function History({ questionList: answeredQuestions }) {

    if (answeredQuestions.length === 0) {

        return (
            <h2 className="w-1/2 mx-auto my-8 text-4xl text-center">
                No questions have been asked
            </h2>
        );

    } else {

        return (
            <table className="w-1/2 mx-auto my-4 border">
                <thead>
                    <tr>
                        <th className="border border-black">No.</th>
                        <th className="border border-black">Question</th>
                        <th className="border border-black">Response</th>
                    </tr>
                </thead>
                <tbody>
                    {answeredQuestions.map(item => (
                        <tr key={item.id}>
                            <td className="p-2 border border-black">{item.id}</td>
                            <td className="p-2 border border-black">{item.question}</td>
                            <td className="p-2 border border-black">{item.answer}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        );
    }
}
```

Update the Footer
Add to footer.js

```JavaScript
import Link from 'next/link';

export default function Footer() {
    return (
        <footer className="p-4 text-gray-100 bg-gray-500">
            <nav className="flex items-center space-x-10 justify-left">
                <Link href="/careers">
                    <a className="text-xl" href="careers">Careers</a>
                </Link>
            </nav>
        </footer>
    );
}
```

Update Index
```<Footer />
```
import Footer
Add careers.js in the pages folder


Add to careers.js

```JavaScript
import Link from 'next/link'

export default function Careers(){
    return(
        <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
            <h1 className="text-4xl">Careers Page Coming Soon!</h1>
            <Link href="/">
                <a className="p-4 m-4 text-2xl bg-gray-300 rounded-lg">Back to Home Page</a>
            </Link>
        </div>
    )
}
```
