import random
import time

quotes = [
    "You are smart and lazy enough to find easier ways to do things.",
    "Start slow until no one can keep up.",
    "Gotta work for that dream life.",
    "You are the smartest person in the room. Use that to your advantage.",
    "You'll never know you can fly until you take the leap.",
    "You miss 100% of the shots you don't take.",
    "Greatness doesn't come from potential, it comes from action.",
    "People think that the sky is the limit until they saw the stars.",
    "Clock is ticking. Are you becoming the person you want to be?"
]

print("\n Lino Motivation Quotes \n")
time.sleep(0.5)

while True:
    print(random.choice(quotes))
    user_input = input("\nPress enter for another, or type 'bye' to exit:").lower()
    if user_input != 'bye':
        print("Stay motivated! Goodbye!")
        break
    print()