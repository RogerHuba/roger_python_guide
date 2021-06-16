# Implementation: Stacks and Queues

A _**stack**_ is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous. LIFO

A _**queue**_ is a data structure that consists of Nodes. Each Node references the next Node in the queue, but does not reference its previous. FIFO

## Author: _Leo Kukharau_

## Challenge

### Stack

Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

Create a _**Stack**_ class that has a top property. It creates an empty Stack when instantiated. This object should be aware of a default empty value assigned to top when the stack is created.

- define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance;

- define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value. Should raise exception when called on empty stack;
- define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
  Should raise exception when called on empty stack
- define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty

### Queue

Create a _**Queue**_ class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.

- define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance;
- define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value. Should raise exception when called on empty queue;
- define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue. Should raise exception when called on empty queue
- define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.

## Approach & Efficiency

### Stack:

- `.pop()` - space and time O(1);
- `.push(val)` - space and time O(1);
- `.peek()` - space and time O(1);
- `.is_empty()` - space and time O(1);

### Queue:

- `.enqueue(value)` - space and time O(1);
- `.dequeue()` - space and time O(1);
- `.peek` - space and time O(1);
- `.is_empty()` - space and time O(1);

## API

- class `Node` - Class for the Node instances
- Class `Stack` - which implements Stack data structure with its common methods

  - `.is_empty()` - Method to check if Stack is empty;
  - `.push(value)` - Method takes any value as an argument and adds a new node with that value to the top of the stack;
  - `.pop()` - Method that removes the node from the top of the stack, and returns the node’s value;
  - `.peek()` - Method that returns the value of the node located on top of the stack, without removing it from the stack.

- class `Queue` - which implements Queue data structure with its common methods
  - `.is_empty()` - method to check if Queue is empty;
  - `.enqueue(value)` - method that takes any value as an argument and adds a new node with that value to the back of the queue;
  - `.dequeue()` - Method that removes the node from the front of the queue, and returns the node’s value;
  - `.peek()` - Method that returns the value of the node located in the front of the queue, without removing it from the queue.

<a href="./stacks_and_queues.py">Link to code</a>
