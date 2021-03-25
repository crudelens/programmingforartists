'''
1. The list of non-negative integers that are [5,10,7,14,25,36] . Print the square of each number.
   eg for [1,2,3,4] the output would be
   1
   4
   9
   16
'''

def squaringNumbers(listofnumbers):
    for i in range(0,len(listofnumbers)):
        print(listofnumbers[i]**2)

squaringNumbers([5,10,7,14,25,36])