blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
pyramid=1
rem_blocks=blocks
while rem_blocks>0:
    print(pyramid*'x')
    height+=1
    rem_blocks=rem_blocks-pyramid
    #pyramid=pyramid*2
    if rem_blocks <= pyramid:
        break
    pyramid+=1
    
print("The height of the pyramid:", height)
