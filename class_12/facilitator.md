# Lecture NOTES: Data analysis with Pandas

## Jokes

You do know, that just under half of all data science jokes are below average, right?

There are two kinds of data scientists: 1) Those who can extrapolate from incomplete data.

A SQL query walks into a bar, walks up to two tables, and asks, “Can I join you?”

## Warm-up or Whitebaord

> Let's work on a Warmup.

```python
# Given nested lists of integers, write some code that will add 2 to each one.
#
# Input:
#
# [[1, 2, 3] , [4, 5, 6]]
#
# Output:
#
# [[3, 4, 5], [6, 7, 8]]

# A few potential ways to accomplish this

def add_two1(nums):
    for arr in nums:
        for num in arr:
            num += 2

    return nums


def add_two2(nums):
    for arr in nums:
        for i, num in enumerate(arr):
            arr[i] = num + 2

    return nums


def add_two3(nums):
    return [[num + 2 for num in arr] for arr in nums]


if __name__ == '__main__':
    list_of_list = [[1, 2, 3], [4, 5, 6]]
    print(add_two1(list_of_list))
    print(add_two2(list_of_list))
    print(add_two3(list_of_list))

```

> We just introduced enumerate in the previous lab code-review.  This may be a good time to go over how enumerate works.
[Enumerate Demo](../demo/enumerate/main.py)

[Broad-casting](../demo/broadcasting/main.ipynb)

> Do a Review of today's Lab
> Fire up a New Kaggle Notebook
> Show how to add in the dataset.
    > click on Add data and search for cereals
> Run the first cell and show the file imported.
> We already have pandas loaded.
> Look at the Docs [Pandas](https://pandas.pydata.org/)

> This is where I got the data from. Under the Data tab, scroll down, and you will see it.
> This is a .csv (Comma Separated Values)
> When we look directly in the .csv file, at the top of the file we see the data headers.
> Not all data sets have this, so this is something we need to account for later.
> Now I want to read in the data.

```python
filename = "/kaggle/input/80-cereals/cereal.csv"
df = pd.read_csv(filename)
```

> We are going to use the df variable which stands for data frame.  Get use to this term. We run this, nothing happens, but also it didn't blow up. Lets take a look at the data that we loaded.

```python
df.info()
```

> If we look at what is displayed, we can see that there were xx amount of entries of data, 0 - xx.
> We also see that our data has been nicely layed out for us, even tells us the data type.
> This is great.  We have this awesome set of data, but this is not how we will normally look at data.
> We look at specific sections, ranges, and filtered data.  Let's do some of that. We are often working with hundreds of thousands, even millions of lines of data.
> First we can look at the first five and then the last 5 entries in the data set with the following:

```python
df.head()
```

```python
df.tail()
```

> That is a good start to filtering some data.  If we dig a little we can filter a little more
> Lets do a filter by name and see what comes up

```python
df['name']
```

> With this we get a list of just the name column.

> QUESTION: What if I wanted to look at the last 10 but only the name column?

```python
df['name'].tail(10)
```

> QUESTION: What if we wanted to get column list of names and calories?
> Try with only a single [] first and look at the error
> Note that the single name will work in the double [[]] as well

```python
df[['name', 'calories']]
```

> if we look at the ordering, you may not like that.  It is not telling the story that you want it to tell.
> we can get rid of that with the following:

```python
df.set_index('name')
```

> We can see the numbering is gone, and the name is a sub-set on the main menu.
> Lets get a little wild now.  I wand to show name, rating, and sugars, and want to sort assending on the rating
> QUESTION: Ideas or thoughts?

```python
df[['name','rating','sugars']].sort_values('rating', ascending=False)
```

> This is all great, we are looking at the date we have and filtering, but all data will not be that simple.
> Data Science is all about looking at and shaping data to tell a story. Let's tell a little story.



> QUESTION: What is the difference between mean, median, mode, and range?
> mean = average
> median = the middle value
> mode = the value that is repeated the most
> range = the difference between lowest and highest value
> We can do things like look at the max or min of something

```python
avg_carbo = df[['sodium']].mean()
avg_carbo
```

```python
median_carbo = df['carbo'].median()
median_carbo
```

```python
min_carbo = df['carbo'].min()
min_carbo
```

```python
max_carbo = df['carbo'].max()
max_carbo
```

> What if we do something like this where we want to get a list of carbs < 10

```python
df[df['carbo'] < 10][['name','carbo']]
```

```python
mcc = df['carbo'].mode()
mcc
```

> This is some cool stuff, and some easy way to display data. It takes a little to get use to but once you get the hang of it, you have a lot of power at your fingertips.
> You are not just limited to Pandas stuff though.

```python
import numpy as np
df[df['carbo'] == np.mean(mcc)][['name','carbo']].set_index('name')
```

> Woah, I just imported numpy and used it, but I didn't add it to my Poetry project!
> QUESTION: Idea on why this worked?
> ANSWER: Pandas uses Numpy, so it is a sub-dependency.

> If you now anything about statistics, you may know about the term standard deviation. Pandas calculates this for us
> on the fly.

```python
df['calories'].std()
```

> In statistics, the [standard deviation](https://www.mathsisfun.com/data/standard-deviation.html) is a measure of the amount of variation of a set of values.
> A low standard deviation indicates that the values tend to be close to the mean of the set
> A high standard deviation indicates that the values are spread out over a wider range.


> Add to demo for their own review

```python
def manfacturer_name(mfr):
    map = {
        'A':'A',
        'G':'General Mills',
        'K': 'Kellogs',
        'N': 'Nabisco',
        'P': 'P',
        'Q': 'Quaker',
        'R': 'Ralcorp'
    }

    return map.get(mfr)

df['Manufacturer'] = df['mfr'].apply(manfacturer_name)
df[["Manufacturer","sugars","protein"]].groupby("Manufacturer").median()
df[df['mfr'] == 'A']


```
