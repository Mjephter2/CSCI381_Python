from random import randint
l = []

while len(l) < 10:
    value = randint(1, 10)
    if value not in l:
        l.append(value)

print(l)
