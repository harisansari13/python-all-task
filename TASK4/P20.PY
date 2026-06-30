feedback = input("Enter feedback: ")

file = open("feedback.txt", "a")

file.write(feedback + "\n")

file.close()

print("Feedback Saved")