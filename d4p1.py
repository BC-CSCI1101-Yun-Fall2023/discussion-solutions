import random
import sys

secret = random.randint(1,100)

print("Enter guesses between 1 and 100.")
print("Whoever is closest to the secret wins!")
p1 = int(input("Player 1 guess: "))
p2 = int(input("Player 2 guess: "))

if p1 < 1 or p1 > 100 or p2 < 1 or p2 > 100:
    print("Guesses must be between 1 and 100!")
    sys.exit()

p1_distance = abs(p1 - secret)
p2_distance = abs(p2 - secret)

if p1_distance == p2_distance:
    print(f"It's a tie! Secret was {secret}.")
elif p1_distance < p2_distance:
    print(f"P1 wins! Secret was {secret}.")
else:
    print(f"P2 wins! Secret was {secret}.")
