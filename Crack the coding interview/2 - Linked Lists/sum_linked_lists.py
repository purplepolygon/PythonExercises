# Sum two linked lists backwards. To do forwards it's just switching variables. Tested with both places > 10.


from linked_list_class import linked_list_creator


node_list = [3, 9, 3]
second_node_list = [1, 2, 6]
ll_one = linked_list_creator(node_list)
ll_two = linked_list_creator(second_node_list)


def sum_linked_lists(ll_one, ll_two):
    ll_three_node_list = []
    digit_three = int(ll_one.first) + int(ll_two.first)
    ll_one.first = ll_one.next.first
    ll_two.first = ll_two.next.first
    digit_two = int(ll_one.first) + int(ll_two.first)
    ll_one.first = ll_one.next.next.first
    ll_two.first = ll_two.next.next.first
    digit_one = int(ll_one.first) + int(ll_two.first)
    digit_four = 0
    print(type(digit_two))
    print("heck")
    print(digit_two)
    print(digit_one)
    if digit_one >= 10:
        digit_one = 10 - digit_one
        digit_four = 1
    if digit_three >= 10:
        digit_three = digit_three - 10
        digit_two += 1
        ll_three_node_list.append(digit_three)
    else:
        ll_three_node_list.append(digit_three)
    if digit_two >= 10:
        digit_two = digit_two - 10
        digit_one += 1
        ll_three_node_list.append(digit_two)
    else:
        ll_three_node_list.append(digit_two)
    if digit_one >= 10:
        digit_one = 10 - digit_one
        digit_four = 1
        ll_three_node_list.append(digit_one)
    else:
        ll_three_node_list.append(digit_one)
    if digit_four == 1:
        ll_three_node_list.append(digit_four)
    else:
        pass
    print(ll_three_node_list)
    ll_three = linked_list_creator(ll_three_node_list)
    return ll_three


checklthree = sum_linked_lists(ll_one, ll_two)


print(checklthree.first)
print(checklthree.next.first)
print(checklthree.next.next.first)
