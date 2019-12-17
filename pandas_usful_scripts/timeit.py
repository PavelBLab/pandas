import timeit

'''
Why timeit?

Well, how about using simple time module? Just save the time before and after the execution of code and subtract them!
But this method is not precise as there might be a background process momentarily running which disrupts the code
execution and you will get significant variations in running time of small code snippets.
timeit runs your snippet of code millions of time (default value is 1000000) so that you get the statistically most 
relevant measurement of code execution time!
timeit is pretty simple to use and has a command line interface as well as a callable one.

So now, let’s start exploring this handy library!

The module function timeit.timeit(stmt, setup, timer, number) accepts four arguments:
stmt which is the statement you want to measure; it defaults to ‘pass’.
setup which is the code that you run before running the stmt; it defaults to ‘pass’.
We generally use this to import the required modules for our code.
timer which is a timeit.Timer object; it usually has a sensible default value so you don’t have to worry about it.
number which is the number of executions you’d like to run the stmt.

Where the timeit.timeit() function returns the number of seconds it took to execute the code.

'''
# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = ''' 
def example(): 
    mylist = [] 
    for x in range(100): 
        mylist.append(sqrt(x)) 
'''

# timeit statement
print(timeit.timeit(setup=mysetup,
              stmt=mycode,
              number=10000))

'''
The output of above program will be the execution time(in seconds) for 10000 iterations of the code snippet passed to timeit.timeit() function.
Note: Pay attention to the fact that the output is the execution time of number times iteration of the code snippet, not the single iteration. For a single iteration exec. time, divide the output time by number.

The program is pretty straight-forward. All we need to do is to pass the code as a string to the timeit.timeit() function.
It is advisable to keep the import statements and other static pieces of code in setup argument.
'''

'========================================================================='

def my_function():
    y = 3.1415
    for x in range(100):
        y = y ** 0.7
    return y

print(timeit.timeit(my_function, number=100000))


