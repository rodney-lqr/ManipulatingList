carPrice = [1000000, 2000000, 1400000, 800000, 2500000]

print()
print (max(carPrice))

def maxPrice(carPrice):
    max_price = carPrice[0]
    for car in carPrice:
        if car > max_price:
            max_price = car
    return max_price

print()
print("The maximum price of the cars is: ", maxPrice(carPrice))


def minPrice(carPrice):
    min_price = carPrice[0]
    for car in carPrice:
        if car < min_price:
            min_price = car
    return min_price

print()
print("The minimum price of the cars is: ",minPrice(carPrice))