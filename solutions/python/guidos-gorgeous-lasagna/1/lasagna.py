"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME=40
PREPARATION_TIME=30

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.

elapsed_bake_time=0

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
   

number_of_layers=5
def preparation_time_in_minutes(number_of_layers):
    """Calculate the prepeartion time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
       
    
    Returns:
        int: The total time (in minutes) preparing.

    This function takes one integer representing the number of lasagna 
    layers. It calculates 
    the total preperation time where each layer takes 2 minutes of preperation.
    
    """
    return number_of_layers*2

def elapsed_time_in_minutes(number_of_layers , elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return (preparation_time_in_minutes(number_of_layers) + elapsed_bake_time)

print("the remaining baing time is",bake_time_remaining(elapsed_bake_time),"the preperation time is ",preparation_time_in_minutes(number_of_layers),"the elapsed time is ",elapsed_time_in_minutes(number_of_layers , elapsed_bake_time))

