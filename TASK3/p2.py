secret = 7

guess = int(input("Guess the number: "))

if guess == secret:
    print("🎉 You Win!")
else:
    print("❌ Try Again")