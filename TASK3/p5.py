computer = "rock"
user = input("Enter rock/paper/scissors: ")

if user == computer:
    print("Draw")
elif user == "paper":
    print("You Win!")
else:
    print("Computer Wins!")