# read the input
n = int(input())

# solve the problem
mytable = []
mytable.append(1)

counter = 1

while counter <= (n-1):

	mytable.append(1)
	while (len(mytable) > 1) and (mytable[len(mytable)-1] == mytable[len(mytable)-2]):
		del mytable[len(mytable)-1]
		mytable[len(mytable)-1] = mytable[len(mytable)-1] + 1

	counter = counter + 1


# print the answer

print(*mytable)
# ????

# profit!
