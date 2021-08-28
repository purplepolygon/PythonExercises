# Write code to remove duplicate items from a linked list.
# How would you solve this if a temporary buffer was not allowed? NO CLUE
# Hours taken to do first part : 4? 5? =(


from linked_list_class import linked_list_creator


node_list = ["e", "b", "b", "c", "d", "d", "e", "b", "b", "b", "a", "a", "b"]
linked_list = linked_list_creator(node_list)


def duplicate_remover(linked_list):
    dupe_checker = set()
    if type(linked_list.first) is str and type(linked_list.next) is tuple:
        return linked_list
    dupe_checker.add(linked_list.first)
    current = linked_list
    while type(current.next) is not tuple:
        if current.next.first not in dupe_checker:
            dupe_checker.add(current.next.first)
            current = current.next
        else:
            current.next = current.next.next
    return linked_list


print(duplicate_remover(linked_list))
print(linked_list.first)
linked_list = linked_list.next
print(linked_list.first)
linked_list = linked_list.next
print(linked_list.first)
linked_list = linked_list.next
print(linked_list.first)
linked_list = linked_list.next
print(linked_list.first)

