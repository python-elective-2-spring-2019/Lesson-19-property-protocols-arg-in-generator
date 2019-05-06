"""
    Exercise: Slow down code
    Create a countdown function that takes one argument, the number to count down from.
    (So if you want 5, 4, 3, 2, 1 then countdown(5)).
    Create a decorator that slows down you code by 1 second for each step.
    For this you can use the time module. 
    The countdown function should be a recursive function in order for this to work.
    When done use the decorator on other recursive functions. You can find some other examples 
    in Lesson-13 earlier this semester.
"""
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper

@slow_down
def countdown(from_number):
    # Base Case
    if from_number == 0:
        print('Lift Offf')
    else:
        print(from_number)
        countdown(from_number - 1)
