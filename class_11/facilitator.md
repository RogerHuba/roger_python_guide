# Demos: Class 11 - Intro to Data Science with Numpy

> Welcome to Module 3. YOu have completed 20% of Python.  Only 80% to go.
> First 2 modules were about getting and applying some of the python language
> If you are still struggling with python concepts. Check out [HolyPython](https://holypython.com/beginner-python-exercises/poetry )

## Demo Jupyter Notebook

> NOTE: Feel free to follow along with what I do, but if you get an error(Weather VS Code, Poetry, Jupyter or other) on your end, hold off questions until the end of lecture or when we get to Lab Time.

```bash
mkidr numpy-fun
cd numpy-fun
poetry init -n
poetry add numpy matplotlib jupyterlab
```

> These 3 dependencies are pretty big. Depending on the speed of your internet and the strength of your computer, this could take a few minutes to complete.

```bash
touch notebook-fun.ipynb
# QUESTION: What does ipynb stand for? Interactive Python Notebook
poetry shell
code .
```

The first time you open VSCode and click on your .ipynb file, you will probably get a prompt to install

- Python XXX 64-bit requires ipykernel to be installed.  Source Jupyter (Extension).
- Click Install and let VS code do its thing. You should be able to ignore warnings.

> NOTE: There may be some issues with Big Sur and Jupyter Notebook. Time to get your Google-FU ready.

- Make sure to select the proper interpreter

> Lets run a command

```python
print('Hello World from Jupyter Notebook')
```

> Couple of ways to get this to run:

> - I can do a shift-enter.
> - I can press the play button to run just this cell.
>   - Add a new Cell with a division by 0, then create a new cell with a print to show the error won't break things
> - I can press the button to run everything.

> - Show the arrows that can move cells up and down in the order of execution.
> - While you can run each cell individually, subsequent cells will be aware of any global variables.

> - Show an example of creating a variable in once cell and printing it in the next.

```python
message = 'Python is fun!'

print(message)
```

> This looks like it is running from Top to Bottom, but that is not entirely true.  What matters is the Numbers of execution.
>
> Add at the beginning in the first cell and talk about execution order.

```python
print(message)
```

> Show the clear all output, then restart the server and show the execution clears.
> Run first line again and now we have an error
> Jupyter Notebook can be used for Presentations and is not only for Python
> Create a new Cell and click the Enter Markdown Mode.

```markdown
# My Awesome Notebook Project
```

NOTE: We will close out the notebook-fun file now.

## Demo for the Lab

```bash
touch checkerboard.ipynb
```


> One thing we are going to need right away is Numpy. Press the 'I believe' button on this and trust me.

```python
import numpy as np
```

> This will import Numpy with an alias of np.  This is industry convention to use. np can be anything.
> numpy will allow us to see straight data. If we want to visualize data, that will take another library, but we will come back to that.
> let's do some things with numpy arrays.
> We are going to need an 8 x 8 matrix (an array of arrays)
> Numpy makes this very easy. I am not going to waste your time and show you the long way to do this.
> Lets make a board / grid.

> How can we set this up? Well lots of ways. The typical way is to give it a default value.
> You want to be able to give this matrix a certain shape. (matrix is not contained to just 2 dimensions)
> In our case we are going to want: 8 x 8 x 3
> We are going to store values that represent a color in a space called RGB (Red Green Blue) and we are going to want values for each of those.

> One way we can do this is by taking advantages of this numpy array called np.ones()

```python
grid = np.ones()
```

> This will return an array of ones with the shape and typy of the input.  But how do you know this other than taking my word for this?

> We can access help files by doing something like this:

```python
# grid = np.ones()
help(np)
help(np.ones)
```

> We can see that it is looking for a shape, and we can even see some examples of how to run this.
> In our case we want a 3 dimensional array to be filled with ones.
>
```python
grid = np.ones((8,8,3))
```

> With this we get 3 values in the inner array, 8 rows, and anyone want guess how many sets? 8
> We could also use zeros (change the example to zeros, but change back to ones)

```python
grid = np.zeros((8,8,3))
```

> Because we have a 3 dimensional grid, we can use tools that numpy use for visualization, we can make some assumptions.
> One of them is called matplotlib.  Lets do the import for this now. Update the first cell to this:

```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
```

> NOTE: %matplotlib inline is actually called a python magic function. In some displays, it will add your run code right above your plot.  Not required.
> NOTE: Do not execute the cell yet (unless called out by the class)

> Now we can do some things with plt.  New cell with plt.imshow() but run the help on it.

```python
help(plt.imshow)
plt.imshow()
```

> ERROR.  Uh-oh.  What happen here?  NOTE: We did not re-run the first cell.  Re-run it and then re-run the help.
> If we dig thorough the help we would see that imshow is looking for an ndarray. Well we just happen to have one of those. If this follows some rules on how imshow uses the ndarray, something should happen for us.
>
```python
plt.imshow(grid)
```

> And super cool, we have what looks like a 8 x 8 grid.  We also have the x3 there, just can't see it.
> Any ideas why this appears to be empty?
> If you remember back to HTML RGB, you would give values from 1 to 255.  This determines how far along you are on the 8-bit color scale. That is not how matplotlib works, it wants between 0-1. Think of 1 as full (as compared to html where 255 is full)
> So in html, what is RGB(255, 255, 255).  It is White. What is RGB(0, 0, 0).
> Change to zeros instead of ones and show the block box.
> We definitely have something going on here.
> It is hard to visualize this right now but if we think about what we have here, we have a 8 x 8 grid.
> How could we change the top left grid at 0,0 to white? Ideas? Could we treat it like a list?

```python
grid[0][0]
```

> Run this.  What do we get back? A list of something. It is actually a numpy array, but we get back a collection of 3 things.  We know the 3 zeros is black, how do we make it white? We assign a 3 dimentional color mapping.

```python
grid[0][0] = (1,1,1)
# or
grid[0,0] = (1, 1, 1) # This is numpy specific
blue: (.1, .2, .5)
```

> Didn't break anything. But also didn't change our grid. Oh, that is because we need to execute the grid again.
> BOOM.  There we go. We should feel good about that because it is doing what we thought it would. Do an example of turning off each of the red / green / blue to show the different colors. Change back to ones.

> Any questions here?

> Next we want to color something down and to the right?  Get a student to provide the answer:

```python
grid[0][0] = (0, 0, 0) # Black
grid[0][0] = (1, 0, 0) # Red
grid[0][1] = (0, 0, 1) # Blue
```

>If there is time color the wrong square, then correct it and show that it is still holding on to the shape that was set, the bad square was not reset.

> What if wanted to color a square across the entire diagonal?  How about some sort of loop?  What is the pattern?

> We could do this

```python
grid[0][0] = (0,1,0)
grid[1][1] = (0,1,0)
grid[2][2] = (0,1,0)
grid[3][3] = (0,1,0)
grid[4][4] = (0,1,0)
grid[5][5] = (0,1,0)
grid[6][6] = (0,1,0)
grid[7][7] = (0,1,0)
```

> This makes me sad. Very NOT DRY.

```python
green = (0,1,0)
for i in range(8):
    grid[i][i] = green
```

> Now using this way of thinking, start formulating your pattern to get a true checkerboard / chessboard.
> I won't give that away, that is part of the fun of today's lab.
> We did just a simple grid, but why not use a little more Python?
> How about we create a class in our our notebook?

```python
class Board:
    def __init__(self):
        self.grid = np.zeros((8,8,3))
```

> Then you have a board instance.
> Look at the Lab. Look at the methods it is asking for?
> You will end up with something "close" to this

```python
class Board:
    def __init__(self):
        self.grid = np.zeros((8,8,3))

    def add_red(self, row, col):
        pass

    def add_blue(self, row, col):
        pass

    def render(self):
        pass

    def is_under_attack(self):
        pass
        # Return True if red is under attack?
```

> Explain how queens attack
> Give a quick example that if the 2 queens are on the same row or same column they are under attack.
