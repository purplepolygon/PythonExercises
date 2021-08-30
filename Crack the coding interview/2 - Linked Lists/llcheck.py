"""NOTE: THIS IS NOT MY CODE NOR MY FILE, I JUST USED IT QUICKLY FOR REFERENCE ON A PROBLEM.
TODO: DELETE AFTER FINISHING LINKED LISTS"""


# # Python3 program to remove duplicates
# # from unsorted linkedlist
#
#
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#
#     def __init__(self):
#
#         self.head = None
#
#     # Function to print nodes in a
#     # given linked list
#     def printlist(self):
#         print("printlistzzzzz")
#         print("wtf")
#         temp = self.head
#
#         while (temp):
#             print(temp.data, end=" ")
#             temp = temp.next
#
#     # Function to remove duplicates from a
#     # unsorted linked list
#     def removeDuplicates(self, headz):
#         print("check")
#         print(headz.data)
#         print(type(headz.next))
#         print(headz.next)
#         # Base case of empty list or
#         # list with only one element
#         if self.head is None or self.head.next is None:
#             return head
#
#         # Hash to store seen values
#         hash = set()
#
#         current = headz
#         hash.add(self.head.data)
#
#         while current.next is not None:
#             print(headz.data)
#             print("wtf")
#             print(hash)
#             if current.next.data in hash:
#                 print(headz.data)
#                 print("is going")
#                 print(hash)
#                 current.next = current.next.next
#                 print(headz)
#                 print(headz.data)
#                 print(hash)
#
#             else:
#                 print("on")
#                 print(headz.data)
#                 print(hash)
#                 hash.add(current.next.data)
#                 current = current.next
#                 print(hash)
#                 print(headz)
#                 print(headz.data)
#
#         return headz
#
#
# # Driver code
# if __name__ == "__main__":
#     # Creating Empty list
#     llist = LinkedList()
#     llist.head = Node(9)
#     second = Node(10)
#     third = Node(11)
#     fourth = Node(1)
#     fifth = Node(1)
#     sixth = Node(1)
#     seventh = Node(13)
#
#     # Connecting second and third
#     llist.head.next = second
#     second.next = third
#     third.next = fourth
#     fourth.next = fifth
#     fifth.next = sixth
#     sixth.next = seventh
#
#     # Printing data
#     print("Linked List before removing Duplicates.")
#     llist.printlist()
#     print("TEST" + "\n")
#     print(llist.head.data)
#     print(llist.head.next)
#     print(llist)
#     llist.removeDuplicates(llist.head)
#     print("shit")
#     print(llist.head.data)
#     print("\nLinked List after removing duplicates.")
#     llist.printlist()
#
