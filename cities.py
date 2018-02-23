n = int(input())

citydict = {}
for i in range(n):
    start, end = input().split("---")
    citydict[start] = end
    # now we have the two strings for each of the first n lines
    # do something with them!

# you still have to read in the 2nd part of the input
# which consists of the value q followed by the q query lines

# for each query, calculate and print the answer
q = int(input())

for j in range(q):
	citytofind = input()
	counter = 0
	while citytofind != "Edmonton":
		citytofind = citydict[citytofind]
		counter = counter + 1

	print(counter)

