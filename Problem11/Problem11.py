arraySize = 20
def createArray():
    file = open('arrayDoc.txt')
    matrix = []
    for var in file:
        arr = var.split('\n')[0].split()
        matrix.append(arr)
    return matrix

def findLargestVert(matrix):
    max = 0
    for i in range(0,arraySize):
        for j in range(0,arraySize-3):
            testMax=1
            for len in range(0,4):
                testMax *= int(matrix[i][j+len])
            if(testMax>max):
                max = testMax
    return max

def findLargestHoriz(matrix):
    max = 0
    for i in range(0,arraySize-3):
        for j in range(0,arraySize):
            testMax=1
            for len in range(0,4):
                testMax *= int(matrix[i+len][j])
            if(testMax>max):
                max = testMax
    return max

def findLargesetDownSlope(matrix):
    max = 0
    for i in range(0,arraySize-3):
        for j in range(0,arraySize-3):
            testMax = 1
            for len in range(0,4):
                testMax *= int(matrix[i+len][j+len])
            if(testMax>max):
                max = testMax
    return max

def findLargestUpSlope(matrix):
    max = 0
    for i in range(3,arraySize):
        for j in range(0,arraySize-3):
            testMax = 1
            for len in range(0,4):
                testMax *= int(matrix[i-len][j+len])
            if(testMax>max):
                max = testMax
    return max


array = createArray()
one = findLargestVert(array)
two = findLargestHoriz(array)
three = findLargesetDownSlope(array)
four = findLargestUpSlope(array)

print("Largest is ", max(one,two,three,four))


