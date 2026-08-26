enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    """potion_strength has local scope since it's inside a function 
    and can only be called within the function"""
    print(potion_strength)

drink_potion()

# Global Scope
player_health = 10
"""player_health has global scope because it can be defined anywhere 
(inside and outside functions) because it's not within a function"""

def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
        print(player_health)
    drink_potion()

# Global and Local scope can apply to variables, functions, and anything else you name (namespace)
# Namespace: anything you give a name too and is valid in certain scopes
