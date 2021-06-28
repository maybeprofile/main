def pi():

    pi = 0
    step = 1
    numerator = 4
    for i in range(1, 10000000):
        a = 2 * (i % 2) - 1
        pi += a * numerator / step
        step += 2
    print(pi)


print(pi())
