import random
import time

def search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def search_binary(list, target, limite_inferior = None,
limite_superior = None):
    if limite_inferior is None:
        limite_inferior = 0
    if limite_superior is None:
        limite_superior = len(list)-1

    if limite_superior <  limite_inferior:
        return -1
    
    middle = (limite_inferior + limite_superior) // 2

    if list[middle] == target:
        return middle
    elif target < list[middle]:
        return search_binary(list, target, limite_inferior, middle-1)
    else:
        return search_binary(list, target, middle+1, limite_superior)
