# First-Project-Playground

This repository is going to be a playground for learning python.
We will play around with some of the foundational stuff in python and in the process build an API (ie. a web service)

You wont be running the python code in your browser like you do with Helsinki, instead you will use VScode.

Also, all of your code and code history will go in this github repository so you can learn how `git` works. Its a good practice to use this, and it makes your life easier over time as a project grows.

Some preliminary things you should do before starting

1. Make sure python is installed.  
   In vscode, open up the terminal and type `python3`, or `python`. If it opens up then thats great. It's installed.
2. 2 ways to code in python
   To code in python, you can do it 2 ways, one way is to type the code in a **file** (using a text editor like vscode). The other way is to just type `python3` in the **terminal** and then just type the code in there. The latter is good for playing around with the language and experimenting. The former is better for longer projects that are more than a few lines long.

   For the latter, its painful to just use the default python. It is not very user friendly. Fortunately there is a nicer version just for playing around with on the terminal called `ipython`. Install it by running the following in the terminal: `pip install ipython`. Then you should be able to run it by just typing `ipython`. It should open up just like typing `python3` would, but its a much better thing to look at and use.

   So, you open up a python "terminal" (some call it a "shell") by typing either `python3` or `ipython` (if you want a pretty thing). And you run a python file by typing in the terminal `python3 file_name.py` (or you can press the triangle 'run' button in the top right of vscode).

   Lets try both of these ways, assuming you have everything installed above:

   Open a terminal in vscode and type: `ipython`. Then lets type the standard "hello world"

   ```python3

   name = input("what is your name: ")
   print(f"what is up, {name}")
   ```

   Press enter and you will see that it runs. Then, press the up arrow and you will see that it brings it back into view so you can run it again.

   Lets try something cooler:

   ```python3
    from datetime import datetime

    print(f"the date and time is: {datetime.now()}")
   ```

   in ipython, you get autocompletion which is helpful for when you just arent sure what you can do with something. Lets create an list variable `list_nums`, then type `list_nums.` then press `TAB`, and you will see your options. It looks like the following:

   ```bash
      In [10]: list_nums = []

      In [11]: list_nums.
                      append()  count()   insert()  reverse()
                      clear()   extend()  pop()     sort()
                      copy()    index()   remove()

   ```

   Now lets try running a python file.

   Create a new file in vscode called `first_file.py`

   In the file, lets write another 'hello world':

   ```python3
   your_input = input('input a word: ')

   list_of_stuff = ["some", "random", "words"]

   # add your input to the list
   list_of_stuff.append(your_input)

   print(list_of_stuff)
   ```

   Now, in the terminal, type `python3 first_file.py` and you should see it run.

   Also, you can press the 'run' triangle in the top right of vscode.

3. After you create your file `first_file.py`, lets push it to github.  
   Press the "Source Control" button on the left bar. Then under `Changes` you will see your file. Click the `+` next to the file name to `Stage` the change you made to it. Then type a commit message such as `added a python file in vscode`. Then press `Commit`. Then press `Sync Changes`. Now your code has been pushed to Github.

---

### Now, lets do some practice

Lets create another file called whatever you want, Ill call it `main.py`.

Now, Lets refresh just what a function does in python:

Here is a function that doubles a number

```python3

def double_number(num):
    double = num * 2
    return double
```

Now if you run this file (ie. "script"), nothing will happen. We need to _call_ the function.

Add this to the bottom of the file:

```python3

number = 10
print(double_number(number))
```

Now, you will see some output.

Lets leave that function where it is, and add another function, one that triples a number

**Try this yourself first**

<details>

```python3

def triple_number(num):
    return num * 3
```

</details>

Try adding another function that takes the average of 2 numbers:

<details>

```python3

def average_of_two_nums(num1, num2):
    total_sum = num1 + num2
    return total_sum / 2
```

</details>

Now add a function that takes the average of list of numbers: ie. average([1,2,3]) is 6/3 == 2
If you dont know much about lists, open `ipython` and play around with one

```ipython
In [2]: list_nums = [1,2,3,4,5,6,7]

In [3]: sum(list_nums)
Out[3]: 28

In [4]: len(list_nums)
Out[4]: 7

```

<details>

```python3

def average_of_list(list_nums):
    total_sum = sum(list_nums)
    length_nums = len(list_nums)
    return total_sum / length_nums
```

</details>

---

You should have a nice set of functions that doesnt really do anything useful, but thats ok. Lets say someone on the other side of the world has a use
