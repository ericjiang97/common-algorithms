# FIT1045 - Introduction to Algorithms and Programming
# Solving the n-Queens Problem using Backtracking
# Based off Core Code by Eric JIANG and Daniel TERRINGTON
# Extended Version by Eric JIANG

import copy
comb = []
listofsolutions = []

# Diagonal Checking Functions
def chkdiag(array):
    for currentrow in range(len(array)):
        currentcol = array[currentrow]
        for newrow in range(currentrow+1,len(array)):
            newcol = array[newrow]
            if abs(newcol-currentcol)==abs(newrow-currentrow):
                return False
    return True

# Main Function
def backtrack(partial,n,solutions):
    possible = []
    if(len(partial) == n  and chkdiag(partial) is True ):
        solutions.append(partial.copy() )
    else:
        possible = getPossible(partial,n,solutions)
        for index in range(len(possible)):
            partial.append(possible[index])
            backtrack(partial,n,solutions)
            partial.remove(possible[index])

# Generate possible solutions for backtrack function
def getPossible(partial,n,solutions):
    array = []
    for value in range(n):
        if len(partial) != 0:
            if value not in partial and value+1!=partial[len(partial)-1] and value-1!=partial[len(partial)-1]: # if row number is not already in partial solution
                array.append(value)
        else:
            array.append(value)
    return array

# Print Table Function
def printtable(arr):
    array = expandtable(arr)
    rowtext=""
    maxspace = 6
    c=len(array)
    r=len(array[c-1])
    line = "  "+ '--------'*(c)+"-"                   # this replaces the ASCII underline method, for Python IDLE support
    length=len(array[0])
    print(line) #header line
    for row in range(0,c):
        print(str(row), end=" |")
        for column in range(0,r):
            boxCharLength = maxspace - len(str(array[row][column]))  # calculates the amount of spacing required to be it look aligned
            if(boxCharLength<=1):
                boxCharLength+=1
            if(array[row][column]==0):
                text=" "
            elif(array[row][column]==1):
                text="Q"
            else:
                text=str(array[row][column])
            rowtext+=" "*(boxCharLength)+text+" |" # prints out the array row by row
        print(rowtext)
        print(line) #prints out bottom line
        rowtext=""
    for i in range(len(array)):
        print(boxCharLength* " "+"  ", end =str(i))
    print("")

def expandtable(oldarray):
    newarray=[]
    for i in range(len(oldarray)):
        newarray.append([])
        for j in range(len(oldarray)):
            newarray[i].append(0)
    for k in range(len(oldarray)):
        newvalue=oldarray[k]
        newarray[k][newvalue]=1
    return newarray

# check horizontal flip
def check_hor_flip(array):
    answerarray=[]
    length = len(array)
    answerarray.append((array[0]))
    for n in range(1,length):
        currentsol = array[n]
        flippedcurrentsol = currentsol[::-1]
        if (flippedcurrentsol not in array[n:]):
            answerarray.append(currentsol)
    return answerarray

# checking vertical flip
def check_vert_flip(array):
    answerstorage = []
    answerstorage.append(array[0])
    # for each record compare
    for n in range(1,len(array)):
        currentsolution = array[n]
        flippedarray = []
        # flip value across vertically
        for i in range(len(currentsolution)):
            flippedarray.append(len(currentsolution)-1-currentsolution[i])
            if(flippedarray not in array):
                answerstorage.append(currentsolution)
    return answerstorage

# simpler rotational function
def rotation(array):
    answerarray = []
    answerarray.append(array[0]) #appends first answer
    for n in range(0,len(array)):
        # n is current array
        # rotate n
        rotatearray = array[n] #array to be rotated
        returnarray = [] #is the first rotated form of array

        for i in range(len(rotatearray)):
            colnum = rotatearray.index(i) # Find position where i is
            rownum = rotatearray[colnum]       # Returns value where i
            # note value = rotatearray[rownum][colnum]
            # has to become rotatearray[colnum][length-rownum]
            rotatecolnum = len(rotatearray)-rownum
            returnarray.append(rotatecolnum)

        returnarray2 = []
        for j in range(len(returnarray)):
            colnum = returnarray.index(i) # Find position where i is
            rownum = returnarray[colnum]       # Returns value where i
            # note value = rotatearray[rownum][colnum]
            # has to become rotatearray[colnum][length-rownum]
            rotatecolnum = len(returnarray)-rownum
            returnarray2.append(returnarray)

# function checks the clockwise flip
def clockwise_rotation(array):
    answerstorage1 = []
    answerstorage1.append(array[0])
    for n in range(0,len(array)):
        expandedarray = expandtable(array[n]) #expand to table form
        clockwise_rotate = []
        clockwiserotate2=[]
        clockwiserotate3=[]
        # Create a expandedtable
        for row in range(0,len(expandedarray)):
            clockwise_rotate.append([])
            clockwiserotate2.append([])
            clockwiserotate3.append([])
            for col in range(0,len(expandedarray)):
                clockwise_rotate[row].append(0)
                clockwiserotate2[row].append(0)
                clockwiserotate3[row].append(0)

        # Rotate Clockwise by 90
        for rowcheck in range(0,len(expandedarray)):
            for colcheck in range(0,len(expandedarray)):
                length  = len(expandedarray)-1
                if(expandedarray[rowcheck][colcheck]==1):
                    clockwise_rotate[colcheck][(length-rowcheck)]=1
        # Rotate Clockwise by 180
        for r2 in range(0,len(clockwise_rotate)):
            for c2 in range(0,len(clockwise_rotate)):
                length  = len(clockwise_rotate)-1
                if(clockwise_rotate[r2][c2]==1):
                    clockwiserotate2[c2][(length-c2)]=1
        # Rotate Clockwise by 270
        for r3 in range(0,len(clockwiserotate2)):
            for c3 in range(0,len(clockwiserotate2)):
                length  = len(clockwiserotate2)-1
                if(clockwiserotate2[r3][c3]==1):
                    clockwiserotate3[c3][(length-c3)]=1
        for m in range(1,len(array)):
            currenttable = expandtable(array[m])
            #expands each individual table to compare with current table
            if(clockwise_rotate not in array and clockwiserotate2 not in array and clockwiserotate3 not in array and array[m] not in answerstorage1):
                answerstorage1.append(array[m])
    return answerstorage1

n = int(input('Enter a value for n: '))
backtrack(comb,n,listofsolutions)
print(listofsolutions)
horizontal = check_hor_flip(listofsolutions)
print(horizontal)
vertical = check_vert_flip(horizontal)
print(vertical)
solutions = clockwise_rotation(vertical)
print(solutions)

'''
if(len(solutions)!=0):
    print(solutions)
    for l in range(0,len(solutions)):
        print('--------------------------------------------------------------------------')
        print('Solution ' + str(l+1))
        print(solutions[l])
        print('--------------------------------------------------------------------------')
        print()
else:
    print('No Solutions')
'''
