'''
3. Write a function called raindrops that takes a number.

   - If the number is divisible by 3, it should return “Pling”.
   - If it is divisible by 5, it should return “Plang”.
   - If it is divisible by both 3 and 5, it should return “PlingPlang”.
   - If it is divisible by by 7, it should return "Plong"
   - If it is divisible by both 7 and 5, it should return “PlongPlang”.
   - If it is divisible by both 7 and 3, it should return “PlongPling”.
   - If it is divisible by both 7, 5 and 3, it should return “PlongPlangPling”.
   - Otherwise, it should return the same number.
'''
dict1={3: "Pling", 5: "Plang", 7: "Plong"}
def rd(userin):
    str1=""
    for key,value in dict1.items():
        if userin%key==0:
            str1+=value
            
    return str1

def rainDrops(userin):
    if userin%3==0 and userin%5==0 and userin%7==0:
        return "PlongPlangPling"
    elif userin%3==0 and userin%7==0:
        return "PlongPling"
    elif userin%5==0 and userin%7==0:
        return "PlongPlang"
    elif userin%3==0 and userin%5==0:
        return "PlingPlang"
    elif userin%3==0:
        return "Pling"
    elif userin%5==0:
        return "Plang"
    elif userin%7==0:
        return "Plong"
    else:
        return userin

answer=rd(int(input("Enter a number: ")))
print(answer)
    
    