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


def get_city_gen(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            yield line[0:-1]


def pos(c):
    for i in range(0, 26):
        if c == chars[i]:
            return i


def map_for_city(city, us_p, rus_p):
    """
    loop through each letter in the alphabet and if its in the city's name multiply it by p(letter), else multiply by p(letter)^c
    """
    def get_char_probs_from(p_list):
        def get_prob_of_char(i):
            if chars[i].upper() in city.upper():
                return p_list[i]
            else:
                return 1 - p_list[i]
        return get_prob_of_char

    def char_probs(p_list):
        char_probs_list = list(map(get_char_probs_from(p_list), range(0, 26)))
        x = reduce(lambda x, y: x * y, char_probs_list)
        return x

    def get_MAP_idx(p_lists):
        probs = list(map(char_probs, p_lists))
        return probs.index(max(probs))

    MAP_idx = get_MAP_idx([us_p, rus_p])
    if MAP_idx == 0:
        return "US"
    else:
        return "Russia"


def print_cities_maps(file_name):
    print('\n'.join(["{},{}".format(city, map_for_city(city, us_p, rus_p)) for city in get_city_gen(file_name)]))

print_cities_maps("rus_50.txt")
print_cities_maps("us_50.txt")
