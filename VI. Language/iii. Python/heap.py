# Modified Author: Inyong Hwang
# 2020-04-09-Thu


def heapify(unheapified, index, heapSize):
    print('heapifiy', unheapified)
    largest = index
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2
    if leftIndex < heapSize and unheapified[leftIndex] > unheapified[largest]:
        largest = leftIndex
    if rightIndex < heapSize and unheapified[rightIndex]  > unheapified[largest]:
        largest = rightIndex
    if largest != index:
        unheapified[largest], unheapified[index] = unheapified[index], unheapified[largest]
        heapify(unheapified, largest, heapSize)
    return None


def heapSort(unheapified, m):
    print('before', unheapified)
    n = len(unheapified)
    if m == 'max': # max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(unheapified, i, n)
    elif m == 'min': # min heap
        for i in range(n-1, 0, -1):
            unheapified[0], unheapified[i] = unheapified[i], unheapified[0]
            heapify(unheapified, 0, i)
    else:
        print('wrong input "m"')
    print('after', unheapified)
    return unheapified

# Reference: https://lsjsj92.tistory.com/472
