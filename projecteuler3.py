# DOES NOT RUN CURRENTLY, WORKED FOR SMALL NUMBERS ONLY
# import math
#
#
# end_list = []
#
#
# def sieve(target):
#     prime_list = [True] * (target + 1)
#     prime_list[0] = prime_list[1] = False
#
#     for i, prime_check in enumerate(prime_list):
#         if prime_check:
#             yield i
#             for j in range(i*i, target, i):
#                 prime_list[j] = False
#
#     for i in range(0, target):
#         if prime_list[i]:
#             end_list.append(i)
#
#
# sieve(970)
# end_list.reverse()
# print(end_list[0])
#
# def largest_prime(n):
#     value = 0
#     for x in range(0, len(end_list)):
#         if n % end_list[x] == 0:
#             print(end_list[x])
#             break
#
# largestprime(970)
