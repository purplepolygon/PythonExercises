#!usr/bin/env python3

def file_opener():
    with open('input.txt') as samp:
        lines = samp.readlines()
        position_tuples = tuple(tuple(line.split()) for line in lines)
        return position_tuples


def position_finder():
    tuples = file_opener()
    horizontal_position = 0
    depth = 0
    for x in range(len(tuples)):
        if tuples[x][0] == "forward":
            horizontal_position += int(tuples[x][1])
        elif tuples[x][0] == "down":
            depth += int(tuples[x][1])
        elif tuples[x][0] == "up":
            depth -= int(tuples[x][1])
    product = horizontal_position * depth
    return product


print(position_finder())


def weird_aim_position_finder():
    tuples = file_opener()
    horizontal_position = 0
    depth = 0
    aim = 0
    for x in range(len(tuples)):
        if tuples[x][0] == "forward":
            horizontal_position += int(tuples[x][1])
            depth += aim * int(tuples[x][1])
        elif tuples[x][0] == "down":
            aim += int(tuples[x][1])
        elif tuples[x][0] == "up":
            aim -= int(tuples[x][1])
    product = horizontal_position * depth
    return product


print(weird_aim_position_finder())
