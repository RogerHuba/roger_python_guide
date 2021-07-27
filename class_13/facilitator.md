# Lecture NOTES: Linear Regression

## Jokes
Q: Why did the fly never land on the computer?
A: He was afriad of the world wide web.

Q: What's the internal temperature of a Tauntaun?
A: Lukewarm

Q: What do you call five Siths piled on top of a lightsaber?
A: Sith-kabob

Q: Where did Luke get his bionic hand
A: Second hand store


## TA Code Challenge

- Have a TA do a code challenge of 
    - Given a list, reverse the list.
    - Once they get that, update the problem,
    - Gived a linked-list reverse the list

## The Why

> Let me ask you a Hypothetical Question.
    > If we had all Covid Data could we...
    > Guess where outbreaks were going to occur?
    > Guess when the spread will slow
    > Guess when we can get back on Campus
> Liner Regression and training model data could help us with some of those answers.
> Now, we need to have GOOD data in order to make a good guess.
> The more data points we have, the more accurate our estimates become.

## Lecture Things

> Let's look at the Lab for Today.  Linear Regressions.
> Open up kaggle.com and look for some data
> Explain that they need to prove their conclusion
> No acceptance tests today.

> Today I am going to do something a little different.  I am going to use an online
> tool by google called colab, or Colaboratory.
> You are will be doing this in your standard way:

```python
mkdir folder
cd folder
poetry init -n
poetry add pandas matplotlib sklearn juypterlab
touch regression.ipynb
code . or juypter lab
```
> If we want to work on some data, well we need to find some data to play around
> with.  I have this salary.csv file that I am going to use.
> Look over the CVS to see what kind of data we are looking at.
> We want to use this data to visualize our data, and start making some
> predictions based on what we see.
> I created another csv file that has something called snacks in it (explain)
> Next we will start our imports

Will need to drag and drop salary.csv into google.colab

```python
import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
```

> Next let's read in our data file.

This is specific to google.colab

```python
from google.colab import drive
drive.mount('/content/drive')
```

```python
salary  = pd.read_csv('salary.csv')
salary.head()
```

> Sweet.  We have some Data.  Next we need to get the data into the form we need
> by the tools to do the linear regression. Lets go through these steps.
> This is called selecting the features

```python
# Selecting Features
X = salary["YearsExperience"].values
y salary["Salary"].values
```

> This is often referred to as X. This is what we are going to pay attention to
> We will use a lower case y to look at the salaries.
> The upper case X is seen as the independent variable while the lower case y is
> dependent. We want to look at years of Experience and see how it relates to ones
> Salary. We can see the data

```python

# X Data
X

# y Data
y
```

> Right now X is not in the shape that we need it, specifically what the test
> train split is going to want. It needs a particular shape.
> The good news is we can reshape it.

```python
# (as many rows as are needed -1, and the columns we set to 1
X = X.reshape(-1, 1)
X
```

> QUESTION:  What did we do to our data?
> Converted from a 1 dimensional array to a 2 dimensional array
> train_test_split needs this specific shape.

```python
# Keep Track of our Data
# X feature = Years of Experience
# y = salary in $
```

> We are going to split this data into training portions and testing portions
> QUESTION: Anyone have a sence as to why we are doing this?
> Why split into test and train portions?
> The train_test_split function is for splitting a single dataset for two
> different purposes: training and testing. The testing subset is for building
> your model.  The testing subset is for using the model on unklnown data to
> evaluate the performance of the model.
> If you had 1000 records you could use the first 200 for your testing, and then
> use the remaining 800 for training your data. This may not give you a good
> randomization of your data.  You may be skewed based on how it is sorted.
> The code for this is not to crazy.
> We want to get (4) things back. Well, to be technical we get back 1 thing, a
> tuple but the tuple has 4 things in it

add to previous
```python
# Keep Track of our Data
# X feature = Years of Experience
# y = salary in $
# We are going to get this data back from the return of train_test_split
# train_test+split wants a few things
x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=.8, test_size=.2, random_state=100)
```

> I ran this, and it didn't break. Let's look at some of our data now.

```python
print(f"X_train shape [{x_train.shape}")
print(f"y_train shape [{y_train.shape}")
print(f"X_test shape [{x_test.shape}")
print(f"y_test shape [{y_test.shape}")
```

> From the data we got some shape data back. Why did we do this?
> 1) to plot the data, (2) Do some analysis of the data

> Let's see what it will take to plot this data using matplotlib

```ptyhon
plt.scatter(x_train, y_train, color='red')
plt.xlabel('Years of Experience')
plt.ylabel('Salary in $')
plt.title('Training Data')
plt.show()
```

> This is what 80% of the data plots out as. It looks like we have a connection
> between years of experience and salary. Good to notice that but how much of a
> connection is there. Our eyes are great, but we can be deceived.

```python
lm = LinearRegression()
lm.fit(x_train, y_train)
```

> Now we want to make some predictions. What will our salary be as it relates to
> years of experience.

add to previous
```python
lm = LinearRegression()
lm.fit(x_train, y_train)
y_predict = lm.predict(x_test)

# What will these prediction look like?  Lets run it and find out.
print(f'Train Accuracy {round(lm.score(x_train, y_train)* 100,2)}%')
print(f'Test Accuracy {round(lm.score(x_test, y_test)* 100,2)}%')
```

> So we ran some predictions, then we asked it for a score.
> We can look at what the score does bu looking at the help file

```python
help(lm.score)
# can also use
?lm.score
# This will show up different here in google.colab
```

> Now here is some great reading material. Essentially is telling us how our
> testing data compares to our training data. Now I am not versed enough in the
> Data Science world to know what I need or don't need.  96% looks good to me.
> Now lets plot this out and see what it looks like.

```python
plt.scatter(x_train, y_train, color='red')
plt.plot(x_test, y_predict)
plt.xlabel('Years of Experience')
plt.ylabel('Salary in $')
plt.title('Trained Model Plot')
plt.plot
```

> We drew a prediction line in how years of experience relates to salary.
> QUESTION: What would you infer from this data?
> We could potentially dig into the data little here and look at some of the
> outliers on our plot.
> If this is something you want to do to prove your hypothesis, then you will
> have a little research to do on what methods or other libraries to import.

> I mentioned earlier that I have another csv file that I did some things with
> and added some snacks. Lets see if we can prove that salary goes up based on
> the number of snacks consumed in a day.
> Let's walk through our code and change years of experience to snacks

Things we need to update:
- csv file
    - Here we notice that everything will still work?
    - QUESTION: Why does everything still work with a new file?
    - ANSWER: Because we still have Years of Exp in there
- Update our X to "Snacks'
- Update X Plots Data

> This was  not overly difficult to make the change and see the new data.
> But I am a developer, I am inherently LAZY.  I want to do a little work as
> possible. So let's do a little more work, so we ultimately have to do less work.

> We are going to use something called Seaborn. We will learn a little more about
> Seaborn next week, but we can use it a little today.

```python
import seaborn as sns
```

```python
# Am going to add this. If you want to know more, it is a help() or ? away.
sns.set()
plt.figure(figsize=(10,6), dpi=300)
sns.regplot(x='YearsExperience', y='Salary', data=salary)


sns.set()
plt.figure(figsize=(10,6), dpi=300)
sns.regplot(x='Snacks', y='Salary', data=salary)
```

Navigate to [Anscombe's Quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet)

> We can actually play around with this data a little
> Seaborn comes with some free data.

```python
anscombe = sns.load_dataset("anscombe")
sns.regplot(x="x", y="y", data=anscombe.query("dataset == 'II'"))
```

> When we look at the data, our eyes tell us that data goes up and goes down, but
> not as linear as we may think, but our linear regression is telling us that we
> have an upward trend.
> Change to this adding the order=2. Simple, this is the number of bends we have
> 2 accounts for the starting up, leveling out, and then heading back down

```python
anscombe = sns.load_dataset("anscombe")
sns.regplot(x = "x", y = "y", data=anscombe.query("dataset == 'II'"), order=2)
```

> Here is another one

```python
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           robust=True, ci=None, scatter_kws={"s": 80})
```

```python
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'IV'"),ci=None, scatter_kws={"s": 80})
```
