#  Program to test functions a to j.

ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]		    	
#ONE_TEN =  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]   
#ONE_TEN = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]           
                                                        

def main() :
    print("The original data for all functions is: ", ONE_TEN)

    #a. Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swapFirstLast(data)         #call this function      
    print("After swapping first and last: ", data)

    #b. Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shiftRight(data)            #call this function
    print("After shifting right: ", data)

    #c. Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replaceEven(data)           #call this function
    print("After replacing even elements: ", data)

    #d. Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replaceNeighbors(data)      #call this function
    print("After replacing with neighbors: ", data)

    #e. Demonstrate removing the middle element.
    data = list(ONE_TEN)
    removeMiddle(data)          #call this function
    print("After removing the middle element(s): ", data)

    #f. Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    evenToFront(data)           #call this function
    print("After moving even elements: ", data)

    #g. Demonstrate finding the second largest value.
    print("The second largest value is: ", secondLargest(ONE_TEN))

    #h. Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", isIncreasing(ONE_TEN))

    #i. Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN))

    #j. Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", hasDuplicate(ONE_TEN))



def swapFirstLast(data:list)-> list: 
    '''Swap the first and last element in a list.'''
    temp = data[0]
    data[0] = data[9]
    data[9] = temp
    return
                                

def shiftRight(data:list)-> list: 
    '''Shift the elements of list to the right.'''
    temp = data[9]
    length = len(data)
    
    for i in range(-1,-10,-1):
        data[i] = data[i-1]

    data[0] = temp
    return 

        
def replaceEven(data:list)-> list:
    '''Replace even numbers in the list with 0'''
    length = len(data)
    
    for i in range(length):
        if data[i]%2 == 0:
            data[i] = 0
    return


def replaceNeighbors(data:list)-> list: 
    '''For all items except ONE_TEN[0]/[9], replace with larger of its 2 neighbors'''
    length = len(data)
    for i in range(1, length - 1):
    
        if data[i-1] >= data[i+1]: 
            data[i] = data[i-1]
        
        elif data[i+1] >= data[i-1]: 
            data[i] = data[i+1]
    return


def removeMiddle(data:list)-> list: 
    '''Removes middle element if list len is odd, removes 2 middle if list len is even'''
    length = len(data)
    middleEven = int(length/2)
    middleOdd = int(length//2)
    
    if length % 2 == 0:
        data.pop(middleEven)    
        data.pop(middleEven-1)

    if length % 2 != 0:
        data.pop(middleOdd+1)
        
    return


def evenToFront(data:list)-> list:   
    '''Moves all even elements to the front, then preserving the order for the remaining elements'''
    newList = list(data)
    length = len(newList)
    
    oddNum = 0
    evenNum = 0
    data.clear()
    
    for i in range(length):
        if newList[i] % 2 == 0:
            evenNum = newList[i]
            data.append(evenNum)
            
    for i in range(length):
        if newList[i] % 2 != 0:
            oddNum = newList[i]
            data.append(oddNum)
    return


def secondLargest(ONE_TEN: list)-> int: 
    '''Returns the second largest element in the list'''
    data = list(ONE_TEN)
    data.sort(reverse=True)
    secLargest = int(data[1])
    return secLargest


def isIncreasing(ONE_TEN: list)-> bool: 
    '''Returns true if the list is currently sorted in increasing order'''
    length = len(ONE_TEN)

    for i in range(1,length -1):
        if ONE_TEN[i] < ONE_TEN[i+1]:
            return True
        else:
            return False


def hasAdjacentDuplicate(ONE_TEN:list)-> bool: 
    '''Returns true if the list contains 2 adjacent duplicate elements'''
    length = len(ONE_TEN)
    for i in range(length -2):
        if (ONE_TEN[i+1] == ONE_TEN[i]) or (ONE_TEN[i+1] == ONE_TEN[i+2]):
            return True
        else:
            return False


def hasDuplicate(ONE_TEN:list)-> bool: 
    '''Returns true if the list contains duplicate elements anywhere in the list'''
    setOneTen = set(ONE_TEN)
    setLength = len(setOneTen)
    length = len(ONE_TEN)
    
    if length == setLength:
        return False
    else:
        return True
   
if __name__ == "__main__":
    main()
