# Sum squares: Sum of first 10 #'s (1**2+2**2...+10**2) = 385 = n
# Square of the sum of first 10 #'s is (1+2..+10)**2 = 3025 = m, find m - n


def sum_squares(n):
    total, s_total = 0, 0
    for x in range(n + 1):
        total += x*x

    for x in range(n + 1):
        s_total += x

    s_total = s_total**2
    print(s_total - total)


sum_squares(100)


# Can refactor this later using sum algorithm: sum i=1, i, -> n n(n+1)/2
# As well as sum of the squares of first natural number n sum i=1, i**2, -> n  n(n+1)(2n+1) / 6
