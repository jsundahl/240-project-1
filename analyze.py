from functools import *


def probability_of(c, lines):
    count = sum([int(c.upper() in line) for line in lines])
    return count / len(lines)


def probabilities_of_chars(chars, lines):
    return list(map(lambda x: probability_of(x, lines), chars))


def probabilities_in_files(chars, file_names):
    for name in file_names:
        with open(name, 'r') as f:
            lines = [line for line in f]
        yield probabilities_of_chars(chars, lines)


chars = "abcdefghijklmnopqrstuvwxyz"
file_names = ["us_100.txt", "rus_100.txt"]

probs = [list for list in probabilities_in_files(chars, file_names)]
us_p = probs[0]
rus_p = probs[1]


def get_city_gen(file_names):
    for name in file_names:
        with open(name, 'r') as f:
            for line in f:
                yield line


def letter_pos(c):
    for i in range(0, 26):
        if c == chars[i]:
            return i


def map_for_city(city, us_p, rus_p):
    """
    loop through each letter in this and add the probability it is and subtract the probability it isn't
    """
    pass
