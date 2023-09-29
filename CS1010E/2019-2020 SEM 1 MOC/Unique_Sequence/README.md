# Exercise
Consder a sequence which may be a string, a list, or a tuple. We want to check if the sequence contains a duplicate. A duplicate on the sequence `seq` is defined as two elements on two different index *i* and *j* such that `seq[i] == seq[j]` and `i != j`. In other words, two elements on two different index being equal.

The sequence may contain another sequence. For instance, we have [1, 2, [1], 3] where the list [1] is nested inside the outer list. For simplicity, the checking only need to be a <ins>*shallow*</ins> checking. In other words, we do not need to check if the element 1 from the outer list is equal to the element inside [1]. In this case, all the elements inside [1, 2, [1], 3] are unique. 
### General Restrictions
You are NOT allowed to use:
- Any built-in functions or imported packages. This includes (but not limited to): copy, count, sort, sorted, set, list, tuple, str. 
- Any set functionalities in Python. You are NOT even allowed to create set and/or dict.
- The *in* operator, except if it appears in a loop (for x in e:)
    
    Two <ins>***exceptions***</ins>: you are allowed to use the function len and range. As usual, you are allowed (and even encouraged) to define any additional functions you may need. 

## 2.1 Simple Unique Sequence
### Question
Write a function `is_unique(seq)` that accepts a sequence `seq` that can be one of three types above and returns a Boolean `True` if all the elements inside `seq` are *unique*. Otherwise, the function returns `False`.
### Assumptions
`seq` will be either str, tuple, or list.
### Example
Input 1
<pre>
is_unique('minions')
</pre>
Output 1
<pre>
False
</pre>
Input 2
<pre>
is_unique('abcdefghijklmnopqrstuvwxyz')
</pre>
Output 2
<pre>
True
</pre>
Input 3
<pre>
is_unique([1, 2, 3, 4, 5, 6, 7, 8])
</pre>
Output 3
<pre>
True
</pre>
Input 4
<pre>
is_unique((1, 2, 999, 4, 0, 6, (1, 2), 999))
</pre>
Output 4
<pre>
False
</pre>
Input 5
<pre>
is_unique(['aaa', 'bbb', (1,1), 1])
</pre>
Output 5
<pre>
True
</pre>

## 2.2 Complex Unique Sequence
What we are going to do is we are going to complicate this a little by not allowing both `len` and `range`. You will get this mark automatically if your code for Question 2.1 is correct AND without `len` and `range`.