# For a given value x, make sure all values < x appear to the left and all >= x appear in the right quadrant.
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8  MAKE TWO LISTS TODO oK

from linked_list_class import linked_list_creator


node_list = [3, 5, 8, 5, 10, 2, 1]
linked_list = linked_list_creator(node_list)


def linked_list_partition(linked_list, value):
    holding = []
    print(linked_list)
    print(linked_list.first)
    print("startloop")
    if linked_list.first >= value:
        holding.append(linked_list.first)
    while type(linked_list) != tuple:
        if type(linked_list.next) == tuple:
            if linked_list.first >= value:
                holding.append(linked_list.first)
                break
            else:
                break
        elif linked_list.next.first >= value:
            holding.append(linked_list.next.first)
            print(holding)
            print(linked_list)
            print(linked_list.next.first)
            linked_list.next.first = linked_list.next.next.first
            linked_list = linked_list.next
            print(linked_list.first)
            print(type(linked_list.next))
            print("check")
        else:
            print("lesser")
            print(linked_list.next.first)
            linked_list = linked_list.next
            print(linked_list.first)
            print(type(linked_list.next))
            print("CHecK")
    return linked_list


shoot = linked_list_partition(linked_list, 5)

print(shoot)
print("hek")
print(shoot.first)
print(shoot.next.first)



