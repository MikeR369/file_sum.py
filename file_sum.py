# Author: Michael Russell
# GitHub username: Mike369
# Date: 07/03/2024
# Description: Write a function named file_sum that takes as a parameter the name of a text file that contains a list
# of numbers, one to a line, like this:

def file_sum(input_file):
    """
    Reads a file containing a list of numbers, sums them,
    and writes the result to 'sum.txt'.

    Parameters:
    input_file (str): The name of the input text file containing numbers.

    Returns:
    None
    """
    with open(input_file, 'r') as f:
        numbers = [float(line.strip()) for line in f]

    total = sum(numbers)

    with open('sum.txt', 'w') as f:
        f.write(str(total))
        