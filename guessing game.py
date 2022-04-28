import random
number = random.randint(1,10)
guess = ''
while guess != number:
 guess = input(" enter your guess")
 break
guess = int(guess)
if guess < number:
 print("to low")
elif guess > number:
 print("too high")
else:
    print("you won")
print(number)
