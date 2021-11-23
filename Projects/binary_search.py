def binary_search(list_items, item):
    low = 0 # индекс первого элемента массива
    high = len(list_items) - 1 # индекс последнего элемента массива
    while low <= high:
        mid = int((low + high) / 2)  # индекс среднего элемента массива 
        # (округляет в меньшую сторону, если нецелое число)
        guess = list_items[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

mylist = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(mylist, 13))
        
    
