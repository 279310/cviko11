import random
import matplotlib.pyplot as plt

def bubble_sort(list):
    numbers = list.copy()
    plt.ion()
    plt.show()
    for j in range(len(list)-1):
        status = 0
        for i in range(len(list)-1-j):
            if list[i]>list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                status += 1
            index_highlight1 = i
            index_highlight2 = i + 1
            colors = ["steelblue"] * len(list)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(list)), list, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
        if status == 0:
            break
    plt.ioff()
    plt.show()
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
