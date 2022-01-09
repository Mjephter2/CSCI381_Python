def my_bin(num):
    """ Returns the binary representation of an integer in base 10

    Args:
        num (int): a positive integer

    Returns:
        str: binary represention
    """
    num_copy = int(num)
    rep = ""
    while num_copy > 0:
        if num_copy % 2 == 0:
            rep = '0' + rep
        else:
            rep = '1' + rep
        num_copy = num_copy//2
    return rep

num = int(input("Enter a positive integer: "))
print(num, "in binary is", my_bin(num))