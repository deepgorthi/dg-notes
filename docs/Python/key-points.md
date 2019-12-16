# Notes
## Key Points About Python:
- Object-Oriented Scripting Language.
- Dynamic & strong typing system.
    - Dynamic types are checked at runtime
    - Strong types don’t change implicitly, can’t add 1 and "something".
- Supports functional concepts like map, reduce, filter, and list comprehension.
- Whitespace delimited (no { or } around code blocks)
- Pseudo-code like syntax
- Extremely popular language used across many different disciplines (academia, data science, scripting, web development, etc.).
- Large open source community and public package index (Pypi).
- Runs on all major operating systems (historically more of a pain to run on Windows than Unix systems). Pre-installed on most *NIX systems.
- Supported by large companies such as Google & YouTube.

## REPL

- Python is an *interpreted language*, and the code is evaluated *line-by-line*. Since each line can be evaluated by itself, the time between evaluating each line doesn’t matter, and this allows us to have a REPL. 
- REPL stands for: Read, Evaluate, Print, Loop. Each line is read, evaluated, the return value is then printed to the screen, and then the process repeats. 
- Python ships with a REPL, and you can access it by running python3.6 from your terminal. 
```bash
$ python3.6
Python 3.6.4 (default, Jan  5 2018, 20:24:27)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

## Some Comments
```python
#!/usr/bin/env python3.6
print("Hello, World")
```
```bash
    $ chmod u+x hello
```

Run the script by using ./hello and we’ll see the same result. 

Let’s create a bin directory and move the script: 
```bash
    $ mkdir ~/bin
    $ mv hello ~/bin/
```

To add this directory to the $PATH in .bashrc:  
```bash
    $ export PATH=$HOME/bin:$PATH
    $ hello # this will run the script from anywhere
```

Triple-quoted string is a `multi-line string` that can functionally work like comments, but they will still be allocated into memory.
```python
"""
This is not a block comment,
but it will work when you need
for some lines of code to not execute.
"""
```

## Str and Numeric types

Some useful snippets on Python:
```python
>>> "double".find('s')
-1
>>> "double".find('u')
2
>>> "double".find('bl')
3
>>> "PassWord123".lower()
'password123'
>>> print("Tab\tDelimited")
Tab     Delimited
>>> print("New\nLine")
New
Line
>>> print("Slash\\Character")
Slash\Character
>>> print("'Single' in Double")
'Single' in Double
>>> print('"Double" in Single')
"Double" in Single
>>> print("\"Double\" in Double")
"Double" in Double
>>> 2 + 2 # Addition
4
>>> 10 - 4 # Subtraction
6
>>> 3 * 9 # Multiplication
27
>>> 5 / 3 # Division
1.66666666666667
>>> 5 // 3 # Floor division, always returns a number without a remainder
1
>>> 8 % 3 # Modulo division, returns the remainder
2
>>> 2 ** 3 # Exponent
8
>>> str(1.1)
'1.1'
>>> int("10")
10
>>> int(5.99999)
5
>>> float("5.6")
5.6
>>> float(5)
5.0
>>> float("1.1 things")
Traceback (most recent call last):
  File "", line 1, in 
ValueError: could not convert string to float: '1.1 things'
```

