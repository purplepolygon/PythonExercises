# Used to quickly generate generic linked list for rest of problems in this set


class LinkedList:
    def __init__(self, first, next = ()):
        self.first = first
        self.next = next


def linked_list_creator(regular_list):
    assert len(regular_list) > 0
    if len(regular_list) == 1:
        return LinkedList(regular_list[0])
    else:
        return LinkedList(regular_list[0], linked_list_creator(regular_list[1:]))


if '__name__' == '__main__':
    pass
else:
    print("LinkedList created")
