def sum_items(list_items):
    if list_items == []:
        return 0
    return list_items[0] + sum_items(list_items[1:])

def len_list(list_items):
    if list_items == []:
        return 0
    return 1 + len_list(list_items[1:])

list_items = [1, 2, 3, 4, 5]
print(len_list(list_items))