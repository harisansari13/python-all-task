try:
    file = open("report.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Report File Not Found")