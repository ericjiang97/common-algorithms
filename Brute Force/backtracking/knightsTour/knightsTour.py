# Main Function
def backtrack(partial,listOfSolutions):
    possible = []
    if(len(nextMoves(partial,listOfSolutions)) == 0 and len(partial) >= 50):
        listOfSolutions.append(partial.copy())
        print(len(partial))
    else:
        possible = nextMoves(partial,listOfSolutions)
        for index in range(len(possible)):
            partial.append(possible[index])
            backtrack(partial,listOfSolutions)
            partial.remove(possible[index])

def nextMoves(history,listOfSolutions):
    current = history[-1]
    availablePositions = []
    potentialMoves = [[-2, 1],[-2, -1],[-1, 2],[-1, -2],[1, 2],[1, -2],[2, -1],[2, 1]]
    for i in range(len(potentialMoves)):
        newPosition = [current[0] + potentialMoves[i][0] , current[1] + potentialMoves[i][1]]
        if(0 <= newPosition[0] <= 7 and 0 <= newPosition[1] <= 7) and newPosition not in history:
            availablePositions.append(newPosition.copy())
    return availablePositions

comb = [[1,2]]
listofsolutions=[]

backtrack(comb,listofsolutions)
print(listofsolutions)
