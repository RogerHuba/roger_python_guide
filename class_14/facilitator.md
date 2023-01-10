# Lecture NOTES: Data Visualization with Seaborn

## Dad Jokes

- What's Forrest Gump's password? 1forrest1
- What do you call a fancy fish? So-fish-ticated.
- If two vegetarians get in an argument, is it still called beef?

## Talk about up-coming project week.

## Warm Up

- Given a linked_list where the data is a list of integers, find the highest value

## Review Assignment

- Head to Canvas and look at assignment that is due.

### Demo

- Fire up a .ipynb file

```python
poetry add pandas
poetry add matplotlib
touch fun_with_seaborn.ipynb
```

> You already got a little taste of seaborn. I don't want you to dismiss matplotlib though. There are times when it still makes sence to use matplotlib because you are doing something quick or because it has features that the other libraries don't have. Matplotlib can be simple to use to quickly visualize some data. Let's plot some lines

```python
import matplotlib.pyplot as plt
```

> I'm not going to dig into these methods because it is going to be replaced by seaborn

```python
plt.figure()
x1 = [2,4,30,45,60]
x2 = [45,44,36,22,1]
plt.plot(x1, label='Anakin Darkside Meter')
plt.plot(x2, label='Younglings in Temple')
plt.legend()
plt.show()
```

> Pretty nice, not overly difficult to quickly generate a graphic to display some data. But..... Lets see what we can do with seaborn.

```python
import seaborn as sns
```

> The crazy thing about seaborn, is that if nothing else other than being at the party, it can make the party a little more fun, or in our case make matplotlib look better

```python
sns.set()
```

> This puts seaborn in charge of the astetics and makes some defaults. There are other things you could pass in but for now we can just use the defaults. Copy and paste the code from above and run, compare the 2 plots. Not a ton of changes there, and if you like that style, easy to go with. We can change the theme back to white if we so choose or change to dark

```python
sns.set()
# sns.set(style='whitegrid')
# sns.set_style('whitegrid')
# sns.set_style('darkgrid')
# sns.set(font='serif')
```

- Rerun the figure drawing after each style.  Leave the dark when done.
- 
> There are 4 styles that are used, dark, whitegrid, darkgrid, and ticks. You can play with them to see what you like to use. There are 2 ways to set the style. We can also experiment with things like font.

```python
sns.set(font='serif')
```

> Or change the color of a line to a specific color

```python
plt.plot(x2, label='Younglings', color='red')
```

> As I mentioned in the previous class, seaborn has some built in datasets that you can play around with. Last class we saw the anscombe set, today we are going to look at some flight data.We can load the data set as such:

```python
flights = sns.load_dataset('flights')
flights
```

> We see here we have a real data, as sns has given us a nice pandas data frame. Super easy to bring into our notebook. They did not need to recreate the wheel. If you want to see the datasets that sns has available:

```python
sns.get_dataset_names()
```

> with our existing data I want to look at some data in the flight data. Lets built a quick visual

```python
sns.relplot(x='year', y='passengers', hue='month', data=flight)
```

> I have some breaking news: From 1950 to 1960 the amount of people using the airlines greatly increased. Ok, not so breaking. You are probably not going to get any designer of the year awards for data visualization, but this is good enough to put in front of a group for a presentation and tell a story.Maybe this is not the story that you want to tell, maybe you don't care about the spread of months but just want this grouped by years. This is based on a pandas df, so we can do that if we want.

```python
year_sums = flight.groupby('year', as_index=False).sum()
sns.relplot(x='year', y='passengers', data=year_sums)
```

> This looks like a pretty steady line to me going up.  As we know our eyes can deceive us, so let's plot it out just to be sure.

```python
sns.lmplot(x='year', y='passengers', data=year_sums)
```

> Based on what I see, I would imagine that 1965 is going to be on the same trajectory.  Years like 2001 and 2020 may have some dips, but over all pretty steady.

> Are there other charts or plots that may tell a better story?  How about a bar plot?

```python
sns.barplot(x='month', y='passengers', data=flight)
```

> If you are getting tired of seeing the instance of the graph, say for a presentation, you can get rid of that by using the print() command.  Nice little hack there.

> There are a few other things you can do to make this plot look better. Maybe we want to rotate the months to be inline with the bar graph.  To do this we want to assign the graph output to a variable.

```python
g = sns.barplot(x='month', y='passengers', data=flight)
g.set_xticklabels(labels=flight['month'], rotation=90)
print()
```

> If you want to move the rotation to an angle change the rotation to 45.
> Now you may be wondering what these lines are on the bar chart. They reference the confidence levels. You almost never say with 100% certainty that somehting is. Especially when dealing with statistics. We say "with a 95% confidence level" this is the case.  You can override this by adding in a ci=None

```python
g = sns.barplot(x='month', y='passengers', data=flight, ci=None)
g.set_xticklabels(labels=flight['month'], rotation=90)
print()
```

Statistics can be confusing.
[Confience Interval](https://www.investopedia.com/terms/c/confidenceinterval.asp)

> This once came about from an experiment. Trying to do some different charts, I tried to implement a pie chart, 45
> min later I was still struggling. Seaborn makes things easy, why is this so difficult. Turns out that pie charts are
> so overused and disliked, seaborn omitted them completely. There are some workarounds to do it, but IMO not worth
> the effort
- [Evil Pie Charts](https://medium.com/@clmentviguier/the-hate-of-pie-charts-harms-good-data-visualization-cc7cfed243b6)
- [Statistics from 21 Movie](https://www.youtube.com/watch?v=BHO5z91BS_E)
