# Exercise

Believe it or not, Happy Number is a *real* definition in mathematics and not something we made up. This should not be confused with Harsahd Number which means "numbers with great joy" in Sanskrit.

A number *n* is a Happy Number if it will eventually become 1 when we replace *n* with the sum of the square of each digit. For instance, 7 is a Happy Number because:

7
⇒ $7^2 = 49$

⇒ $4^2 + 9^2 = 16 + 81 = 97$

⇒ $9^2 + 7^2 = 81 + 49 = 130$

⇒ $1^2 + 3^2 + 0^2 = 1 + 9 + 0 = 10$

⇒ $1^2 + 0^2 = 1$

Let's denote ⇒ as SDS operation to sum the square of each digit. As shown below, 930 would not be a Happy Number because:

930 ⇒ 30 ⇒ 81 ⇒ 65 ⇒ 61 ⇒ 37 ⇒ 58 ⇒ 89 ⇒ 145 ⇒ 42 ⇒ 20 ⇒ 4 ⇒ 16 ⇒ 37

Note how in the case of 930, the number 37 appears twice. Since the process is *deterministic*, if we start with 37, we will always eventually reach 37 again without reaching 1. Therefore, we will never reach 1. 

### General Restrictions

In this question, you MUST work with integers and are NOT allowed to change the input number into any other data types including (but not limited to) float, string, tuple or list. 

## 1.1 Iterative SDS
### Question
Write the *iterative* function `sum_digit_square_I(n)` that takes in a positive integer `n` and returns a positive integer corresponding to the sum of the square of digits of `n`. 
### Restrictions
You may not use recursive function(s) to solve this. 
### Assumptions
$n>0$
### Example
Input 1
<pre>
sum_digit_square_I(123456)
</pre>
Output 1
<pre>
91
</pre>
Input 2
<pre>
sum_digit_square_I(987654321)
</pre>
Output 2
<pre>
285
</pre>
Input 3
<pre>
sum_digit_square_I(999988887777666655554444333322221111)
</pre>
Output 3
<pre>
1140
</pre>
## 1.2 Recursive SDS
### Question
Write the *recursive* function `sum_digit_square_R(n)` that takes in a positive integer `n` and returns a positive integer corresponding to the sum of the square of digits of `n`. 
### Restrictions
- You may not use iterative constructs (*e.g.*, loop, list comprehensions, etc.) to solve this.
- The function `sum_digit_square_R` must be *recursive*. The use of any recursive helper functions will not be counted as being recursive. 
### Assumptions
$n>0$
### Example
Input 1
<pre>
sum_digit_square_R(123456)
</pre>
Output 1
<pre>
91
</pre>
Input 2
<pre>
sum_digit_square_R(987654321)
</pre>
Output 2
<pre>
285
</pre>
Input 3
<pre>
sum_digit_square_R(999988887777666655554444333322221111)
</pre>
Output 3
<pre>
1140
</pre>
## 1.3 Single Happy Numbers
Before you start, there are some facts about Happy Numbers that may make your computation easier:
- For any number *n* such that 0 $\le$ *n* $<$ 10, there are only two Happy Numbers namely 1 and 7. 
    - In other words, 2, 3, 4, 5, 6, 8 and 9 are NOT happy numbers as they will never reach 1 no matter how many times you apply SDS.
- For any number *n* such that *n* $\ge$ 10, the cycle will always produce a number that is smaller than 10 eventually after some finite number of application of SDS.
### Question
Write the function `is_happy_number(n)` that takes in a positive integer `n` and returns a Boolean `True` if the number `n` is a Happy Number and `False` otherwise. 
### Assumptions
- *n* $>$ 0
- If you encounter infinite loop, press `CTRL + C` to stop the execution of your code to IDLE.
- We limit the execution on Coursemology to 2 seconds per test cases.
### Example
Input 1
<pre>
is_happy_number(83)
</pre>
Output 1
<pre>
False
</pre>
Input 2
<pre>
is_happy_number(849)
</pre>
Output 2
<pre>
False
</pre>
Input 3
<pre>
is_happy_number(10888)
</pre>
Output 3
<pre>
True
</pre>
Input 4
<pre>
is_happy_number(100093)
</pre>
Output 4
<pre>
True
</pre>

## 1.4 All Happy Numbers
### Question
Write the function `all_happy_numbers(n,m)` that takes in two positive integers *n* and *m*. The function returns a list of all Happy Numbers between *n* (inclusive) and *m* (inclusive). Your list must be sorted in ascending order. 
### Assumptions
*n* $>$ 0
### Note
- If you encounter infinite loop, press `CTRL + C` to stop the execution of your code to IDLE.
- We limit the execution on Coursemology to 2 seconds per test cases.
- You will only get the mark if your answer to Question 1.3 is completely correct.

### Example
Input
<pre>
all_happy_numbers(1,70)
</pre>
Output
<pre>
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70]
</pre>

