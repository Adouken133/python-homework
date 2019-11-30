marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

first = line.find(marker)

s = len(marker)

replaced = line[0:first] + replacement + line[first + s:]

print (replaced)

