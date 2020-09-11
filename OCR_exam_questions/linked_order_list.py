# 2017 Paper 2 June Q2
def linked_order_list(orders):
    finished = False
    print(finished)
    count = 0
    print(count)
    while not finished:
        if orders[1][count] is None:
            finished = True
        else:
            output = orders[0][count]
            print(output)
            print(finished)
            count = orders[1][count]
            print(count)
    output = orders[0][count]
    print(output)


the_orders = [[154, 156, 155, 157], [1, 2, 3, None]]
#the_orders = [[184, 1], [186, 2], [185, 3], [187, None]]
linked_order_list(the_orders)
