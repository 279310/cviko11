import random

def bubble_sort(list):
    numbers = list.copy()
    for j in range(len(list)-1):
        status = 0
        for i in range(len(list)-1-j):
            if list[i]>list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                status += 1
        if status == 0:
            break
    return list

def selection_sort(list):
    numbers = list.copy()
    for i in range(len(list)):
        smallest = list[i]
        index = i
        for j in list[i::]:
            if j < smallest:
                smallest = j
                index = list.index(j)
        list[i], list[index] = list[index], list[i]
    return(list)


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

print(bubble_sort(random_numbers(10)))
