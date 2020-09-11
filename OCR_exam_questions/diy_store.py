purchases = [['Matt Pink Paint', 'Decorating', 6.99],
             ['Floral Wallpaper', 'Decorating', 7.99],
             ['Magnolia Gloss Paint', 'Decorating', 5.49],
             ['Weedkiller', 'Gardening', 2.99],
             ['Picture Frame', 'Decorating', 8.99],
             ['Plug Socket', 'Electrics', 6.99],
             ['Doorbell', 'Electrics', 15.99],
             ['Matt White Paint', 'Decorating', 4.99],
             ['Tiles', 'Decorating', 19.99],
             ['Grass Seed', 'Gardening', 1.99],
             ['Lawnmower', 'Gardening', 129.99]]


# items are given a discount of 10% IF £20 or more is spent on decorating products

# debug and check what comes out
#print(purchases[0][2])

# loop through the array purchases[row,col]

decorating_total_cost = 0
total_cost = 0

for i in range(len(purchases)):

    # i print every line item
    print(purchases[i][0] + " " + str(purchases[i][2]))

    # i accumulate the total cost
    total_cost = total_cost + float(purchases[i][2])
    # print(total_cost)

    # i need to know if it is a decorating item and keep track of that total
    if purchases[i][1] == 'Decorating':
        decorating_total_cost = decorating_total_cost + purchases[i][2]

    # if i send more than £20 on decorating items, i get a 10% discount on all gardening items
    if decorating_total_cost >= 20.00 and purchases[i][1]=="Gardening":
        discount = purchases[i][2] * 0.1
        # i need to print that information when it happens
        print("-" + str(discount))
        # i need to adjust the total in this case
        total_cost = total_cost - discount


# after we have gone through the loop, i print the total
print("Total cost = {0:.2f}".format(round(total_cost,2)))



