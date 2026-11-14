def minElement(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp

def maxElement(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
    return temp

a = [24, 345, 453, 2322]
size = len(a)
print("Maximum element of array:", maxElement(a, size))
print("Minimum element of array:", minElement(a, size))