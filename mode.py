words = input().split()
numwords = len(words)
# words is now a list of all strings in the input

# finish the problem!
soln = [None] * numwords  #words to solution of problem
otherword = 0
indcurword = 0
freqofcurword = 0
maxfreq = 0
numsoln = 0
for currentword in words:

	while otherword < numwords:
		#for test
		if currentword == words[otherword]:
			freqofcurword = freqofcurword +1
		otherword = otherword +1


	otherword = 0
	
	if  (maxfreq <= freqofcurword) and (soln.count(currentword)==0):
		
		maxfreq = freqofcurword
		numsoln = numsoln +1
		soln[numsoln-1] = currentword

	indcurword = indcurword +1
	freqofcurword = 0

counteroutput = 0

for removein in range(len(soln)-1,numsoln-1,-1):
	del soln[removein]
	
soln.sort()

while counteroutput < numsoln:
	
	if (words.count(soln[counteroutput]) == maxfreq):
		print(soln[counteroutput])

	counteroutput = counteroutput + 1


