friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print("Who will pay the bill?")

# first option
import random
print(random.choice(friends))

# second option
random_friend = random.randint(0, 4)
print(friends[random_friend])