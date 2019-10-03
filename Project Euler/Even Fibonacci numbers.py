"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""



FibList = [0,1]                                                 #Adding first 2 elements of Fibonacci sequence manually

for i in range(0,200):                                          #Range limit is irrelevant
    FibList.append(FibList[i+1] + FibList[i])                   #Adding next Fibonacci number to List
    if FibList[i+2] > 4000000:                                  #Removing the last element if it exceeds 4 million
        FibList.pop(i+2)
        break
        
print(sum(FibList))
