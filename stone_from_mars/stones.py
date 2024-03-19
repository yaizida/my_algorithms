import sys


def mars_stones(order, delevery):
    order = sorted(order)
    delevery = sorted(delevery)
    order_complite = 0
    for i in order:
        if len(delevery) == 0:
            break
        for j in delevery:
            if i <= j:
                order_complite += 1
                delevery.remove(j)
                break

    return order_complite


if __name__ == '__main__':
    many_order = int(sys.stdin.readline().rstrip())
    order = list(map(int, (sys.stdin.readline().rstrip().split())))
    many_delevery = int(sys.stdin.readline().rstrip())
    delevery = list(map(int, (sys.stdin.readline().rstrip().split())))
    print(mars_stones(order, delevery))