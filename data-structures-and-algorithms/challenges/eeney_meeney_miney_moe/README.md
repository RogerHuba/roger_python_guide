# Eeney Meeney Miney Moe

## Challenge

People are standing in a circle playing Eeney Meeney Miney Moe. Counting begins at a specified point in the circle and proceeds around the circle in a specified direction. After a specified number of people are skipped, the next person is removed. The procedure is repeated with the remaining people, starting with the next person, going in the same direction and skipping the same number of people, until only one person remains, and wins the game.

Write a function called EeneyMeeneyMineyMoe() that accepts a list of strings and an int k. Start at the beginning of the list and count up to k and remove the person at that index from the list. Keep counting from that index and count up to k over and over until only one person is left in the list. Return a string with the name of the last person left in the list.

## Approach & Efficiency

This solution uses a circular LinkedList to store indexes of the given list of names. Then we iterate through the LL removing every k-th element before only one index is left.
This solution can be described as O(n \* k) time and O(1) space

## Solution

<a href="../../challenges/eeney_meeney_miney_moe/eeney_meeney_miney_moe.py">Link to code</a>
