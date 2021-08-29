# Delete a given node given you are at that node. Do not return anything but linked list should be one less.
# a - b - c - d - e -> a - b - d - e
# TODO : use an array to mimic a node list for n, that way we can pinpoint specific nodes.


from linked_list_class import linked_list_creator


node_list = ["a", "b", "c",]
linked_list = linked_list_creator(node_list)


def ll_middle_element_remover(linked_list, n):
    n = linked_list
    if n.next == tuple:
        return False
    print(n.first)
    print(n.next.first)
    n.first = n.next.first
    n.next = n.next.next
    return True


ll_middle_element_remover(linked_list, n)
