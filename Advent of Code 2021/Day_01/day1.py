#!usr/bin/env python3


def depth_increase_counter():
    depth_file = open("input.txt", "r")
    depth_list = []
    for line in depth_file:
        stripped_line = line.strip()
        depth_list.append(stripped_line)
    depth_file.close()
    j = 1
    increase_counter = 0
    for i in range(0, len(depth_list) - 1):
        if int(depth_list[i]) < int(depth_list[j]):
            increase_counter += 1
            i += 1
            j += 1
            continue
        else:
            j += 1
            i += 1
            continue
    return increase_counter


print(depth_increase_counter())


def three_sum_increase_counter():
    depth_file = open("input.txt", "r")
    depth_list = []
    for line in depth_file:
        stripped_line = line.strip()
        depth_list.append(stripped_line)
    depth_file.close()
    j = 1
    k = 2
    increase_counter = 0
    for i in range(0, len(depth_list) - 3):
        if int(depth_list[i]) + int(depth_list[j]) + int(depth_list[k]) < int(depth_list[i+1]) + int(depth_list[j+1]) + int(depth_list[k+1]):
            increase_counter += 1
            i += 1
            j += 1
            k += 1
        else:
            i += 1
            j += 1
            k += 1
    return increase_counter


print(three_sum_increase_counter())
