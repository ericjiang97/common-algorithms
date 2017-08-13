def binarySearch(array,targetValue):
    '''
    A Function to Find the Location of An Item
    :param array: the array to look through
    :param targetValue: the value to look for
    :return: the index of the item, otherwise False
    :pre: array must be a sorted list
    '''
    minloc = 0
    maxloc = len(array)-1

    while(minloc <= maxloc):
        middle=(maxloc+minloc)//2
        if(array[middle]==targetValue):
            return middle
        elif(array[middle]>targetValue):
            maxloc=middle-1
        elif(array[middle]<targetValue):
            minloc=middle+1
    return False


if __name__ == "__main__":
    try:
        searchvalue = int(input('Enter number between 1 and 30 to search: '))
        position = binarySearch(listofnumbers,searchvalue)
        print(position)
    except ValueError:
        print('Invalid Value')