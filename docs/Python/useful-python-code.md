# Useful Python Code

## Anagram
```python
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
# If the Counter objects of two strings are equal, then they are anagrams.

from collections import Counter

str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, cnt_3  = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print('1 and 2 anagram')
if cnt_1 == cnt_3:
    print('1 and 3 anagram')
```

## Convert Title case

```python
my_string = "test scenario again"

# using the title() function of string class
new_string = my_string.title()

print(new_string)
```

## Counter

```python
## Python counter keeps track of the frequency of each element in the container. Counter() returns a dictionary with elements as keys and frequency as values.

# finding frequency of each element in a list
from collections import Counter

my_list = ['a','a','b','b','b','c','d','d','d','d','d']
count = Counter(my_list) # defining a counter object

print(count) # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print(count['b']) # of individual element
# 3

print(count.most_common(1)) # most frequent element
# [('d', 5)]
```

## Digitize

```python
import time

num = 123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456

# using map
start_time_1 = time.time()
list_of_digits = list(map(int, str(num)))
end_time_1 = time.time()

time_taken_in_micro_1 = (end_time_1 - start_time_1)*(10**6)

print(f"This is the map value: {map(int, str(num))}")
print(list_of_digits)
print(f"Time taken using map: {time_taken_in_micro_1}")
# [1, 2, 3, 4, 5, 6]

start_time_2 = time.time()
# using list comprehension
list_of_digits = [int(x) for x in str(num)]
end_time_2 = time.time()

time_taken_in_micro_2 = (end_time_2 - start_time_2)*(10**6)

print(list_of_digits)
print(f"Time taken using for loop: {time_taken_in_micro_2}")
# [1, 2, 3, 4, 5, 6]
```

## Enumerate

```python
# The following script uses enumerate to iterate through values in a list along with their indices.

my_list = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(my_list):
    # Two different formats to print
    print('{0}: {1}'.format(index, value))
    print(f"{index}: {value}")

# 0: a
# 1: b
# 2: c
# 3: d
# 4: e
```

## Flattening Lists

```python
# Need to install the package - iteration_utilities using 
#   ```$ pip3 install iteration_utilities```

from iteration_utilities import deepflatten

# if you only have one depth nested_list, use this
def flatten(l):
    return [item for sublist in l for item in sublist]

l = [[1,2,3],[3]]
print(flatten(l))
# [1, 2, 3, 3]

# if you don't know how deep the list is nested
l = [[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]

print(list(deepflatten(l, depth=3)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Memory Usage

```python
import sys

num = 21

print(sys.getsizeof(num))
```

## Dict Merge

```python
dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
# Values from the second dictionary are used in case of intersections.

# Output
# {'apple': 9, 'banana': 4, 'orange': 8}
```

## List Multiplication

```python
# Multiplying each element in a list by 2

original_list = [1,2,3,4]

new_list = [2*x for x in original_list]

print(new_list)
# [2,4,6,8]
```

## Palindrome

```python
my_string = "abcba"

if my_string == my_string[::-1]:
    print("palindrome")
else:
		print("not palindrome")
```

## Reverse String 

```python
# Reversing a string using slicing

my_string = "Test Scenario"
reversed_string = my_string[::-1]

print(reversed_string)
```

## Snake Case

```python
# https://python.30secondsofcode.org/list
# Converts a string to snake case. Break the string into words and combine them adding _ as a separator, using a regexp.

import re

def snake(s):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1',
    re.sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

# EXAMPLES
# snake('camelCase') # 'camel_case'
# snake('some text') # 'some_text'
# snake('some-mixed_string With spaces_underscores-and-hyphens') # 'some_mixed_string_with_spaces_underscores_and_hyphens'
# snake('AllThe-small Things') # "all_the_smal_things"
```

## Exec time

```python
import time

start_time = time.time()
# Code to check
a, b = 1,2
c = a + b
# Code to check
end_time = time.time()
time_taken_in_micro = (end_time- start_time)*(10**6)

print(f"Time taken in micro_seconds: {time_taken_in_micro} ms")
```

## Exception Handling

```python
a, b = 1, 1

try:
    print(a/b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
# else statement is run when there is no exception raised in the try block.
else:
    print("no exceptions raised")
# If you need to run something irrespective of exception, use finally.
finally:
    print("Run this always")
```

## Unique Elements

```python
my_string = "aabbbbbbccccddddeee"

# converting the string to a set
temp_set = set(my_string)

# all elements in a set are unique.

# stitching set into a string using join
new_string = ''.join(temp_set)

print(new_string)
```