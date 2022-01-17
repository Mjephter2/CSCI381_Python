my_string = 'abcdef'

def gen_char(s):
    i = 0
    while True:
        yield s[i]
        i = (i+1) % len(s)

my_generator = gen_char(my_string)

for i in range(10):
    print(next(my_generator))