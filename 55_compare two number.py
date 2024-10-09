#
# Monika
# Add input as calculator
#

# 1. Input
n1 = int (input ('Number 1:')) #IF YOU ALREADY DECLARE THE NUMBER NAME FIRST, NEXT U DONT HAVE TO WRITE THE "int" AGAIN
n2 = int (input ('Number 2:'))

# 2. Process
if int(n1) > int(n2): #in phyton u have to put : in the end of sentence IMPORTANT !!!!
    bigger = int(n1)
elif int(n1) < int(n2):
    bigger = int(n2)
else :
    bigger = 'same'

# 3. Output
print(f'bigger   : {bigger}')