'''
5. Given the list ["nail", "shoe",
   "horse", "rider",
   "message", "battle",
   "kingdom"],
   you will output the full text of this proverbial rhyme.
   For want of a nail the shoe was lost.
   For want of a shoe the horse was lost.
   For want of a horse the rider was lost.
   For want of a rider the message was lost.
   For want of a message the battle was lost.
   For want of a battle the kingdom was lost.
   And all for the want of a nail.
'''

def rhyme(proverblist):
    for i in range(0,len(proverblist)-1):
        print(f"For want of a {proverblist[i]} the {proverblist[i+1]} was lost.")
    print(f"And all for the want of a {proverblist[0]}")

rhyme(proverblist=["nail", "shoe","horse","rider","message","battle","kingdom"])