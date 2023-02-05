"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# // TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40

# // TODO: consider defining the 'PREPARATION_TIME' constant
# // equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2


# // TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_of_layers):
    """Calculate the preparation time in minutes."""
    return num_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(num_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes) for preparing and baking the lasagna.

    Function that takes the number of layers added to the lasagna as an argument
    and returns how many minutes have elapsed from when the lasagna went into the
    oven to when it came out based on the `PREPARATION_TIME` and `elapsed_bake_time`.
    """
    return preparation_time_in_minutes(num_of_layers) + elapsed_bake_time
