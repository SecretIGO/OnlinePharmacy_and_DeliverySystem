# library for calculations

def item_total(items):
    items = [1,2,3,4,5]

    items.append(6)

    print("displaying items:")

    i = 0
    sum = 0
    for item in items:
        sum += item
        print(sum)
        i+=1

