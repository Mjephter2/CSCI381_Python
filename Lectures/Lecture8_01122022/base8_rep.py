
def get_num_base8(n):
    rep_list = 8 * [0]
    exp = 7
    while n > 0:
        rep_list[exp] = n % 8
        n = n//8
        exp -= 1
    return rep_list

print(get_num_base8(8**8 - 2))
