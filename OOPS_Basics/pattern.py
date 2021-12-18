n = int(input("Enter the number:"))
for row in range(1, n+1):
    for j in range(1, row+1):
    	print("*", end=" ")
    print()
    

###############################################################

for row in range(1, n+1):
    print("* "*(row))
