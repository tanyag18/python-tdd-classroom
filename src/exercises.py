def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    rev = input_list[::-1]
    return rev

def count_digits(number):
    """
    Return count of digits
    """
    count = 0
    while number != 0: 
        number //= 10
        count+= 1
    return count 