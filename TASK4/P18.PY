file = open("log.txt", "r")

count = len(file.readlines())

print("Total Lines =", count)

file.close()