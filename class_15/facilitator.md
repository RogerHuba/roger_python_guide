# Trees

## Dad Joke
- Why do trees hate riddles? To each to get stumpted?
- Why did the tree get stumped? Couldn't get to the root of the porblem
- Trees favorite drink:  Root Beer
- What did the tree do when the bank closed? Opened it's own branch
- `Why are trees tge best a networking? They always branch out.`
- `How do you know a tree had to much root beer? Won't stop texted his AX.`
- `What is a brief description of an acorn? In a nutshell, it's an oak tree!`
- `What side of the tree has the most leaves? The outside.`
## Trees
- Review the Implementation Assignment
Real world examples
- 3D video game to determine what objects need to be rendered.
- Databases indexes. When you index a field, it is put in a binary tree for fast retrieval.


> Let's talk about trees. Before we can dig in to deep we nned to talk about the bits that make up a tree.  A tree is a node based file structure. Similar to LL, stacks, and queues.

> Draw on the screen a node.  Instead of having a next, in a Binary Tree we have something called a left and right which point to other nodes in the tree.  For most of the examples that you will see, the value will be a int or a string, but as you saw in the previous class warmup, the value can be whatever (int, string, list, object, link_list)
- Tree Nodes contain:
    - Value - int, string, list, object, link_list
    - Left Child - points to another node or None
    - Right Child - points to another node or None

> Looking at our drawing here we have a single node in our tree. Like the head of a linked_list the top of the tree has a identifier called '`Root`.
- Label root on drawing.

Add a left Node with a value
Right now there is a right but it is None.
Add a right node with a value
On the right node add a left and right node (add a right to this node)


Every node in the tree will have 0, 1, or 2 children in a Binary Tree
Each node will have attributes of
- value
- left
- right

> You will see different variations of this on the internet.  You may see things like data, left/right child, left/right node.  We are going to stick with value, left, and right for class but any of these are correct.

QUESTION: What does an instance of a LL know about?
ANSWER: It knows the head

QUESTION: What will an instance of a BT know about?
ANSWER: It will know the root.

What are some operations we can do on a Binary Tree?
- Draw out a Binary Tree with Letters (3 nodes)
- The entire tree has a root. root b, left a right c

```text
    B
  /   \
 A     C
 ```

- Lets traverse through our tree.
  - One of our Key differences here is that we are not moving in only 1 direction, ie they are linear. Only one way to go. We have to consider root, left and right. BT are not linear. Traversing is also refered to as walking.  So if I say walk through.  We have 3 primary ways we "walk" through a tree.

  - `pre order` root >> left >> right
    - This means that any work we do, we do in the root firest, then the left, then the right. As you get into each child, you apply the current order to the existing node.
    - If our job was to print out the values of our tree we would end up with:
      [b, a, c]
  
  - `in order` left >> root >> right
    - This means that any work we do, we do in the root firest, then the left, then the right.
    - If our job was to print out the values of our tree we would end up with:
      [a, b c]
  
  - `post order` left >> right >> root
    - This means that any work we do, we do in the root firest, then the left, then the right.
    - If our job was to print out the values of our tree we would end up with:
      [a, c, b]
  
The operation of these 3 traversals are similar, it is about the order of doing things (Hint, same code, different order)

These 3 traversals are a `depthfirst traversal`.  You start at the top and work down.  There is something callded a `breathfirst` traversal which we will learn more about in a future class.

This talk assumes you completed the required tree reading. In the reading, there is pseudo-code for all 3 order methods.

- Re-review the implementation assignemnt.
- Let them know there is some demo code and a couple of tests in the class repo.