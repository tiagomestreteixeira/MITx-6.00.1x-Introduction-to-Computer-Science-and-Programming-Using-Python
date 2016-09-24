low = 0
high = 100
ans = 50
print('Please think of a number between 0 and 100!')
while True:
    print("Is your secret number " + str(ans) + "?")
    user_response = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_response == 'h':
        high = ans
    elif user_response == 'l':
        low = ans
    elif user_response == 'c':
        print("Game over. Your secret number was: 83")
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = int((high + low) / 2.0)

