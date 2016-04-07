array=[]
maxSize = 2000000
for i in range(0,maxSize+1):
    array.append(i)
j = 2
while(j*j<maxSize):
    index=j
    while(index<=maxSize-j):
        index += j
        array[index]=0
    j+=1
sum = 0
for num in array:
    sum += num

print(sum-1)