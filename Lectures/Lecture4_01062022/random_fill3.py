from random import randint
l = []

while len(l) < 25:
    value = randint(1, 50)
    if value not in l:
        l.append(value)

def my_max(list):
    m = 0
    for i in list:
        if i > m:
            m = i
    return m

print(l)
print("max is", my_max(l))