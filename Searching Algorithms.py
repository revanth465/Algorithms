# Linear Search    |     Time Complexity : O(n)
import random
def linearSearch(numbers, find):
    for i in numbers:
        if(i==find):
            return "Found"
    return "Not Found"
numbers = [1,3,5,23,5,23,34,5,63]
find = 23
print(linearSearch(numbers,find))


# Insertion Sort     |      Time Complexity : O(N^2)

def insertionSort(numbers):
    i = 2
    while(i <= len(numbers)):
        j = i-1
        while( j > 0 ):
            if(numbers[j] < numbers[j-1]):
                temp = numbers[j-1]
                numbers[j-1] = numbers[j]
                numbers[j] = temp
                j -= 1
            else:
                break
        i += 1
    return numbers
                
    

# Binary Search     |     Time Complexity : O(logN)    |    With Insertion Sort : O(N^2)

def binarySearch():
    # Let's build a list of random numbers and a random value to find in the list.
    numbers = [random.randint(1,21) for i in range(10)]
    find = random.randint(1,21)
    numbers = insertionSort(numbers)
    low = 0
    high = len(numbers) -1
    while(low <= high):
        middle = (low + high) /2
        if(numbers[middle] == find):
            return "Number Found"
        elif(find < numbers[middle]):
            high = middle - 1
        else:
            low = middle + 1
    return "Number Not Found"
print(binarySearch())
