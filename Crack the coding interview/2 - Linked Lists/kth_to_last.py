# Implement algorithm to find elements from kth element to last of single linked list


from linked_list_class import linked_list_creator


node_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
linked_list = linked_list_creator(node_list)


def kth_creator():
    return linked_list_creator(node_list)


def kth_to_last(linked_list, length, k):
    ll_check = linked_list.next
    if type(ll_check) == tuple:
        kth_check = kth_creator()
        for x in range(length - k + 1):
            if x == (length - k):
                return kth_check.first
            else:
                kth_check = kth_check.next
                continue
    else:
        length += 1
        ll_check.first = linked_list.next
        return kth_to_last(ll_check, length, k)


print(kth_to_last(linked_list, 1, 4))
