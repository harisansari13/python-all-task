file = open("report.txt", "r")

text = file.read()

words = len(text.split())

print("Total Words =", words)

file.close()