from random import randint

with open('numbers.txt', 'a') as the_file:
    for _ in range(1000000):
        the_file.write(str(randint(0,100000)) + "\n")