import sys

badwords = {"v","k","j","x","q","z","V","K","J","X","Q","Z"}

for line in sys.stdin:
    counter = 0
    badcount = 0
    usedlets = {}
    if line[0] != "\n":
	    while counter < len(line):
	    	if (line[counter] in badwords) and (line[counter] not in usedlets):
	    		badcount = badcount + 1
	    		usedlets[line[counter]] = "Used"
	    	counter = counter + 1
	    if badcount > 4:
	    	print("BAD")
	    if badcount <= 4:
	    	print("OK")
    pass
